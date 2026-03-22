import asyncio
import os
import re
from urllib.parse import urldefrag, urljoin, urlparse

from bs4 import BeautifulSoup
import html2text
from playwright.async_api import async_playwright

BASE_URL = "https://docs.pencil.dev/"
DOMAIN = "https://docs.pencil.dev"

h2t = html2text.HTML2Text()
h2t.body_width = 0
h2t.ignore_links = False
h2t.ignore_images = False
h2t.mark_code = True
h2t.wrap_links = False
h2t.default_image_alt = "image"


def normalize_url(raw_url):
    if not raw_url:
        return None

    absolute_url = urljoin(DOMAIN, raw_url)
    absolute_url = urldefrag(absolute_url).url

    if not absolute_url.startswith(DOMAIN):
        return None

    if absolute_url != BASE_URL and absolute_url.endswith("/"):
        absolute_url = absolute_url.rstrip("/")

    return absolute_url


def clean_markdown_codeblocks(md_text):
    md_text = re.sub(
        r"\[code\](.*?)\[/code\]",
        lambda match: "```\n" + match.group(1).strip() + "\n```",
        md_text,
        flags=re.DOTALL,
    )

    def remove_extra_newlines(match):
        cleaned = re.sub(r"\n{3,}", "\n\n", match.group(1))
        return f"```\n{cleaned.strip()}\n```"

    md_text = re.sub(r"```(.*?)```", remove_extra_newlines, md_text, flags=re.DOTALL)
    md_text = md_text.replace("Permalink for this section", "")
    return re.sub(r"\n{3,}", "\n\n", md_text)


def absolutize_assets_and_links(soup, current_url):
    for img in soup.find_all("img"):
        src = img.get("src")
        if src:
            img["src"] = urljoin(current_url, src)

    for link in soup.find_all("a"):
        href = link.get("href")
        if href and not href.startswith("#"):
            link["href"] = urljoin(current_url, href)


async def get_all_links(page):
    print("Получаем список страниц документации Pencil...")
    await page.goto(BASE_URL, wait_until="domcontentloaded", timeout=60000)
    await page.wait_for_selector("aside.nextra-sidebar ul", timeout=30000)
    await page.wait_for_timeout(300)

    links_data = await page.evaluate(
        """() => {
            const rootList = document.querySelector('aside.nextra-sidebar ul');
            if (!rootList) return [];

            const results = [];
            const seen = new Set();

            const cleanText = value => (value || '').replace(/\\s+/g, ' ').trim();
            const normalize = href => {
                try {
                    const url = new URL(href, location.origin);
                    url.hash = '';
                    return url.href;
                } catch {
                    return null;
                }
            };

            function walk(list, depth) {
                for (const item of Array.from(list.children)) {
                    if (item.tagName !== 'LI') continue;

                    const directChildren = Array.from(item.children);
                    const link = directChildren.find(child => child.tagName === 'A');
                    const button = directChildren.find(child => child.tagName === 'BUTTON');
                    const nestedList = item.querySelector('ul');

                    if (link) {
                        const href = normalize(link.getAttribute('href'));
                        const text = cleanText(link.textContent);
                        if (href && href.startsWith(location.origin) && !seen.has(href)) {
                            seen.add(href);
                            results.push({ type: 'link', href, text, depth });
                        }
                    } else if (button) {
                        results.push({
                            type: 'group',
                            text: cleanText(button.textContent),
                            depth
                        });
                    }

                    if (nestedList) {
                        walk(nestedList, depth + 1);
                    }
                }
            }

            walk(rootList, 0);
            return results;
        }"""
    )

    print(f"Найдено элементов меню: {len(links_data)}.")
    return links_data


async def extract_main_html(page):
    return await page.evaluate(
        """() => {
            const main =
                document.querySelector('article main[data-pagefind-body="true"]') ||
                document.querySelector('article main') ||
                document.querySelector('main[data-pagefind-body="true"]') ||
                document.querySelector('main');

            if (!main) return '';

            const clone = main.cloneNode(true);
            const escapeHtml = text => text
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;');

            clone.querySelectorAll('iframe, script, style, .subheading-anchor, [aria-label="Permalink for this section"]').forEach(el => el.remove());

            clone.querySelectorAll('pre').forEach(pre => {
                pre.querySelectorAll('button').forEach(button => button.remove());
                const text = (pre.innerText || '').replace(/\\u00a0/g, ' ');
                pre.innerHTML = '<code>' + escapeHtml(text) + '</code>';
            });

            return clone.innerHTML;
        }"""
    )


async def parse_page(context, item, output_dir, index, semaphore):
    url = item["href"]
    async with semaphore:
        print(f"Парсинг [{index}]: {url}")
        page = await context.new_page()
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=60000)
            await page.wait_for_selector("main h1", timeout=30000)
            await page.wait_for_timeout(300)

            main_html = await extract_main_html(page)
            if not main_html:
                print(f"Не найден основной контент: {url}")
                return None

            soup = BeautifulSoup(main_html, "html.parser")
            absolutize_assets_and_links(soup, url)

            markdown_text = h2t.handle(str(soup))
            markdown_text = clean_markdown_codeblocks(markdown_text)

            anchor = f'<a id="page-{index}"></a>\n'
            header = f"{anchor}---\nurl: {url}\n---\n\n"
            markdown_text = header + markdown_text

            path_part = urlparse(url).path.strip("/") or "index"
            safe_name = re.sub(r"[^a-zA-Z0-9_\-]", "_", path_part)
            filepath = os.path.join(output_dir, f"{index:02d}_{safe_name}.md")

            with open(filepath, "w", encoding="utf-8") as file:
                file.write(markdown_text.strip() + "\n")

            return {"index": index, "item": item, "filepath": filepath}
        except Exception as exc:
            print(f"Ошибка при парсинге {url}: {exc}")
            return None
        finally:
            await page.close()


async def parse_with_config(config):
    output_dir = "pencil/parsed_pages"
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(output_dir):
        if filename.endswith(".md"):
            os.remove(os.path.join(output_dir, filename))

    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=config.get("headless", True))
        context = await browser.new_context(
            viewport=config.get("browser_viewport", {"width": 1280, "height": 720}),
            user_agent=config.get("user_agent", "Mozilla/5.0"),
        )

        await context.route("**/*.{png,jpg,jpeg,webp,gif,svg}", lambda route: route.abort())
        await context.route("**/googletagmanager.com/**", lambda route: route.abort())
        await context.route("**/google-analytics.com/**", lambda route: route.abort())

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

        tasks = [
            parse_page(context, item, output_dir, index, semaphore)
            for index, item in enumerate(links_to_parse, 1)
        ]
        parsed_results = await asyncio.gather(*tasks)
        parsed_dict = {
            result["item"]["href"]: result for result in parsed_results if result is not None
        }

        merged_file = "pencil/pencil_docs_full.md"
        with open(merged_file, "w", encoding="utf-8") as outfile:
            outfile.write("# Полная документация Pencil\n\n## Оглавление\n\n")

            for item in menu_items:
                indent = "  " * item["depth"]
                if item["type"] == "group":
                    outfile.write(f"{indent}- **{item['text']}**\n")
                elif item["type"] == "link":
                    result = parsed_dict.get(item["href"])
                    if result:
                        outfile.write(f"{indent}- [{item['text']}](#page-{result['index']})\n")
                    else:
                        outfile.write(f"{indent}- {item['text']} (ошибка парсинга)\n")

            outfile.write("\n---\n\n")

            successful_results = [result for result in parsed_results if result is not None]
            successful_results.sort(key=lambda result: result["index"])
            for result in successful_results:
                with open(result["filepath"], "r", encoding="utf-8") as infile:
                    outfile.write(infile.read())
                    outfile.write("\n\n---\n\n")

        print(f"Готово! Сохранено в {merged_file}")
        await browser.close()


async def main():
    await parse_with_config(
        {
            "max_concurrent_connections": 5,
            "browser_viewport": {"width": 1280, "height": 720},
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "headless": True,
        }
    )


if __name__ == "__main__":
    asyncio.run(main())
