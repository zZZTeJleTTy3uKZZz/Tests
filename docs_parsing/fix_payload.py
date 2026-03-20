with open('payload/parser.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the semaphore definition inside main to take config value
old_main = """async def main():
    output_dir = "payload/parsed_pages"
    os.makedirs(output_dir, exist_ok=True)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        context = await browser.new_context(viewport={"width": 1280, "height": 720}, user_agent=user_agent)"""

new_main = """async def parse_with_config(config):
    output_dir = "payload/parsed_pages"
    os.makedirs(output_dir, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=config.get("headless", True))
        user_agent = config.get("user_agent", "Mozilla/5.0")
        context = await browser.new_context(
            viewport=config.get("browser_viewport", {"width": 1280, "height": 720}), user_agent=user_agent
        )"""

text = text.replace(old_main, new_main)

old_sem = """        print(f"Запускаем парсинг {len(links_to_parse)} страниц...")
        semaphore = asyncio.Semaphore(5)"""

new_sem = """        print(f"Запускаем парсинг {len(links_to_parse)} страниц...")
        max_conn = config.get("max_concurrent_connections", 5)
        semaphore = asyncio.Semaphore(max_conn if max_conn > 0 else 1000)"""

text = text.replace(old_sem, new_sem)

# Create a backward-compatible main()
new_fallback_main = """        print(f"Готово! Сохранено в {merged_file}")
        await browser.close()


async def main():
    await parse_with_config({
        "max_concurrent_connections": 5,
        "browser_viewport": {"width": 1280, "height": 720},
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "headless": True
    })

if __name__ == "__main__":"""

text = text.replace("        print(f\"Готово! Сохранено в {merged_file}\")\n        await browser.close()\n\nif __name__ == \"__main__\":", new_fallback_main)

with open('payload/parser.py', 'w', encoding='utf-8') as f:
    f.write(text)

