with open("nextjs/parser.py", "r", encoding="utf-8") as f:
    text = f.read()

# I see it! The problem is that the selector 'div[data-rehype-pretty-code-figure] select option'
# was too restrictive, so it found 0 tab_names for TS/JS, meaning the loop `for tab_name in tab_names`
# didn't even run for TypeScript!

text = text.replace("document.querySelectorAll('div[data-rehype-pretty-code-figure] select option').forEach", 
                    "document.querySelectorAll('select option').forEach")
text = text.replace("filter(b => b.querySelector('[data-geist-tabs]') || b.querySelector('select'))",
                    "filter(b => b.querySelector('[data-geist-tabs]') || b.querySelector('select') || b.parentElement.querySelector('select'))")

with open("nextjs/parser.py", "w", encoding="utf-8") as f:
    f.write(text)

