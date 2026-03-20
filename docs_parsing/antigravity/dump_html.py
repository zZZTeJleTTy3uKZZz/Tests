import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(
            "https://antigravity.google/docs/get-started", wait_until="networkidle"
        )

        main_html = await page.evaluate("""() => {
            const h1 = document.querySelector('h1');
            return h1 ? h1.parentElement.parentElement.innerHTML : "Not found";
        }""")
        print(main_html[:2000])

        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
