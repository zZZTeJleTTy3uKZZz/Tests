with open("nextjs/parser.py", "r", encoding="utf-8") as f:
    text = f.read()

# I see it! I need to use wait_until='networkidle' inside parse_page in parser.py, NOT domcontentloaded, 
# because Next.js loads the selectors dynamically via JS!

text = text.replace('await page.goto(url, wait_until="domcontentloaded", timeout=60000)', 'await page.goto(url, wait_until="networkidle", timeout=60000)')

with open("nextjs/parser.py", "w", encoding="utf-8") as f:
    f.write(text)

