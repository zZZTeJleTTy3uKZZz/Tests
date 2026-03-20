import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://nextjs.org/docs/app/getting-started/installation', wait_until='domcontentloaded')
        
        script = """async () => {
            const delay = ms => new Promise(res => setTimeout(res, ms));
            const main = document.querySelector('article') || document.querySelector('main');
            const tabGroups = Array.from(main.querySelectorAll('[data-geist-tabs]'));
            
            for (let i = 0; i < tabGroups.length; i++) {
                const tabGroup = tabGroups[i];
                let buttons = Array.from(tabGroup.querySelectorAll('button[role="tab"]'));
                if (!buttons.length) buttons = Array.from(tabGroup.querySelectorAll('button'));
                
                const parentBlock = tabGroup.closest('[data-geist-code-block]') || tabGroup.closest('div[data-rehype-pretty-code-figure]') || tabGroup.parentElement.parentElement;
                
                let resHTML = '';
                for (let j = 0; j < buttons.length; j++) {
                    const btn = buttons[j];
                    const tabName = btn.innerText.trim();
                    btn.click();
                    await delay(150);
                    const pre = parentBlock.querySelector('pre');
                    if (pre) {
                        resHTML += 'TAB_START ' + tabName + ' TAB_END <pre><code>' + pre.innerText + '</code></pre>';
                    }
                }
                
                const wrapper = document.createElement('div');
                wrapper.innerHTML = resHTML;
                wrapper.className = 'extracted-tabs-container';
                parentBlock.parentElement.replaceChild(wrapper, parentBlock);
            }
            
            return main.innerHTML;
        }"""
        
        val = await page.evaluate(script)
        print("TAB_START in eval output?", "TAB_START" in val)
        await browser.close()
        
asyncio.run(main())
