import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://nextjs.org/docs/app/getting-started/installation', wait_until='domcontentloaded')
        
        script = """() => {
            const tabs = Array.from(document.querySelectorAll('[data-geist-tabs] button')).map(b => b.innerText);
            return tabs;
        }"""
        
        print("Installation tabs:", await page.evaluate(script))
        await browser.close()
        
asyncio.run(main())
