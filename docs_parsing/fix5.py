with open('nextjs/parser.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the first evaluate call assignment
text = text.replace("            await page.evaluate(\"\"\"async () => {", "            main_html = await page.evaluate(\"\"\"async () => {")

# Find the end of the first evaluate block
idx = text.find("                    });\n                }\n            }\"\"\")")
if idx != -1:
    text = text[:idx] + "                    });\n                    return main.innerHTML;\n                }\n                return '';\n            }\"\"\")" + text[idx + len("                    });\n                }\n            }\"\"\")"):]

# Remove the second evaluate block
start_idx = text.find("            # Извлекаем HTML")
end_idx = text.find("            if not main_html:")
if start_idx != -1 and end_idx != -1:
    text = text[:start_idx] + text[end_idx:]

with open('nextjs/parser.py', 'w', encoding='utf-8') as f:
    f.write(text)
