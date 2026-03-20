import asyncio
import re
from bs4 import BeautifulSoup
import html2text
from playwright.async_api import async_playwright
import json

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.route("**/*.{png,jpg,jpeg,webp,gif,svg}", lambda r: r.abort())
        
        await page.goto('https://nextjs.org/docs/app/getting-started/project-structure', wait_until='domcontentloaded')
        await page.wait_for_selector('h1', timeout=30000)
        
        await page.wait_for_timeout(2000)
        
        # Test TS/JS tabs
        tab_names = await page.evaluate('''() => {
            const set = new Set();
            document.querySelectorAll('button[role=\"tab\"], [class*=\"tab\"] button, button[class*=\"tab\"]').forEach(b => {
                if(b.innerText.trim()) set.add(b.innerText.trim());
            });
            return Array.from(set);
        }''')
        
        print("Найдено вкладок:", tab_names)
        
        await browser.close()

asyncio.run(main())
