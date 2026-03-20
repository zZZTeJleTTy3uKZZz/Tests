import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://nextjs.org/docs/app/getting-started/installation', wait_until='domcontentloaded')
        
        script = """async () => {
            const delay = ms => new Promise(res => setTimeout(res, ms));
            const tabGroups = Array.from(document.querySelectorAll('[data-geist-tabs]'));
            let res = '';
            
            for(let j=0; j<tabGroups[0].querySelectorAll('button').length; j++) {
                const btn = tabGroups[0].querySelectorAll('button')[j];
                btn.click();
                await delay(300);
                
                res += btn.innerText + ' | ';
                const pre0 = tabGroups[0].closest('[data-geist-code-block]').querySelector('pre');
                res += 'Group 0: ' + pre0.innerText.substring(0, 30) + ' | ';
                
                const pre1 = tabGroups[1].closest('[data-geist-code-block]').querySelector('pre');
                res += 'Group 1: ' + pre1.innerText.substring(0, 30) + '...';
            }
            return res;
        }"""
        val = await page.evaluate(script)
        print(val)
        
        await browser.close()
asyncio.run(main())
