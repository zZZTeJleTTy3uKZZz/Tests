with open("nextjs/parser.py", "r", encoding="utf-8") as f:
    text = f.read()

# Fix the bug where it gets an empty array of tab names!
old_find = """            tab_names = await page.evaluate('''() => {
                const set = new Set();
                
                // 1. Стандартные кнопки табов (npm, pnpm)
                document.querySelectorAll('[data-geist-tabs] button').forEach(b => {
                    if(b.innerText.trim()) set.add(b.innerText.trim());
                });
                
                // 2. Скрытые селекты (TypeScript, JavaScript)
                document.querySelectorAll('div[data-rehype-pretty-code-figure] select option').forEach(opt => {
                    if(opt.value) set.add(opt.value);
                });
                
                return Array.from(set);
            }''')"""

new_find = """            tab_names = await page.evaluate('''() => {
                const set = new Set();
                
                document.querySelectorAll('[data-geist-tabs] button').forEach(b => {
                    if(b.innerText.trim()) set.add(b.innerText.trim());
                });
                
                document.querySelectorAll('select option').forEach(opt => {
                    if(opt.value) set.add(opt.value);
                });
                
                return Array.from(set);
            }''')"""

text = text.replace(old_find, new_find)

with open("nextjs/parser.py", "w", encoding="utf-8") as f:
    f.write(text)

