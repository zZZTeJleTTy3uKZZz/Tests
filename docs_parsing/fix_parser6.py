with open("nextjs/parser.py", "r", encoding="utf-8") as f:
    text = f.read()

# Fix the bug where blocks array was empty due to missing elements 
# Next.js code block structure is dynamic! `div[data-rehype-pretty-code-figure]` gets replaced by `div[data-geist-code-block]` depending on render state!

text = text.replace(
    "const blocks = Array.from(document.querySelectorAll('[data-geist-code-block], div[data-rehype-pretty-code-figure]')).filter(b => b.querySelector('[data-geist-tabs]') || b.querySelector('select') || b.parentElement.querySelector('select'));",
    "const blocks = Array.from(document.querySelectorAll('[data-geist-code-block], div[data-rehype-pretty-code-figure], pre')).map(el => el.closest('[data-geist-code-block]') || el.closest('div[data-rehype-pretty-code-figure]') || el.parentElement).filter((b, i, arr) => b && arr.indexOf(b) === i).filter(b => b.querySelector('[data-geist-tabs]') || b.querySelector('select') || b.parentElement.querySelector('select'));"
)

text = text.replace(
    "const sel = block.querySelector('select');",
    "const sel = block.querySelector('select') || block.parentElement.querySelector('select');"
)


with open("nextjs/parser.py", "w", encoding="utf-8") as f:
    f.write(text)

