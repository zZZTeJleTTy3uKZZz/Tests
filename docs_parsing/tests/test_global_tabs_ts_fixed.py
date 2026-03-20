import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('https://nextjs.org/docs/app/getting-started/layouts-and-pages', wait_until='domcontentloaded')
        await page.wait_for_timeout(2000)
        
        tab_names = await page.evaluate('''() => {
            const set = new Set();
            document.querySelectorAll('[data-geist-tabs] button').forEach(b => {
                if(b.innerText.trim()) set.add(b.innerText.trim());
            });
            document.querySelectorAll('div[data-rehype-pretty-code-figure] select option').forEach(opt => {
                if(opt.value) set.add(opt.value);
            });
            return Array.from(set);
        }''')
        
        print("Найдено вкладок:", tab_names)
        
        extracted_data = {} 
        
        for tab_name in tab_names:
            print(f"Извлекаем вкладку {tab_name}...")
            
            # Click buttons
            await page.evaluate(f'''(tabName) => {{
                // Handle select toggles
                document.querySelectorAll('select').forEach(sel => {{
                    const hasOption = Array.from(sel.options).some(o => o.value === tabName);
                    if (hasOption) {{
                        sel.value = tabName;
                        sel.dispatchEvent(new Event('change', {{ bubbles: true }}));
                    }}
                }});
                
                // Handle button toggles
                document.querySelectorAll('button').forEach(b => {{
                    if(b.innerText.trim() === tabName) b.click();
                }});
            }}''', tab_name)
            
            await page.wait_for_timeout(1000) 
                
            # Grab all code blocks in this state
            data = await page.evaluate('''() => {
                const blocks = Array.from(document.querySelectorAll('[data-geist-code-block], div[data-rehype-pretty-code-figure]')).filter(b => b.querySelector('[data-geist-tabs]') || b.querySelector('select'));
                return blocks.map(block => {
                    let activeName = null;
                    
                    const activeBtn = block.querySelector('button[aria-selected="true"], button[data-state="active"]');
                    if (activeBtn) activeName = activeBtn.innerText.trim();
                    
                    if (!activeName) {
                        const sel = block.querySelector('select');
                        if (sel) activeName = sel.value;
                    }
                    
                    let codeText = null;
                    const pre = block.querySelector('pre');
                    if (pre) {
                        const lines = Array.from(pre.querySelectorAll('.line'));
                        if(lines.length > 0) {
                            let rawText = '';
                            for(let i=0; i<lines.length; i++) {
                                rawText += lines[i].innerText + String.fromCharCode(10);
                            }
                            codeText = rawText;
                        } else {
                            codeText = pre.innerText;
                        }
                    }
                    return { activeName, codeText };
                });
            }''')
            
            for idx, block_state in enumerate(data):
                if idx not in extracted_data:
                    extracted_data[idx] = []
                
                if block_state['activeName'] == tab_name and block_state['codeText']:
                    extracted_data[idx].append({ "name": tab_name, "code": block_state['codeText'] })
                    
        print("\nУспешно собраны данные:")
        for idx in extracted_data:
            print(f"--- Блок {idx} ---")
            for tab in extracted_data[idx]:
                print(f"[{tab['name']}] -> {tab['code'][:30]}...")
            
        await browser.close()
        
asyncio.run(main())
