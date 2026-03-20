import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36')
        page = await context.new_page()
        
        await page.goto('https://nextjs.org/docs/app/getting-started/layouts-and-pages', wait_until='networkidle')
        await page.wait_for_timeout(2000)
        
        script = "async () => { const delay = ms => new Promise(res => setTimeout(res, ms)); const blocks = Array.from(document.querySelectorAll('[data-rehype-pretty-code-figure]')); let res = 'Blocks: ' + blocks.length + ' '; for (let block of blocks) { const sel = block.parentElement.querySelector('select'); if (sel) { sel.value = 'TypeScript'; sel.dispatchEvent(new Event('change', { bubbles: true })); await delay(300); res += 'TS: ' + block.querySelector('pre').innerText.substring(0, 15) + ' '; sel.value = 'JavaScript'; sel.dispatchEvent(new Event('change', { bubbles: true })); await delay(300); res += 'JS: ' + block.querySelector('pre').innerText.substring(0, 15) + ' '; } } return res; }"
        
        val2 = await page.evaluate(script)
        print(val2)
        await browser.close()
asyncio.run(main())
