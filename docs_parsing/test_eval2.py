import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://nextjs.org/docs/app/getting-started/installation', wait_until='domcontentloaded')
        
        script = """async () => {
                const delay = ms => new Promise(res => setTimeout(res, ms));
                const h1 = document.querySelector('h1');
                if (!h1) return 'No h1';
                const main = document.querySelector('article') || h1.parentElement;
                
                if (main) {
                    const tabGroups = Array.from(main.querySelectorAll('[data-geist-tabs]'));
                    
                    for (let i = 0; i < tabGroups.length; i++) {
                        const tabGroup = tabGroups[i];
                        let buttons = Array.from(tabGroup.querySelectorAll('button[role="tab"]'));
                        if (!buttons.length) buttons = Array.from(tabGroup.querySelectorAll('button'));
                        if (!buttons.length) continue;
                        
                        const parentBlock = tabGroup.closest('[data-geist-code-block]') || tabGroup.closest('div[data-rehype-pretty-code-figure]') || tabGroup.parentElement.parentElement;
                        
                        if (!parentBlock) continue;
                        
                        let resHTML = '';
                        
                        for (let j = 0; j < buttons.length; j++) {
                            const btn = buttons[j];
                            const tabName = btn.innerText.trim();
                            if(!tabName) continue;
                            
                            btn.click();
                            await delay(150);
                            
                            const pre = parentBlock.querySelector('pre');
                            if (pre) {
                                const lines = Array.from(pre.querySelectorAll('.line'));
                                let codeText = '';
                                if(lines.length > 0) {
                                    for(let k=0; k<lines.length; k++) {
                                        codeText += lines[k].innerText + String.fromCharCode(10);
                                    }
                                } else {
                                    codeText = pre.innerText;
                                }
                                
                                resHTML += '<br><strong>TAB_START ' + tabName + ' TAB_END</strong><pre><code>' + codeText.replace(/</g, '&lt;').replace(/>/g, '&gt;') + '</code></pre>';
                            }
                        }
                        
                        if (resHTML !== '') {
                            const newEl = document.createElement('div');
                            newEl.className = 'extracted-tabs-container';
                            newEl.innerHTML = resHTML;
                            // WE HAVE TO USE insertBefore + remove!!!
                            // parentBlock.outerHTML fails inside the full loop context for some React reason
                            parentBlock.parentNode.insertBefore(newEl, parentBlock);
                            parentBlock.remove();
                        }
                    }
                    return main.innerHTML.substring(0, 1000);
                }
                return 'No main';
            }"""
        
        val = await page.evaluate(script)
        print("TAB_START in eval output?", "TAB_START" in val)
        await browser.close()
        
asyncio.run(main())
