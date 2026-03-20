import asyncio
import re
from bs4 import BeautifulSoup
import html2text
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        # ВАЖНО: Next.js использует Vercel Web Analytics и т.д., не блокируем всё подряд, чтобы скрипты React точно загрузились
        await page.route("**/*.{png,jpg,jpeg,webp,gif,svg}", lambda r: r.abort())
        
        await page.goto('https://nextjs.org/docs/app/getting-started/installation', wait_until='domcontentloaded')
        await page.wait_for_selector('h1', timeout=30000)
        
        # Даем React время "ожить" (Hydration)
        await page.wait_for_timeout(2000)
        
        # 1. Get all unique tab names
        tab_names = await page.evaluate('''() => {
            const set = new Set();
            document.querySelectorAll('[data-geist-tabs] button').forEach(b => {
                if(b.innerText.trim()) set.add(b.innerText.trim());
            });
            return Array.from(set);
        }''')
        print("Найдено вкладок:", tab_names)
        
        extracted_data = {} 
        
        # 2. Iterate through each globally using Playwright clicks
        for tab_name in tab_names:
            print(f"Извлекаем вкладку {tab_name}...")
            
            # Кликаем на самую первую вкладку с таким именем
            # Используем force=True, так как иногда вкладки перекрываются
            try:
                await page.get_by_role("tab", name=tab_name, exact=True).first.click(timeout=5000, force=True)
                # Вы правы! Увеличиваем задержку, чтобы контент 100% обновился!
                await page.wait_for_timeout(1000) 
            except Exception as e:
                print(f"Ошибка при клике на {tab_name}: {e}")
                continue
                
            # Забираем текст
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
                if idx not in extracted_data:
                    extracted_data[idx] = []
                
                # Сохраняем, только если эта вкладка реально переключилась в блоке
                if block_state['activeName'] == tab_name and block_state['codeText']:
                    extracted_data[idx].append({ "name": tab_name, "code": block_state['codeText'] })
                    
        print("\nУспешно собраны данные. Пример первого блока:")
        for tab in extracted_data.get(0, []):
            print(f"[{tab['name']}] -> {tab['code'][:30]}...")
            
        await browser.close()
        
asyncio.run(main())
