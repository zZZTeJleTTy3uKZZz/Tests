import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://nextjs.org/docs/app/getting-started/layouts-and-pages', wait_until='domcontentloaded')
        
        script = """() => {
            const selects = Array.from(document.querySelectorAll('select')).map(s => {
                return {
                    classes: s.className,
                    options: Array.from(s.options).map(o => o.value)
                }
            });
            const tabs = Array.from(document.querySelectorAll('[data-geist-tabs] button')).map(b => b.innerText);
            return { selects, tabs };
        }"""
        
        print(await page.evaluate(script))
        await browser.close()
        
asyncio.run(main())
