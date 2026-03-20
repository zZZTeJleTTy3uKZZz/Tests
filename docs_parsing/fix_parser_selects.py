with open("nextjs/parser.py", "r", encoding="utf-8") as f:
    text = f.read()

# Replace the tab clicking logic in the evaluate block

old_js_block = """            tab_names = await page.evaluate('''() => {
                const set = new Set();
                document.querySelectorAll('[data-geist-tabs] button').forEach(b => {
                    if(b.innerText.trim()) set.add(b.innerText.trim());
                });
                return Array.from(set);
            }''')"""

new_js_block = """            tab_names = await page.evaluate('''() => {
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

text = text.replace(old_js_block, new_js_block)

old_click = """                try:
                    await page.get_by_role("tab", name=tab_name, exact=True).first.click(timeout=5000, force=True)
                    await page.wait_for_timeout(500) 
                except Exception:
                    continue"""

new_click = """                try:
                    # Пробуем переключить таб через кнопку (для pnpm/npm)
                    if await page.get_by_role("tab", name=tab_name, exact=True).count() > 0:
                        await page.get_by_role("tab", name=tab_name, exact=True).first.click(timeout=3000, force=True)
                    else:
                        # Если это не кнопка, значит это скрытый Select (TypeScript/JavaScript)
                        await page.evaluate(f'''(tabName) => {{
                            document.querySelectorAll('select').forEach(sel => {{
                                const hasOption = Array.from(sel.options).some(o => o.value === tabName);
                                if (hasOption) {{
                                    sel.value = tabName;
                                    sel.dispatchEvent(new Event('change', {{ bubbles: true }}));
                                }}
                            }});
                        }}''', tab_name)
                    
                    await page.wait_for_timeout(500) 
                except Exception as e:
                    print(f"Skipping {tab_name}: {e}")
                    continue"""

text = text.replace(old_click, new_click)

old_active_name = """                    const activeBtn = block.querySelector('button[aria-selected="true"], button[data-state="active"]');
                    const activeName = activeBtn ? activeBtn.innerText.trim() : null;"""

new_active_name = """                    let activeName = null;
                    
                    // Проверяем табы-кнопки
                    const activeBtn = block.querySelector('button[aria-selected="true"], button[data-state="active"]');
                    if (activeBtn) activeName = activeBtn.innerText.trim();
                    
                    // Если кнопок нет, проверяем селекты (TS/JS)
                    if (!activeName) {
                        const sel = block.querySelector('select');
                        if (sel) activeName = sel.value;
                    }"""

text = text.replace(old_active_name, new_active_name)

# Also fix the filter so it triggers on code blocks with select elements too!
old_filter = """filter(b => b.querySelector('[data-geist-tabs]'))"""
new_filter = """filter(b => b.querySelector('[data-geist-tabs]') || b.querySelector('select'))"""
text = text.replace(old_filter, new_filter)

with open("nextjs/parser.py", "w", encoding="utf-8") as f:
    f.write(text)

