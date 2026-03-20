import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36')
        page = await context.new_page()
        await page.goto('https://nextjs.org/docs/app/getting-started/installation', wait_until='domcontentloaded')
        
        script = """async () => {
            const delay = ms => new Promise(res => setTimeout(res, ms));
            const main = document.querySelector('article');
            const blocks = Array.from(main.querySelectorAll('[data-geist-code-block]')).filter(b => b.querySelector('[data-geist-tabs]'));
            
            let res = '';
            for (const tabName of ['pnpm', 'npm', 'yarn', 'bun']) {
                res += 'TESTING TAB: ' + tabName + ' | ';
                
                const allButtons = Array.from(main.querySelectorAll('[data-geist-tabs] button'));
                
                for(let b of allButtons) {
                    if (b.innerText.trim() === tabName) {
                        // try mousedown mouseup instead of just click
                        b.dispatchEvent(new MouseEvent('mousedown', {bubbles: true}));
                        b.dispatchEvent(new MouseEvent('mouseup', {bubbles: true}));
                        b.click();
                    }
                }
                
                await delay(500);
                
                blocks.forEach((block, idx) => {
                    const activeBtn = block.querySelector('button[aria-selected="true"], button[data-state="active"]');
                    const currentActiveName = activeBtn ? activeBtn.innerText.trim() : 'NONE';
                    res += currentActiveName + ' ';
                });
            }
            return res;
        }"""
        val = await page.evaluate(script)
        print(val)
        await browser.close()
asyncio.run(main())
