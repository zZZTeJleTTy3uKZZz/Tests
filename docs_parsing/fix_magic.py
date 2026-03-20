with open("nextjs/parser.py", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace('markdown_text.replace("TAB_START ", "\n\n### [").replace(\n                " TAB_END", "]\n"\n            )', 'markdown_text.replace("MAGICSTART", "\n\n### [").replace("MAGICEND", "]\n")')

with open("nextjs/parser.py", "w", encoding="utf-8") as f:
    f.write(text)
