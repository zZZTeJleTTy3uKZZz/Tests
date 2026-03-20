with open('nextjs/parser.py', 'r', encoding='utf-8') as f:
    text = f.read()

old_code = """                        pre.innerHTML = '<code>' + codeText.replace(/</g, '&lt;').replace(/>/g, '&gt;') + '</code>';
                    });
                }
            }""")

            # Извлекаем HTML
            main_html = await page.evaluate(\"\"\"() => {
                const h1 = document.querySelector('h1');
                if (!h1) return '';
                const main = document.querySelector('article') || h1.parentElement;
                return main.innerHTML;
            }\"\"\")"""

new_code = """                        pre.innerHTML = '<code>' + codeText.replace(/</g, '&lt;').replace(/>/g, '&gt;') + '</code>';
                    });
                    return main.innerHTML;
                }
                return '';
            }""")

            main_html = await page.evaluate(\"\"\"() => {
                const h1 = document.querySelector('h1');
                if (!h1) return '';
                const main = document.querySelector('article') || h1.parentElement;
                return main.innerHTML;
            }\"\"\")"""
# Wait, no. I should just assign `main_html = await page.evaluate...` directly to the first evaluate and remove the second.
