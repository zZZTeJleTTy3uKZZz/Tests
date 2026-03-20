import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36')
        page = await context.new_page()
        await page.goto('https://nextjs.org/docs/app/getting-started/layouts-and-pages', wait_until='networkidle')
        
        script2 = "async () => { const delay = ms => new Promise(res => setTimeout(res, ms)); const blocks = Array.from(document.querySelectorAll('[data-rehype-pretty-code-figure]')); let r = ''; if(blocks.length > 0) { const b = blocks[0]; const tsbtn = Array.from(document.querySelectorAll('button, a, div')).find(el => el.innerText && el.innerText.trim() === 'TypeScript'); if(tsbtn) { tsbtn.click(); await delay(300); const pre = b.querySelector('pre'); r += 'Clicked TS: ' + (pre ? pre.innerText.substring(0, 30) : 'no pre') + ' | '; } const jsbtn = Array.from(document.querySelectorAll('button, a, div')).find(el => el.innerText && el.innerText.trim() === 'JavaScript'); if(jsbtn) { jsbtn.click(); await delay(300); const pre = b.querySelector('pre'); r += 'Clicked JS: ' + (pre ? pre.innerText.substring(0, 30) : 'no pre') + ' | '; } } return r; }"
        val2 = await page.evaluate(script2)
        print('Blocks:', val2)
        
        await browser.close()
asyncio.run(main())
