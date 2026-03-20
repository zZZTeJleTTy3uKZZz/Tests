await page.goto('https://nextjs.org/docs/app/getting-started/layouts-and-pages');

// 1. Посмотрим, сколько select на странице и какие у них опции
const selects = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('select')).map(s => {
        return {
            classes: s.className,
            options: Array.from(s.options).map(o => o.value)
        }
    });
});
console.log('Selects:', JSON.stringify(selects, null, 2));

// 2. Посмотрим на кнопки табов
const tabs = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('[data-geist-tabs] button')).map(b => b.innerText);
});
console.log('Tabs:', tabs);
