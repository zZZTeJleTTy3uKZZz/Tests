import asyncio
import re
from bs4 import BeautifulSoup
import html2text
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36')
        page = await context.new_page()
        
        print("Загрузка страницы Next.js...")
        await page.goto('https://nextjs.org/docs/app/getting-started/installation', wait_until='domcontentloaded')
        await page.wait_for_selector('h1', timeout=30000)
        
        print("Запуск скрипта извлечения...")
        html = await page.evaluate('''async () => {
            const delay = ms => new Promise(res => setTimeout(res, ms));
            const main = document.querySelector('article') || document.querySelector('main');
            
            // 1. Находим все блоки с табами
            const blocks = Array.from(main.querySelectorAll('[data-geist-code-block], div[data-rehype-pretty-code-figure]'))
                              .filter(b => b.querySelector('[data-geist-tabs]'));
            
            // 2. Структура для хранения данных (чтобы отвязаться от DOM)
            const extractedData = {};
            
            // Ищем все уникальные имена табов на ВСЕЙ странице
            const allTabNames = new Set();
            blocks.forEach((block, idx) => {
                block.setAttribute('data-tab-block-id', idx);
                extractedData[idx] = [];
                const buttons = Array.from(block.querySelectorAll('button[role=\"tab\"], [data-geist-tabs] button'));
                buttons.forEach(btn => {
                    const name = btn.innerText.trim();
                    if (name) allTabNames.add(name);
                });
            });
            
            // 3. СБОР ДАННЫХ по каждому глобальному стейту
            for (const tabName of allTabNames) {
                // Находим все кнопки с таким именем и кликаем
                const allButtons = Array.from(main.querySelectorAll('button[role=\"tab\"], [data-geist-tabs] button'));
                const targetButtons = allButtons.filter(b => b.innerText.trim() === tabName);
                
                if (targetButtons.length > 0) {
                    // Достаточно кликнуть по одной (так как стейт глобальный), но кликнем по всем для надежности
                    targetButtons.forEach(b => b.click());
                    await delay(300); // Ждем пока React перерисует все блоки
                    
                    // Теперь собираем текст из всех блоков
                    blocks.forEach((block, idx) => {
                        const pre = block.querySelector('pre');
                        if (pre) {
                            // Проверяем, активна ли текущая вкладка в ЭТОМ блоке
                            // Если у блока вообще нет вкладки 'yarn', он может показывать что-то другое
                            const activeBtn = block.querySelector('button[aria-selected=\"true\"], button[data-state=\"active\"]');
                            const currentActiveName = activeBtn ? activeBtn.innerText.trim() : null;
                            
                            // Записываем только если активная вкладка реально совпадает с той, которую мы тестируем
                            if (currentActiveName === tabName) {
                                const lines = Array.from(pre.querySelectorAll('.line'));
                                let codeText = ''; if (lines.length>0) { for(let z=0; z<lines.length; z++) codeText += lines[z].innerText + String.fromCharCode(10); } else { codeText = pre.innerText; }
                                extractedData[idx].push({ name: tabName, code: codeText });
                            }
                        }
                    });
                }
            }
            
            // 4. ЗАПИСЬ ДАННЫХ (Модификация DOM)
            // Делаем это одним проходом в самом конце, чтобы React не успел ничего сломать
            blocks.forEach((block, idx) => {
                const data = extractedData[idx];
                if (data && data.length > 0) {
                    let resHTML = '';
                    data.forEach(d => {
                        resHTML += '<br>MAGICSTART' + d.name + 'MAGICEND<pre><code>' + d.code.replace(/</g, '&lt;').replace(/>/g, '&gt;') + '</code></pre>';
                    });
                    
                    const div = document.createElement('div');
                    div.className = 'extracted-tabs-container';
                    div.innerHTML = resHTML;
                    block.replaceWith(div);
                }
            });
            
            // Очищаем оставшийся мусор
            main.querySelectorAll('nav').forEach(n => n.remove());
            main.querySelectorAll('button[aria-label=\"Copy code\"], button').forEach(b => {
                if (b.innerText.toLowerCase().includes('copy') || b.querySelector('svg')) {
                    if (!b.getAttribute('role') || b.getAttribute('role') !== 'tab') b.remove();
                }
            });
            
            main.querySelectorAll('pre').forEach(pre => {
                if(pre.closest('.extracted-tabs-container')) return;
                pre.querySelectorAll('.line-number').forEach(n => n.remove());
                const lines = Array.from(pre.querySelectorAll('.line'));
                let codeText = ''; if (lines.length>0) { for(let z=0; z<lines.length; z++) codeText += lines[z].innerText + String.fromCharCode(10); } else { codeText = pre.innerText; }
                pre.innerHTML = '<code>' + codeText.replace(/</g, '&lt;').replace(/>/g, '&gt;') + '</code>';
            });
            
            // Мгновенно возвращаем HTML, пока React не запустил Hydration
            return main.innerHTML;
        }''')
        
        print("Конвертация в Markdown...")
        h2t = html2text.HTML2Text()
        h2t.body_width = 0
        h2t.mark_code = True
        
        soup = BeautifulSoup(html, "html.parser")
        md_text = h2t.handle(str(soup))
        
        # Очистка markdown блоков кода
        md_text = re.sub(r'\[code\](.*?)\[/code\]', lambda m: '```\n' + m.group(1).strip() + '\n```', md_text, flags=re.DOTALL)
        def remove_extra_newlines(match):
            cleaned = re.sub(r'\n{3,}', '\n\n', match.group(1))
            return f"```\n{cleaned.strip()}\n```"
        md_text = re.sub(r'```(.*?)```', remove_extra_newlines, md_text, flags=re.DOTALL)
        
        # Подставляем красивые заголовки для табов
        md_text = md_text.replace("MAGICSTART", "\n\n### [").replace("MAGICEND", "]\n")
        
        with open("test_result.md", "w", encoding="utf-8") as f:
            f.write(md_text)
            
        print("Успешно сохранено в tests/test_result.md")
        await browser.close()

asyncio.run(main())
