import asyncio
import os
from bs4 import BeautifulSoup
import html2text
from playwright.async_api import async_playwright
import re

BASE_URL = "https://nextjs.org/docs"
DOMAIN = "https://nextjs.org"

h2t = html2text.HTML2Text()
h2t.body_width = 0
h2t.ignore_links = False
h2t.ignore_images = False
h2t.mark_code = True
h2t.wrap_links = False
h2t.default_image_alt = "image"


async def get_all_links(page):
    print("Получаем список страниц документации Next.js...")
    await page.goto(BASE_URL, wait_until="domcontentloaded")

    links_data = await page.evaluate("""async () => {
        const results = [];
        const sidebars = Array.from(document.querySelectorAll('nav'));
        let nav = null;
        let maxLinks = 0;
        
        // Ищем тот nav, в котором больше всего ссылок на документацию
        for(const n of sidebars) {
            const links = n.querySelectorAll('a[href^="/docs"]');
            if(links.length > maxLinks) {
                maxLinks = links.length;
                nav = n;
            }
        }
        
        if (!nav) return [];
        
        const seen = new Set();
        
        function walk(element, depth) {
            if (!element) return;
            
            if (element.tagName === 'A') {
                const href = element.href.split('#')[0];
                if (href.includes('/docs') && !seen.has(href)) {
                    seen.add(href);
                    results.push({ type: 'link', href: href, text: element.innerText.trim(), depth: depth });
                }
            } 
            
            Array.from(element.children).forEach(child => {
                let newDepth = depth;
                if (child.tagName === 'UL') {
                    // Если это вложенный UL, увеличиваем глубину
                    if (depth >= 0) newDepth++;
                    else newDepth = 0;
                }
                walk(child, newDepth);
            });
        }
        
        walk(nav, -1);
        
        return results;
    }""")

    print(f"Найдено ссылок: {len(links_data)}.")
    return links_data


def clean_markdown_codeblocks(md_text):
    md_text = re.sub(
        r"\[code\](.*?)\[/code\]",
        lambda m: "```\n" + m.group(1).strip() + "\n```",
        md_text,
        flags=re.DOTALL,
    )

    def remove_extra_newlines(match):
        cleaned = re.sub(r"\n{3,}", "\n\n", match.group(1))
        return f"```\n{cleaned.strip()}\n```"

    return re.sub(r"```(.*?)```", remove_extra_newlines, md_text, flags=re.DOTALL)


async def parse_page(context, item, output_dir, index, semaphore):
    url = item["href"]
    async with semaphore:
        print(f"Парсинг [{index}]: {url}")
        page = await context.new_page()
        try:
            # Блокируем трекеры и картинки, но аккуратно, чтобы не заблокировать сами страницы с похожими названиями
            await page.route("**/*.{png,jpg,jpeg,webp,gif,svg}", lambda r: r.abort())
            await page.route("**/google-analytics.com/**", lambda r: r.abort())
            await page.route("**/googletagmanager.com/**", lambda r: r.abort())

            await page.goto(url, wait_until="networkidle", timeout=60000)

            # Ждем H1 (на страницах Next.js всегда есть H1)
            await page.wait_for_selector("h1", timeout=30000)

            # Даем React время "ожить"
            await page.wait_for_timeout(1000)
            
            tab_names = await page.evaluate('''() => {
                const set = new Set();
                
                document.querySelectorAll('[data-geist-tabs] button').forEach(b => {
                    if(b.innerText.trim()) set.add(b.innerText.trim());
                });
                
                document.querySelectorAll('select option').forEach(opt => {
                    if(opt.value) set.add(opt.value);
                });
                
                return Array.from(set);
            }''')
            
            extracted_data = {} 
            
            for tab_name in tab_names:
                try:
                    # Next.js блокирует get_by_role("tab"), поэтому используем evaluate для клика по кнопкам табов
                    await page.evaluate(f'''(tabName) => {{
                        // 1. Кликаем по кнопкам
                        document.querySelectorAll('[data-geist-tabs] button').forEach(b => {{
                            if (b.innerText.trim() === tabName) b.click();
                        }});
                        
                        // 2. Меняем скрытые селекты
                        document.querySelectorAll('select').forEach(sel => {{
                            const hasOption = Array.from(sel.options).some(o => o.value === tabName);
                            if (hasOption) {{
                                sel.value = tabName;
                                sel.dispatchEvent(new Event('change', {{ bubbles: true }}));
                            }}
                        }});
                    }}''', tab_name)
                    
                    await page.wait_for_timeout(500) 
                except Exception as e:
                    print(f"Skipping {tab_name}: {e}")
                    continue
                    
                data = await page.evaluate('''() => {
                    const blocks = Array.from(document.querySelectorAll('[data-geist-code-block], div[data-rehype-pretty-code-figure], pre')).map(el => el.closest('[data-geist-code-block]') || el.closest('div[data-rehype-pretty-code-figure]') || el.parentElement).filter((b, i, arr) => b && arr.indexOf(b) === i).filter(b => b.querySelector('[data-geist-tabs]') || b.querySelector('select') || b.parentElement.querySelector('select'));
                    return blocks.map(block => {
                        const activeBtn = block.querySelector('button[aria-selected="true"], button[data-state="active"]');
                        const activeName = activeBtn ? activeBtn.innerText.trim() : null;
                        
                        let codeText = null;
                        const pre = block.querySelector('pre');
                        if (pre) {
                            const lines = Array.from(pre.querySelectorAll('.line'));
                            if(lines.length > 0) {
                                let rawText = '';
                                for(let i=0; i<lines.length; i++) {
                                    rawText += lines[i].innerText + String.fromCharCode(10);
                                }
                                codeText = rawText;
                            } else {
                                codeText = pre.innerText;
                            }
                        }
                        return { activeName: activeName, codeText: codeText };
                    });
                }''')
                
                for idx, block_state in enumerate(data):
                    idx_str = str(idx) # FIX Playwright evaluate param dict keys must be strings
                    if idx_str not in extracted_data:
                        extracted_data[idx_str] = []
                    
                    if block_state['activeName'] == tab_name and block_state['codeText']:
                        extracted_data[idx_str].append({ "name": tab_name, "code": block_state['codeText'] })
                        
            await page.evaluate(f'''(extractedData) => {{
                const blocks = Array.from(document.querySelectorAll('pre')).map(pre => pre.closest('[data-geist-code-block]') || pre.closest('div[data-rehype-pretty-code-figure]') || pre.parentElement);
                
                blocks.forEach((block, idx) => {{
                    const data = extractedData[String(idx)];
                    if (data && data.length > 0) {{
                        // Если собрана всего 1 версия кода (например, это просто блок без табов), не добавляем заголовки
                        if (data.length === 1 && data[0].name === null) return;
                        
                        // Удаляем дубликаты (иногда React сходит с ума и выдает 2 раза одно и то же)
                        const uniqueData = Array.from(new Map(data.map(item => [item.name, item])).values());
                        if (uniqueData.length === 1) return; // Значит табов реально нет
                        let resHTML = '';
                        data.forEach(d => {{
                            resHTML += '<br>MAGICSTART' + d.name + 'MAGICEND<pre><code>' + d.code.replace(/</g, '&lt;').replace(/>/g, '&gt;') + '</code></pre>';
                        }});
                        
                        const div = document.createElement('div');
                        div.className = 'extracted-tabs-container';
                        div.innerHTML = resHTML;
                        block.parentElement.insertBefore(div, block);
                        block.style.display = 'none';
                        block.className = 'do-not-parse';
                    }}
                }});
                
                const main = document.querySelector('article') || document.querySelector('main');
                if (main) {{
                    main.querySelectorAll('nav').forEach(n => n.remove());
                    main.querySelectorAll('button[aria-label="Copy code"], button').forEach(b => {{
                        if (b.innerText.toLowerCase().includes('copy') || b.querySelector('svg')) {{
                            if (!b.getAttribute('role') || b.getAttribute('role') !== 'tab') b.remove();
                        }}
                    }});
                    
                    main.querySelectorAll('pre').forEach(pre => {{
                        if(pre.closest('.extracted-tabs-container')) return;
                        pre.querySelectorAll('.line-number').forEach(n => n.remove());
                        const lines = Array.from(pre.querySelectorAll('.line'));
                        let codeText = lines.length > 0 ? lines.map(l => l.innerText).join(String.fromCharCode(10)) : pre.innerText;
                        pre.innerHTML = '<code>' + codeText.replace(/</g, '&lt;').replace(/>/g, '&gt;') + '</code>';
                    }});
                    
                    main.querySelectorAll('.do-not-parse').forEach(el => el.remove());
                }}
            }}''', extracted_data)
            
            main_html = await page.evaluate("() => { const main = document.querySelector('article') || document.querySelector('main'); return main ? main.innerHTML : ''; }")

            if not main_html:
                return None

            soup = BeautifulSoup(main_html, "html.parser")

            for img in soup.find_all("img"):
                src = img.get("src")
                if src and src.startswith("/"):
                    img["src"] = DOMAIN + src

            markdown_text = h2t.handle(str(soup))
            markdown_text = clean_markdown_codeblocks(markdown_text)

            # Восстанавливаем красивые заголовки для табов
            markdown_text = markdown_text.replace("MAGICSTART", "\n\n### [").replace(
                "MAGICEND", "]\n"
            )

            anchor = f'<a id="page-{index}"></a>\n'
            header = f"{anchor}---\nurl: {url}\n---\n\n"
            markdown_text = header + markdown_text

            path_part = url.replace(DOMAIN + "/docs/", "").strip("/")
            if not path_part:
                path_part = item["text"]
            safe_name = re.sub(r"[^a-zA-Z0-9_\-]", "_", path_part)
            filepath = os.path.join(output_dir, f"{index:02d}_{safe_name}.md")

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(markdown_text.strip() + "\n")

            return {"index": index, "item": item, "filepath": filepath}
        except Exception as e:
            print(f"Ошибка при парсинге {url}: {e}")
            return None
        finally:
            await page.close()


async def parse_with_config(config):
    output_dir = "nextjs/parsed_pages"
    os.makedirs(output_dir, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=config.get("headless", True))
        user_agent = config.get("user_agent", "Mozilla/5.0")
        context = await browser.new_context(
            viewport=config.get("browser_viewport", {"width": 1280, "height": 720}), user_agent=user_agent
        )
        page = await context.new_page()

        menu_items = await get_all_links(page)
        await page.close()

        if not menu_items:
            print("Нет ссылок для парсинга.")
            await browser.close()
            return

        links_to_parse = [item for item in menu_items if item["type"] == "link"]
        print(f"Запускаем парсинг {len(links_to_parse)} страниц...")
        max_conn = config.get("max_concurrent_connections", 5)
        # Если 0, то делаем огромный лимит для "безграничного"
        semaphore = asyncio.Semaphore(max_conn if max_conn > 0 else 1000)

        tasks = []
        for i, item in enumerate(links_to_parse, 1):
            tasks.append(parse_page(context, item, output_dir, i, semaphore))

        parsed_results = await asyncio.gather(*tasks)
        parsed_dict = {
            res["item"]["href"]: res for res in parsed_results if res is not None
        }

        merged_file = "nextjs/nextjs_docs_full.md"
        with open(merged_file, "w", encoding="utf-8") as outfile:
            outfile.write("# Полная документация Next.js\n\n## Оглавление\n\n")

            for item in menu_items:
                indent = "  " * item["depth"]
                if item["type"] == "group":
                    outfile.write(f"{indent}- **{item['text']}**\n")
                elif item["type"] == "link":
                    res = parsed_dict.get(item["href"])
                    if res:
                        outfile.write(
                            f"{indent}- [{item['text']}](#page-{res['index']})\n"
                        )
                    else:
                        outfile.write(f"{indent}- {item['text']} (ошибка парсинга)\n")

            outfile.write("\n---\n\n")

            successful_results = [res for res in parsed_results if res is not None]
            successful_results.sort(key=lambda x: x["index"])
            for res in successful_results:
                with open(res["filepath"], "r", encoding="utf-8") as infile:
                    outfile.write(infile.read())
                    outfile.write("\n\n---\n\n")

        print(f"Готово! Сохранено в {merged_file}")
        await browser.close()


async def main():
    # Fallback for old run behavior without config
    await parse_with_config({
        "max_concurrent_connections": 5,
        "browser_viewport": {"width": 1280, "height": 720},
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "headless": True
    })

if __name__ == "__main__":
    asyncio.run(main())
