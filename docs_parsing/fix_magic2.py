with open("nextjs/parser.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if 'markdown_text.replace("TAB_START ", "\n\n### [").replace(' in line:
        new_lines.append(line.replace('TAB_START ', 'MAGICSTART'))
    elif '" TAB_END", "]\n"' in line:
        new_lines.append(line.replace(' TAB_END', 'MAGICEND'))
    else:
        new_lines.append(line)

with open("nextjs/parser.py", "w", encoding="utf-8") as f:
    f.writelines(new_lines)

