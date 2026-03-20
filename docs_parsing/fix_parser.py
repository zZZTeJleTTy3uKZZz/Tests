with open("nextjs/parser.py", "r", encoding="utf-8") as f:
    text = f.read()

old_click = """                try:
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

new_click = """                try:
                    # Next.js блокирует get_by_role("tab"), поэтому используем evaluate для клика по кнопкам табов
                    await page.evaluate(f'''(tabName) => {{
                        // 1. Кликаем по кнопкам
                        document.querySelectorAll('[data-geist-tabs] button').forEach(b => {{
                            if (b.innerText.trim() === tabName) b.click();
                        }});
                        
                        // 2. Меняем скрытые селекты
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

with open("nextjs/parser.py", "w", encoding="utf-8") as f:
    f.write(text)

