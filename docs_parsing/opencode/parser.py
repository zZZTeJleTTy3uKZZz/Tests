import asyncio
import os
from bs4 import BeautifulSoup
import html2text
from playwright.async_api import async_playwright
import re

BASE_URL = "https://opencode.ai/docs/ru"
DOMAIN = "https://opencode.ai"

h2t = html2text.HTML2Text()
h2t.body_width = 0
h2t.ignore_links = False
h2t.ignore_images = False
h2t.mark_code = True
h2t.wrap_links = False
h2t.default_image_alt = "image"

async def get_all_links(page):
    print("Получаем список страниц документации...")
    await page.goto(BASE_URL)
    await page.wait_for_load_state("networkidle")
    
    nav = page.locator('nav[aria-label="Основное"], aside nav').first
    if await nav.count() == 0:
        print("Не найдено меню навигации!")
        return []
    
    links_data = await nav.evaluate('''nav => {
        const results = [];
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
            else if (element.classList && element.classList.contains('group-label')) {
                results.push({ type: 'group', text: element.innerText.trim(), depth: depth });
            }
            
            const children = Array.from(element.children);
            for (const child of children) {
                let newDepth = depth;
                if (child.tagName === 'UL' && !child.classList.contains('top-level')) {
                    newDepth++;
                }
                walk(child, newDepth);
            }
        }
        
        const rootUl = nav.querySelector('.sidebar-content ul.top-level');
        if (rootUl) {
            walk(rootUl, 0);
        } else {
            walk(nav, 0);
        }
        return results;
    }''')
    print(f"Найдено элементов меню: {len(links_data)}.")
    return links_data

def clean_markdown_codeblocks(md_text):
    md_text = re.sub(r'\[code\](.*?)\[/code\]', lambda m: '```\n' + m.group(1).strip() + '\n```', md_text, flags=re.DOTALL)
    def remove_extra_newlines(match):
        cleaned = re.sub(r'\n{3,}', '\n\n', match.group(1))
        return f"```\n{cleaned.strip()}\n```"
    return re.sub(r'```(.*?)```', remove_extra_newlines, md_text, flags=re.DOTALL)

async def parse_page(context, item, output_dir, index, semaphore):
    url = item['href']
    async with semaphore:
        print(f"Парсинг [{index}]: {url}")
        page = await context.new_page()
        try:
            await page.goto(url)
            await page.wait_for_load_state("networkidle")
            
            main_content = page.locator("main")
            if await main_content.count() == 0:
                return None
            
            await main_content.evaluate('''main => {
                main.querySelectorAll('pre button, .copy-button').forEach(btn => btn.remove());
                main.querySelectorAll('pre').forEach(pre => {
                    const text = pre.innerText;
                    pre.innerHTML = '<code>' + text.replace(/</g, '&lt;').replace(/>/g, '&gt;') + '</code>';
                });
            }''')
            
            html = await main_content.inner_html()
            soup = BeautifulSoup(html, "html.parser")
            
            for img in soup.find_all("img"):
                src = img.get("src")
                if src and src.startswith("/"):
                    img["src"] = DOMAIN + src
                    
            markdown_text = h2t.handle(str(soup))
            markdown_text = clean_markdown_codeblocks(markdown_text)
            
            anchor = f"<a id=\"page-{index}\"></a>\n"
            header = f"{anchor}---\nurl: {url}\n---\n\n"
            markdown_text = header + markdown_text
            
            path_part = url.replace(BASE_URL, "").strip("/")
            if not path_part:
                path_part = "index"
            safe_name = re.sub(r'[^a-zA-Z0-9_\-]', '_', path_part)
            filepath = os.path.join(output_dir, f"{index:02d}_{safe_name}.md")
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(markdown_text.strip() + "\n")
                
            return {"index": index, "item": item, "filepath": filepath}
        except Exception as e:
            print(f"Ошибка при парсинге {url}: {e}")
            return None
        finally:
            await page.close()

async def main():
    output_dir = "opencode/parsed_pages"
    os.makedirs(output_dir, exist_ok=True)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1280, "height": 720})
        page = await context.new_page()
        
        menu_items = await get_all_links(page)
        await page.close()
        
        if not menu_items:
            print("Нет ссылок для парсинга.")
            await browser.close()
            return

        links_to_parse = [item for item in menu_items if item['type'] == 'link']
        print(f"Запускаем парсинг {len(links_to_parse)} страниц...")
        semaphore = asyncio.Semaphore(5)
        
        tasks = []
        for i, item in enumerate(links_to_parse, 1):
            tasks.append(parse_page(context, item, output_dir, i, semaphore))
            
        parsed_results = await asyncio.gather(*tasks)
        
        parsed_dict = {res["item"]["href"]: res for res in parsed_results if res is not None}
        
        merged_file = "opencode/opencode_docs_full.md"
        with open(merged_file, "w", encoding="utf-8") as outfile:
            outfile.write("# Полная документация OpenCode\n\n## Оглавление\n\n")
            
            for item in menu_items:
                indent = "  " * item["depth"]
                if item["type"] == "group":
                    outfile.write(f"{indent}- **{item['text']}**\n")
                elif item["type"] == "link":
                    res = parsed_dict.get(item["href"])
                    if res:
                        outfile.write(f"{indent}- [{item['text']}](#page-{res['index']})\n")
                    else:
                        outfile.write(f"{indent}- {item['text']}\n")
                
            outfile.write("\n---\n\n")
            
            successful_results = [res for res in parsed_results if res is not None]
            successful_results.sort(key=lambda x: x["index"])
            for res in successful_results:
                with open(res["filepath"], "r", encoding="utf-8") as infile:
                    outfile.write(infile.read())
                    outfile.write("\n\n---\n\n")
                    
        print(f"Готово! Сохранено в {merged_file}")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
