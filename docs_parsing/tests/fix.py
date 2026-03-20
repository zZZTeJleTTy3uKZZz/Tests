with open("test_global_tabs.py", "r", encoding="utf-8") as f:
    text = f.read()

# Fix python escape character issue
text = text.replace("let codeText = lines.length > 0 ? lines.map(l => l.innerText).join('\\n') : pre.innerText;", "let codeText = ''; if (lines.length>0) { for(let z=0; z<lines.length; z++) codeText += lines[z].innerText + String.fromCharCode(10); } else { codeText = pre.innerText; }")

with open("test_global_tabs.py", "w", encoding="utf-8") as f:
    f.write(text)
