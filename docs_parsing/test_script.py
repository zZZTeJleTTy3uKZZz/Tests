with open('nextjs/parser.py', 'r', encoding='utf-8') as f:
    text = f.read()
    
old_code = """                    // Решение для табов кода (JavaScript / TypeScript / pnpm / npm и тд)
                    const tabGroups = Array.from(main.querySelectorAll('[data-geist-tabs]'));
                    
                    for (let i = 0; i < tabGroups.length; i++) {
                        const tabGroup = tabGroups[i];
                        let buttons = Array.from(tabGroup.querySelectorAll('button[role="tab"]'));
                        if (!buttons.length) buttons = Array.from(tabGroup.querySelectorAll('button'));
                        if (!buttons.length) continue;
                        
                        // Ищем родительский контейнер всего блока с кодом
                        const parentBlock = tabGroup.closest('[data-geist-code-block]') || tabGroup.closest('div[data-rehype-pretty-code-figure]') || tabGroup.parentElement.parentElement;
                        
                        if (!parentBlock) continue;
                        
                        let resHTML = '';
                        
                        for (let j = 0; j < buttons.length; j++) {
                            const btn = buttons[j];
                            const tabName = btn.innerText.trim();
                            if(!tabName) continue;
                            
                            btn.click();
                            await delay(150); // Ждем пока React подменит контент
                            
                            const pre = parentBlock.querySelector('pre');
                            if (pre) {
                                const lines = Array.from(pre.querySelectorAll('.line'));
                                let codeText = '';
                                if(lines.length > 0) {
                                    for(let k=0; k<lines.length; k++) {
                                        codeText += lines[k].innerText + String.fromCharCode(10);
                                    }
                                } else {
                                    codeText = pre.innerText;
                                }
                                
                                resHTML += '<br>MAGICSTART' + tabName + 'MAGICEND<pre><code>' + codeText.replace(/</g, '&lt;').replace(/>/g, '&gt;') + '</code></pre>';
                            }
                        }
                        
                        if (resHTML !== '') {
                            // ИСПОЛЬЗУЕМ outerHTML вместо replaceWith, потому что React в Next.js 
                            // может перехватить манипуляцию с DOM и откатить её назад.
                            parentBlock.outerHTML = '<div class="extracted-tabs-container">' + resHTML + '</div>';
                        }
                    }"""
                    
new_code = """                    // Собираем все блоки кода на странице
                    const blocks = Array.from(main.querySelectorAll('[data-geist-code-block], div[data-rehype-pretty-code-figure]'));
                    
                    for (let i = 0; i < blocks.length; i++) {
                        const block = blocks[i];
                        const tabGroup = block.querySelector('[data-geist-tabs]');
                        if (!tabGroup) continue;
                        
                        let buttons = Array.from(tabGroup.querySelectorAll('button[role="tab"]'));
                        if (!buttons.length) buttons = Array.from(tabGroup.querySelectorAll('button'));
                        if (!buttons.length) continue;
                        
                        let resHTML = '';
                        
                        for (let j = 0; j < buttons.length; j++) {
                            const btn = buttons[j];
                            const tabName = btn.innerText.trim();
                            if(!tabName) continue;
                            
                            btn.click();
                            await delay(150); // Ждем пока React подменит контент
                            
                            const pre = block.querySelector('pre');
                            if (pre) {
                                const lines = Array.from(pre.querySelectorAll('.line'));
                                let codeText = '';
                                if(lines.length > 0) {
                                    for(let k=0; k<lines.length; k++) {
                                        codeText += lines[k].innerText + String.fromCharCode(10);
                                    }
                                } else {
                                    codeText = pre.innerText;
                                }
                                
                                resHTML += '<br>MAGICSTART' + tabName + 'MAGICEND<pre><code>' + codeText.replace(/</g, '&lt;').replace(/>/g, '&gt;') + '</code></pre>';
                            }
                        }
                        
                        if (resHTML !== '') {
                            // ИСПОЛЬЗУЕМ insertBefore и потом скрываем, удалим в конце.
                            // Это обходит защиту React Virtual DOM от манипуляций.
                            const div = document.createElement('div');
                            div.className = 'extracted-tabs-container';
                            div.innerHTML = resHTML;
                            block.parentElement.insertBefore(div, block);
                            block.style.display = 'none';
                            block.className = 'do-not-parse';
                        }
                    }
                    
                    // Удаляем оригинальные блоки табов, которые мы скрыли
                    main.querySelectorAll('.do-not-parse').forEach(el => el.remove());"""
                    
text = text.replace(old_code, new_code)
with open('nextjs/parser.py', 'w', encoding='utf-8') as f:
    f.write(text)

