import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={"width": 1280, "height": 720})
        page = await context.new_page()
        await page.goto("https://opencode.ai/docs/ru", wait_until="networkidle")
        nav = page.locator('nav[aria-label="Основное"]')
        links_data = await nav.evaluate("""nav => {
            const results = [];
            const seen = new Set();
            
            function walk(element, depth) {
                if (!element) return;
                
                // If it's a link
                if (element.tagName === 'A') {
                    const href = element.href.split('#')[0];
                    if (href.includes('/docs') && !seen.has(href)) {
                        seen.add(href);
                        results.push({
                            type: 'link',
                            href: href,
                            text: element.innerText.trim(),
                            depth: depth
                        });
                    }
                } 
                // If it's a group label
                else if (element.classList && element.classList.contains('group-label')) {
                    results.push({
                        type: 'group',
                        text: element.innerText.trim(),
                        depth: depth
                    });
                }
                
                // Recursively walk children
                const children = Array.from(element.children);
                for (const child of children) {
                    // Increase depth if we enter a new UL that isn't the top-level
                    let newDepth = depth;
                    if (child.tagName === 'UL' && !child.classList.contains('top-level')) {
                        newDepth++;
                    }
                    walk(child, newDepth);
                }
            }
            
            const rootUl = nav.querySelector('.sidebar-content ul.top-level');
            if (rootUl) {
                walk(rootUl, 0);
            }
            return results;
        }""")

        for l in links_data:
            indent = "  " * l["depth"]
            if l["type"] == "group":
                print(f"{indent}📁 {l['text']}")
            else:
                print(f"{indent}- {l['text']} ({l['href']})")
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
