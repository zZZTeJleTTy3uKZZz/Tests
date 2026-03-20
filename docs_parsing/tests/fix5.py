import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36')
        page = await context.new_page()
        await page.goto('https://nextjs.org/docs/app/getting-started/installation', wait_until='domcontentloaded')
        
        # Use playwright locator click to simulate actual user interaction!
        print("Clicking npm...")
        await page.get_by_role("tab", name="npm", exact=True).first.click()
        await page.wait_for_timeout(500)
        
        script = """() => {
            const blocks = Array.from(document.querySelectorAll('[data-geist-code-block]')).filter(b => b.querySelector('[data-geist-tabs]'));
            let res = '';
            blocks.forEach((block) => {
                const activeBtn = block.querySelector('button[aria-selected="true"], button[data-state="active"]');
                res += (activeBtn ? activeBtn.innerText.trim() : 'NONE') + ' ';
            });
            return res;
        }"""
        print(await page.evaluate(script))
        
        print("Clicking yarn...")
        await page.get_by_role("tab", name="yarn", exact=True).first.click()
        await page.wait_for_timeout(500)
        print(await page.evaluate(script))

        await browser.close()
asyncio.run(main())
