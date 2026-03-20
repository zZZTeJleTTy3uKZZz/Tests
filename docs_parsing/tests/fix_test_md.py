import asyncio
import re
from bs4 import BeautifulSoup
import html2text
from playwright.async_api import async_playwright
import json

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.route("**/*.{png,jpg,jpeg,webp,gif,svg}", lambda r: r.abort())
        
        await page.goto('https://nextjs.org/docs/app/getting-started/installation', wait_until='domcontentloaded')
        await page.wait_for_selector('h1', timeout=30000)
        
        await page.wait_for_timeout(2000)
        
        tab_names = await page.evaluate('''() => {
            const set = new Set();
            document.querySelectorAll('[data-geist-tabs] button').forEach(b => {
                if(b.innerText.trim()) set.add(b.innerText.trim());
            });
            return Array.from(set);
        }''')
        
        extracted_data = {} 
        
        for tab_name in tab_names:
            try:
                await page.get_by_role("tab", name=tab_name, exact=True).first.click(timeout=5000, force=True)
                await page.wait_for_timeout(1000) 
            except Exception:
                continue
                
            data = await page.evaluate('''() => {
                const blocks = Array.from(document.querySelectorAll('[data-geist-code-block], div[data-rehype-pretty-code-figure]')).filter(b => b.querySelector('[data-geist-tabs]'));
                return blocks.map(block => {
                    const activeBtn = block.querySelector('button[aria-selected="true"], button[data-state="active"]');
                    const activeName = activeBtn ? activeBtn.innerText.trim() : null;
                    
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
                    return { activeName: activeName, codeText: codeText };
                });
            }''')
            
            for idx, block_state in enumerate(data):
                idx_str = str(idx) # FIX Playwright evaluate param dict keys must be strings!
                if idx_str not in extracted_data:
                    extracted_data[idx_str] = []
                
                if block_state['activeName'] == tab_name and block_state['codeText']:
                    extracted_data[idx_str].append({ "name": tab_name, "code": block_state['codeText'] })
                    
        await page.evaluate(f'''(extractedData) => {{
            const blocks = Array.from(document.querySelectorAll('[data-geist-code-block], div[data-rehype-pretty-code-figure]')).filter(b => b.querySelector('[data-geist-tabs]'));
            
            blocks.forEach((block, idx) => {{
                const data = extractedData[String(idx)];
                if (data && data.length > 0) {{
                    let resHTML = '';
                    data.forEach(d => {{
                        resHTML += '<br>MAGICSTART' + d.name + 'MAGICEND<pre><code>' + d.code.replace(/</g, '&lt;').replace(/>/g, '&gt;') + '</code></pre>';
                    }});
                    
                    const div = document.createElement('div');
                    div.className = 'extracted-tabs-container';
                    div.innerHTML = resHTML;
                    block.parentElement.insertBefore(div, block);
                    block.style.display = 'none';
                    block.className = 'do-not-parse';
                }}
            }});
            
            const main = document.querySelector('article') || document.querySelector('main');
            main.querySelectorAll('nav').forEach(n => n.remove());
            main.querySelectorAll('button[aria-label=\"Copy code\"], button').forEach(b => {{
                if (b.innerText.toLowerCase().includes('copy') || b.querySelector('svg')) {{
                    if (!b.getAttribute('role') || b.getAttribute('role') !== 'tab') b.remove();
                }}
            }});
            
            main.querySelectorAll('pre').forEach(pre => {{
                if(pre.closest('.extracted-tabs-container')) return;
                pre.querySelectorAll('.line-number').forEach(n => n.remove());
                const lines = Array.from(pre.querySelectorAll('.line'));
                let codeText = lines.length > 0 ? lines.map(l => l.innerText).join(String.fromCharCode(10)) : pre.innerText;
                pre.innerHTML = '<code>' + codeText.replace(/</g, '&lt;').replace(/>/g, '&gt;') + '</code>';
            }});
            
            main.querySelectorAll('.do-not-parse').forEach(el => el.remove());
            
        }}''', extracted_data)
        
        main_html = await page.evaluate("() => (document.querySelector('article') || document.querySelector('main')).innerHTML")
        
        h2t = html2text.HTML2Text()
        h2t.body_width = 0
        h2t.mark_code = True
        
        soup = BeautifulSoup(main_html, "html.parser")
        md_text = h2t.handle(str(soup))
        
        md_text = re.sub(r'\[code\](.*?)\[/code\]', lambda m: '```\n' + m.group(1).strip() + '\n```', md_text, flags=re.DOTALL)
        def remove_extra_newlines(match):
            cleaned = re.sub(r'\n{3,}', '\n\n', match.group(1))
            return f"```\n{cleaned.strip()}\n```"
        md_text = re.sub(r'```(.*?)```', remove_extra_newlines, md_text, flags=re.DOTALL)
        
        md_text = md_text.replace("MAGICSTART", "\n\n### [").replace("MAGICEND", "]\n")
        
        with open("test_result_final.md", "w", encoding="utf-8") as f:
            f.write(md_text)
            
        await browser.close()
        print("Final render test completed.")

asyncio.run(main())
