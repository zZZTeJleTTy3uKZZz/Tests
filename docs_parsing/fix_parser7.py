with open("nextjs/parser.py", "r", encoding="utf-8") as f:
    text = f.read()

# Let's completely rework the TS/JS select detection because NextJS places the <select>
# element completely OUTSIDE the main block of code.

# Find the specific block:
# blocks.map(block => {
#     let activeName = null;

old_block_map = """                data = await page.evaluate('''() => {
                    const blocks = Array.from(document.querySelectorAll('[data-geist-code-block], div[data-rehype-pretty-code-figure], pre')).map(el => el.closest('[data-geist-code-block]') || el.closest('div[data-rehype-pretty-code-figure]') || el.parentElement).filter((b, i, arr) => b && arr.indexOf(b) === i).filter(b => b.querySelector('[data-geist-tabs]') || b.querySelector('select') || b.parentElement.querySelector('select'));
                    return blocks.map(block => {
                        let activeName = null;
                        
                        // Проверяем табы-кнопки
                        const activeBtn = block.querySelector('button[aria-selected="true"], button[data-state="active"]');
                        if (activeBtn) activeName = activeBtn.innerText.trim();
                        
                        // Если кнопок нет, проверяем селекты (TS/JS)
                        if (!activeName) {
                            const sel = block.querySelector('select') || block.parentElement.querySelector('select');
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
                        return { activeName: activeName, codeText: codeText };
                    });
                }''')"""

new_block_map = """                data = await page.evaluate(f'''(tabName) => {{
                    const blocks = Array.from(document.querySelectorAll('pre'));
                    return blocks.map(pre => {{
                        const block = pre.closest('[data-geist-code-block]') || pre.closest('div[data-rehype-pretty-code-figure]') || pre.parentElement;
                        let activeName = null;
                        
                        // 1. Проверяем табы-кнопки внутри блока
                        const activeBtn = block.querySelector('button[aria-selected="true"], button[data-state="active"]');
                        if (activeBtn) activeName = activeBtn.innerText.trim();
                        
                        // 2. Если кнопок нет, значит это селект. 
                        // Так как селекты синхронизированы глобально, если мы запрашивали 'TypeScript', 
                        // и мы видим код (а он меняется), мы просто принудительно ставим активное имя = tabName
                        // чтобы он сохранился в массив!
                        if (!activeName) {{
                           const sel = document.querySelector('select'); // Ищем любой селект на странице
                           if (sel) {{
                               activeName = sel.value;
                           }}
                        }}
                        
                        let codeText = null;
                        if (pre) {{
                            const lines = Array.from(pre.querySelectorAll('.line'));
                            if(lines.length > 0) {{
                                let rawText = '';
                                for(let i=0; i<lines.length; i++) {{
                                    rawText += lines[i].innerText + String.fromCharCode(10);
                                }}
                                codeText = rawText;
                            }} else {{
                                codeText = pre.innerText;
                            }}
                        }}
                        return {{ activeName: activeName, codeText: codeText, blockHTML: block.outerHTML.substring(0, 100) }};
                    }});
                }}''', tab_name)"""

text = text.replace(old_block_map, new_block_map)


old_inject = """            await page.evaluate(f'''(extractedData) => {{
                const blocks = Array.from(document.querySelectorAll('[data-geist-code-block], div[data-rehype-pretty-code-figure], pre')).map(el => el.closest('[data-geist-code-block]') || el.closest('div[data-rehype-pretty-code-figure]') || el.parentElement).filter((b, i, arr) => b && arr.indexOf(b) === i).filter(b => b.querySelector('[data-geist-tabs]') || b.querySelector('select') || b.parentElement.querySelector('select'));
                
                blocks.forEach((block, idx) => {{
                    const data = extractedData[String(idx)];
                    if (data && data.length > 0) {{"""

new_inject = """            await page.evaluate(f'''(extractedData) => {{
                const blocks = Array.from(document.querySelectorAll('pre')).map(pre => pre.closest('[data-geist-code-block]') || pre.closest('div[data-rehype-pretty-code-figure]') || pre.parentElement);
                
                blocks.forEach((block, idx) => {{
                    const data = extractedData[String(idx)];
                    if (data && data.length > 0) {{
                        // Если собрана всего 1 версия кода (например, это просто блок без табов), не добавляем заголовки
                        if (data.length === 1 && data[0].name === null) return;
                        
                        // Удаляем дубликаты (иногда React сходит с ума и выдает 2 раза одно и то же)
                        const uniqueData = Array.from(new Map(data.map(item => [item.name, item])).values());
                        if (uniqueData.length === 1) return; // Значит табов реально нет"""

text = text.replace(old_inject, new_inject)

with open("nextjs/parser.py", "w", encoding="utf-8") as f:
    f.write(text)
