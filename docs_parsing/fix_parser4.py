with open("nextjs/parser.py", "r", encoding="utf-8") as f:
    text = f.read()

# Add a small wait before extracting tab names, maybe networkidle isn't enough if it's aborted

old_logic = """            await page.goto(url, wait_until="networkidle", timeout=60000)
            
            # Ждем H1 (на страницах Next.js всегда есть H1)
            await page.wait_for_selector('h1', timeout=30000)
            
            # Даем React время "ожить"
            await page.wait_for_timeout(1000)"""

new_logic = """            await page.goto(url, wait_until="networkidle", timeout=60000)
            
            # Ждем H1 (на страницах Next.js всегда есть H1)
            await page.wait_for_selector('h1', timeout=30000)
            
            # Даем React время "ожить"
            await page.wait_for_timeout(2000)
            
            # Ждем пока появятся табы или селекты (не обязательно, но полезно)
            try:
                await page.wait_for_selector('select, [data-geist-tabs]', timeout=3000)
            except:
                pass"""

text = text.replace(old_logic, new_logic)

with open("nextjs/parser.py", "w", encoding="utf-8") as f:
    f.write(text)

