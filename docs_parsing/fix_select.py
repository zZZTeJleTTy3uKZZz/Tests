with open("nextjs/parser.py", "r", encoding="utf-8") as f:
    text = f.read()

# I found the secret! Next.js does NOT use buttons for JS/TS switcher! 
# It uses an invisible <select> element mapped to the whole code block!
# 
# <select class="absolute inset-0 outline-hidden opacity-0 cursor-pointer bg-gray-100">
#   <option value="JavaScript">JavaScript</option>
#   <option value="TypeScript" selected="">TypeScript</option>
# </select>
# 
# To parse this, we must also query for `<select>` elements and dispatch "change" events!
