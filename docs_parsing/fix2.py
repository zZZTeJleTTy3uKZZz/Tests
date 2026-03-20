import re

with open('nextjs/nextjs_docs_full.md', 'r', encoding='utf-8') as f:
    text = f.read()

# I see what's happening. On page 2, the tab extraction didn't work because
# the selector `[data-geist-tabs]` wasn't matching the correct code blocks or 
# they didn't have `button[role="tab"]`.
# The output on page 6 (Server components) worked flawlessly though! So the logic IS working!

# Let's check page 2 structure
