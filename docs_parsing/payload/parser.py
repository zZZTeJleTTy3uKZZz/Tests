import asyncio
import os
from bs4 import BeautifulSoup
import html2text
from playwright.async_api import async_playwright
import re

BASE_URL = "https://payloadcms.com/docs/getting-started/what-is-payload"
DOMAIN = "https://payloadcms.com"

h2t = html2text.HTML2Text()
h2t.body_width = 0
h2t.ignore_links = False
h2t.ignore_images = False
h2t.mark_code = True
h2t.wrap_links = False
h2t.default_image_alt = "image"


async def get_all_links(page):
    print("Получаем список страниц документации...")
    # Используем domcontentloaded, так как networkidle может висеть из-за аналитики
    await page.goto(BASE_URL, wait_until="domcontentloaded")
    await page.wait_for_selector("h1", timeout=60000)

    # На сайте Payload CMS боковое меню работает как аккордеон.
    # Если мы просто кликнем на все, некоторые могут закрыться.
    # Поэтому мы будем кликать по одной группе, ждать и собирать ссылки.

    links_data = await page.evaluate("""async () => {
        const results = [];
        const seen = new Set();
        
        const delay = ms => new Promise(res => setTimeout(res, ms));
        
        const nav = document.querySelector('aside [data-orientation="vertical"]')?.parentElement || document.querySelector('aside');
        if (!nav) return [];
        
        // Получаем все группы (H1) и кнопки (H2)
        const elements = Array.from(nav.querySelectorAll('[class*="groupLabel"], button[class*="topic"]'));
        
        let currentGroup = "";
        
        for (const el of elements) {
            if (el.className.includes('groupLabel')) {
                currentGroup = el.innerText.trim();
                results.push({ type: 'group', text: currentGroup, depth: 0 });
            } 
            else if (el.tagName === 'BUTTON') {
                const topicText = el.innerText.trim();
                results.push({ type: 'group', text: topicText, depth: 1 });
                
                // Кликаем, чтобы раскрыть
                if (el.getAttribute('data-state') === 'closed') {
                    el.click();
                    await delay(300); // ждем анимацию
                }
                
                // Собираем ссылки под этой кнопкой (они появляются в соседнем ul)
                const parentDiv = el.parentElement;
                const links = parentDiv.querySelectorAll('a');
                
                links.forEach(a => {
                    const href = a.href.split('#')[0];
                    if (href.includes('/docs') && !seen.has(href)) {
                        seen.add(href);
                        results.push({
                            type: 'link',
                            href: href,
                            text: a.innerText.trim() || href.split('/').pop(),
                            depth: 2
                        });
                    }
                });
            }
        }
        return results;
    }""")

    print(f"Найдено элементов меню: {len(links_data)}.")
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
            # Блокируем аналитику для ускорения
            await page.route(
                "**/*.{png,jpg,jpeg,webp,gif,svg}", lambda route: route.abort()
            )
            await page.route("**/*google-analytics*", lambda route: route.abort())
            await page.route("**/*doubleclick*", lambda route: route.abort())

            await page.goto(url, wait_until="domcontentloaded", timeout=60000)
            await page.wait_for_selector("h1", timeout=30000)

            main_locator = page.locator("main").first
            if await main_locator.count() == 0:
                print(f"Не найден <main> на странице {url}")
                return None

            # Очищаем блоки кода и лишние элементы навигации
            await main_locator.evaluate("""main => {
                // Удаляем номера строк, чтобы они не попадали в код
                main.querySelectorAll('[class*="lineNumber"]').forEach(n => n.remove());
                main.querySelectorAll('pre button, .copy-button').forEach(btn => btn.remove());
                
                // Payload CMS использует div.code-block-wrap или .code-block вместо стандартных pre
                main.querySelectorAll('.code-block-wrap, pre').forEach(block => {
                    const text = block.innerText;
                    block.innerHTML = '<pre><code>' + text.replace(/</g, '&lt;').replace(/>/g, '&gt;') + '</code></pre>';
                });
                main.querySelectorAll('.breadcrumb-list, .TableOfContents_wrap__CXNv1, [class*="TableOfContents"]').forEach(b => b.remove());
            }""")

            html = await main_locator.inner_html()
            soup = BeautifulSoup(html, "html.parser")

            for img in soup.find_all("img"):
                src = img.get("src")
                if src and src.startswith("/"):
                    img["src"] = DOMAIN + src

            markdown_text = h2t.handle(str(soup))
            markdown_text = clean_markdown_codeblocks(markdown_text)

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


async def main():
    output_dir = "payload/parsed_pages"
    os.makedirs(output_dir, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        context = await browser.new_context(
            viewport={"width": 1280, "height": 720}, user_agent=user_agent
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
        semaphore = asyncio.Semaphore(max_conn if max_conn > 0 else 1000)

        tasks = []
        for i, item in enumerate(links_to_parse, 1):
            tasks.append(parse_page(context, item, output_dir, i, semaphore))

        parsed_results = await asyncio.gather(*tasks)
        parsed_dict = {
            res["item"]["href"]: res for res in parsed_results if res is not None
        }

        merged_file = "payload/payload_docs_full.md"
        with open(merged_file, "w", encoding="utf-8") as outfile:
            outfile.write("# Полная документация Payload CMS\n\n## Оглавление\n\n")

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


if __name__ == "__main__":
    asyncio.run(main())
