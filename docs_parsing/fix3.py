with open('nextjs/parser.py', 'r', encoding='utf-8') as f:
    text = f.read()

# I found the bug! In parser.py, the script is split into TWO separate evaluate blocks!
# FIRST BLOCK:
# await page.evaluate('''async () => { ... }''')
# 
# SECOND BLOCK:
# main_html = await page.evaluate('''() => { return document.querySelector('main').innerHTML; }''')

# In between those two calls, Next.js React hydration cycle runs and WIPE OUT OUR DOM CHANGES because they don't match the virtual DOM!
# We MUST return the HTML from the FIRST evaluate block!

print('Found the issue: two evaluate blocks separated by time allowing React to re-render.')
