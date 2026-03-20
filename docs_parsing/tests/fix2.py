import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36')
        page = await context.new_page()
        await page.goto('https://nextjs.org/docs/app/getting-started/installation', wait_until='domcontentloaded')
        
        script = """async () => {
            const delay = ms => new Promise(res => setTimeout(res, ms));
            const main = document.querySelector('article');
            const blocks = Array.from(main.querySelectorAll('[data-geist-code-block]')).filter(b => b.querySelector('[data-geist-tabs]'));
            
            const allTabNames = new Set();
            blocks.forEach((block) => {
                const buttons = Array.from(block.querySelectorAll('[data-geist-tabs] button'));
                buttons.forEach(btn => allTabNames.add(btn.innerText.trim()));
            });
            
            let res = '';
            for (const tabName of allTabNames) {
                if(!tabName) continue;
                res += 'TESTING TAB: ' + tabName + ' | ';
                
                const allButtons = Array.from(main.querySelectorAll('[data-geist-tabs] button'));
                const targetButtons = allButtons.filter(b => b.innerText.trim() === tabName);
                
                if (targetButtons.length > 0) {
                    targetButtons[0].click();
                    await delay(300);
                    
                    blocks.forEach((block, idx) => {
                        const activeBtn = block.querySelector('button[aria-selected="true"], button[data-state="active"]');
                        const currentActiveName = activeBtn ? activeBtn.innerText.trim() : null;
                        res += currentActiveName + ' ';
                    });
                }
            }
            return res;
        }"""
        val = await page.evaluate(script)
        print(val)
        await browser.close()
asyncio.run(main())
