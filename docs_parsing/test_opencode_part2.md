# Start the web server
    opencode web --port 4096
    
    
    # In another terminal, attach the TUI
    opencode attach http://localhost:4096
```

Это позволяет вам одновременно использовать веб-интерфейс и терминал, используя одни и те же сеансы и состояние.

* * *

## Конфигурационный файл

Вы также можете настроить параметры сервера в файле конфигурации `opencode.json`:
```
{
      "server": {
        "port": 4096,
        "hostname": "0.0.0.0",
        "mdns": true,
        "cors": ["https://example.com"]
      }
    }
```

CLI-флаги имеют приоритет над настройками файла конфигурации.

[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/web.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-11"></a>
---
url: https://opencode.ai/docs/ru/ide/
---

# IDE

Расширение opencode для VS Code, Cursor и других IDE.

opencode интегрируется с VS Code, Cursor или любой IDE, поддерживающей терминал. Просто запустите `opencode` в терминале, чтобы начать.

* * *

## Использование

  * **Быстрый запуск** : используйте `Cmd+Esc` (Mac) или `Ctrl+Esc` (Windows/Linux), чтобы открыть opencode в разделенном представлении терминала, или сфокусируйтесь на существующем сеансе терминала, если он уже запущен.
  * **Новый сеанс** : используйте `Cmd+Shift+Esc` (Mac) или `Ctrl+Shift+Esc` (Windows/Linux), чтобы начать новый сеанс терминала opencode, даже если он уже открыт. Вы также можете нажать кнопку opencode в пользовательском интерфейсе.
  * **Осведомленность о контексте** : автоматически делитесь своим текущим выбором или вкладкой с помощью opencode.
  * **Шорткаты ссылок на файлы** : Используйте `Cmd+Option+K` (Mac) или `Alt+Ctrl+K` (Linux/Windows) для вставки ссылок на файлы. Например, `@File#L37-42`.



* * *

## Установка

Чтобы установить opencode на VS Code и популярные форки, такие как Cursor, Windsurf, VSCodium:

  1. Откройте VS Code
  2. Откройте встроенный терминал
  3. Запустите `opencode` — расширение установится автоматически.



С другой стороны, если вы хотите использовать собственную IDE при запуске `/editor` или `/export` из TUI, вам необходимо установить `export EDITOR="code --wait"`. [Подробнее](/docs/tui/#editor-setup).

* * *

### Ручная установка

Найдите **opencode** в магазине расширений и нажмите **Установить**.

* * *

### Устранение неполадок

Если расширение не устанавливается автоматически:

  * Убедитесь, что вы используете `opencode` во встроенном терминале.
  * Убедитесь, что CLI для вашей IDE установлен: 
    * Для Code: команда `code`.
    * Для Cursor: команда `cursor`.
    * Для Windsurf: команда `windsurf`.
    * Для VSCodium: команда `codium`.
    * Если нет, запустите `Cmd+Shift+P` (Mac) или `Ctrl+Shift+P` (Windows/Linux) и найдите “Shell Command: Install ‘code’ command in PATH” (или эквивалент для вашей IDE).
  * Убедитесь, что у VS Code есть разрешение на установку расширений.



[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/ide.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-12"></a>
---
url: https://opencode.ai/docs/ru/zen/
---

# Zen

Подобранный список моделей, предоставленный OpenCode.

OpenCode Zen — это список протестированных и проверенных моделей, предоставленный командой OpenCode.

Заметка

OpenCode Zen в настоящее время находится в стадии бета-тестирования.

Zen работает как любой другой провайдер в OpenCode. Вы входите в OpenCode Zen и получаете ваш ключ API. Это **совершенно необязательно** , и вам не обязательно использовать его для использования OpenCode.

* * *

## Предыстория

Существует большое количество моделей, но лишь некоторые из них хорошо работают в качестве кодинг-агентов. Кроме того, большинство провайдеров настроены совсем по-другому; так что вы получите совсем другую производительность и качество.

Совет

Мы протестировали избранную группу моделей и поставщиков, которые хорошо работают с opencode.

Поэтому, если вы используете модель через что-то вроде OpenRouter, вы никогда не сможете уверен, что вы получаете лучшую версию модели, которую хотите.

Чтобы это исправить, мы сделали пару вещей:

  1. Мы протестировали избранную группу моделей и поговорили с их командами о том, как лучше всего запустить их.
  2. Затем мы поработали с несколькими поставщиками услуг, чтобы убедиться, что они обслуживаются правильно.
  3. Наконец, мы сравнили комбинацию модель/провайдер и составили список, который мы с удовольствием рекомендуем.



OpenCode Zen — это шлюз искусственного интеллекта, который дает вам доступ к этим моделям.

* * *

## Как это работает

OpenCode Zen работает так же, как и любой другой поставщик OpenCode.

  1. Вы входите в систему **[OpenCode Zen](https://opencode.ai/auth)** , добавляете платежные данные и копируете свой ключ API.
  2. Вы запускаете команду `/connect` в TUI, выбираете OpenCode Zen и вставляете свой ключ API.
  3. Запустите `/models` в TUI, чтобы просмотреть список рекомендуемых нами моделей.



С вас взимается плата за каждый запрос, и вы можете добавить кредиты на свой счет.

* * *

## Конечные точки

Вы также можете получить доступ к нашим моделям через следующие конечные точки API.

Модель| Идентификатор модели| Конечная точка| Пакет AI SDK  
---|---|---|---  
GPT 5.2| gpt-5.2| `https://opencode.ai/zen/v1/responses`| `@ai-sdk/openai`  
GPT 5.2 Codex| gpt-5.2-codex| `https://opencode.ai/zen/v1/responses`| `@ai-sdk/openai`  
GPT 5.1| gpt-5.1| `https://opencode.ai/zen/v1/responses`| `@ai-sdk/openai`  
GPT 5.1 Codex| gpt-5.1-codex| `https://opencode.ai/zen/v1/responses`| `@ai-sdk/openai`  
GPT 5.1 Codex Max| gpt-5.1-codex-max| `https://opencode.ai/zen/v1/responses`| `@ai-sdk/openai`  
GPT 5.1 Codex Mini| gpt-5.1-codex-mini| `https://opencode.ai/zen/v1/responses`| `@ai-sdk/openai`  
GPT 5| gpt-5| `https://opencode.ai/zen/v1/responses`| `@ai-sdk/openai`  
GPT 5 Codex| gpt-5-codex| `https://opencode.ai/zen/v1/responses`| `@ai-sdk/openai`  
GPT 5 Nano| gpt-5-nano| `https://opencode.ai/zen/v1/responses`| `@ai-sdk/openai`  
Claude Sonnet 4.5| claude-sonnet-4-5| `https://opencode.ai/zen/v1/messages`| `@ai-sdk/anthropic`  
Claude Sonnet 4| claude-sonnet-4| `https://opencode.ai/zen/v1/messages`| `@ai-sdk/anthropic`  
Claude Haiku 4.5| claude-haiku-4-5| `https://opencode.ai/zen/v1/messages`| `@ai-sdk/anthropic`  
Claude Haiku 3.5| claude-3-5-haiku| `https://opencode.ai/zen/v1/messages`| `@ai-sdk/anthropic`  
Claude Opus 4.6| claude-opus-4-6| `https://opencode.ai/zen/v1/messages`| `@ai-sdk/anthropic`  
Claude Opus 4.5| claude-opus-4-5| `https://opencode.ai/zen/v1/messages`| `@ai-sdk/anthropic`  
Claude Opus 4.1| claude-opus-4-1| `https://opencode.ai/zen/v1/messages`| `@ai-sdk/anthropic`  
Gemini 3 Pro| gemini-3-pro| `https://opencode.ai/zen/v1/models/gemini-3-pro`| `@ai-sdk/google`  
Gemini 3 Flash| gemini-3-flash| `https://opencode.ai/zen/v1/models/gemini-3-flash`| `@ai-sdk/google`  
MiniMax M2.5| minimax-m2.5| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
MiniMax M2.5 Free| minimax-m2.5-free| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
MiniMax M2.1| minimax-m2.1| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
GLM 5| glm-5| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
GLM 4.7| glm-4.7| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
GLM 4.7 Free| glm-4.7-free| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
GLM 4.6| glm-4.6| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
Kimi K2.5| kimi-k2.5| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
Kimi K2.5 Free| kimi-k2.5-free| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
Kimi K2 Thinking| kimi-k2-thinking| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
Kimi K2| kimi-k2| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
Qwen3 Coder 480B| qwen3-coder| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
Big Pickle| big-pickle| `https://opencode.ai/zen/v1/chat/completions`| `@ai-sdk/openai-compatible`  
  
[модель id](/docs/config/#models) в вашей конфигурации opencode использует формат `opencode/<model-id>`. Например, для Кодекса GPT 5.2 вы должны используйте `opencode/gpt-5.2-codex` в вашей конфигурации.

* * *

### Модели

Полный список доступных моделей и их метаданные можно получить по адресу:
```
https://opencode.ai/zen/v1/models
```

* * *

## Цены

Мы поддерживаем модель оплаты по мере использования. Ниже приведены цены **за 1 миллион токенов**.

Модель| Вход| Выход| Кэшированное чтение| Кэшированная запись  
---|---|---|---|---  
Big Pickle| Бесплатно| Бесплатно| Бесплатно| -  
MiniMax M2.5 Free| Бесплатно| Бесплатно| Бесплатно| -  
MiniMax M2.5| $0.30| $1.20| $0.06| -  
MiniMax M2.1| $0.30| $1.20| $0.10| -  
GLM 5| $1.00| $3.20| $0.20| -  
GLM 4.7| $0.60| $2.20| $0.10| -  
GLM 4.7| $0.60| $2.20| $0.10| -  
GLM 4.6| $0.60| $2.20| $0.10| -  
GLM 4.7 Free| Бесплатно| Бесплатно| Бесплатно| -  
Kimi K2.5 Free| Бесплатно| Бесплатно| Бесплатно| -  
Kimi K2.5| $0.60| $3.00| $0.08| -  
Kimi K2 Thinking| $0.40| $2.50| -| -  
Kimi K2| $0.40| $2.50| -| -  
Qwen3 Coder 480B| $0.45| $1.50| -| -  
Claude Sonnet 4.5 (≤ 200 тыс. токенов)| $3.00| $15.00| $0.30| $3.75  
Claude Sonnet 4.5 (> 200 тыс. токенов)| $6.00| $22.50| $0.60| $7.50  
Claude Sonnet 4 (≤ 200 тыс. токенов)| $3.00| $15.00| $0.30| $3.75  
Claude Sonnet 4 (> 200 тыс. токенов)| $6.00| $22.50| $0.60| $7.50  
Claude Haiku 4.5| $1.00| $5.00| $0.10| $1.25  
Claude Haiku 3.5| $0.80| $4.00| $0.08| $1.00  
Claude Opus 4.6 (≤ 200 тыс. токенов)| $5.00| $25.00| $0.50| $6.25  
Claude Opus 4.6 (> 200 тыс. токенов)| $10.00| $37.50| $1.00| $12.50  
Claude Opus 4.5| $5.00| $25.00| $0.50| $6.25  
Claude Opus 4.1| $15.00| $75.00| $1.50| $18.75  
Gemini 3 Pro (≤ 200 тыс. токенов)| $2.00| $12.00| $0.20| -  
Gemini 3 Pro (> 200 тыс. токенов)| $4.00| $18.00| $0.40| -  
Gemini 3 Flash| $0.50| $3.00| $0.05| -  
GPT 5.2| $1.75| $14.00| $0.175| -  
GPT 5.2 Codex| $1.75| $14.00| $0.175| -  
GPT 5.1| $1.07| $8.50| $0.107| -  
GPT 5.1 Codex| $1.07| $8.50| $0.107| -  
GPT 5.1 Codex Max| $1.25| $10.00| $0.125| -  
GPT 5.1 Codex Mini| $0.25| $2.00| $0.025| -  
GPT 5| $1.07| $8.50| $0.107| -  
GPT 5 Codex| $1.07| $8.50| $0.107| -  
GPT 5 Nano| Бесплатно| Бесплатно| Бесплатно| -  
  
Вы можете заметить _Claude Haiku 3.5_ в своей истории использования. Это [недорогая модель](/docs/config/#models), которая используется для создания заголовков ваших сеансов.

Заметка

Комиссии по кредитной карте учитываются по себестоимости (4,4% + 0,30 доллара США за транзакцию); мы не взимаем ничего сверх этого.

Бесплатные модели:

  * Kimi K2.5 Free доступен на OpenCode в течение ограниченного времени. Команда использует это время для сбора отзывов и улучшения модели.
  * MiniMax M2.5 Free доступен на OpenCode в течение ограниченного времени. Команда использует это время для сбора отзывов и улучшения модели.
  * Big Pickle — это стелс-модель, которая доступна бесплатно на OpenCode в течение ограниченного времени. Команда использует это время для сбора отзывов и улучшения модели.



[Свяжитесь с нами](mailto:contact@anoma.ly), если у вас есть вопросы.

* * *

### Автопополнение

Если ваш баланс упадет ниже 5 долларов, Zen автоматически пополнит 20 долларов.

Вы можете изменить сумму автопополнения. Вы также можете полностью отключить автопополнение.

* * *

### Ежемесячные лимиты

Вы также можете установить месячный лимит использования для всего рабочего пространства и для каждого член вашей команды.

Например, предположим, что вы установили ежемесячный лимит использования в размере 20 долларов США, Zen не будет использовать более 20 долларов в месяц. Но если у вас включено автопополнение, Zen может взимать с вас более 20 долларов США, если ваш баланс опускается ниже 5 долларов США.

* * *

## Конфиденциальность

Все наши модели размещены в США. Наши поставщики придерживаются политики нулевого хранения и не используют ваши данные для обучения моделей, за следующими исключениями:

  * Big Pickle: во время бесплатного периода собранные данные могут быть использованы для улучшения модели.
  * Kimi K2.5 Free: в течение бесплатного периода собранные данные могут использоваться для улучшения модели.
  * MiniMax M2.5 Free: в течение бесплатного периода собранные данные могут использоваться для улучшения модели.
  * API OpenAI: запросы хранятся в течение 30 дней в соответствии с [Политикой данных OpenAI](https://platform.openai.com/docs/guides/your-data).
  * API-интерфейсы Anthropic: запросы хранятся в течение 30 дней в соответствии с [Политикой данных Anthropic](https://docs.anthropic.com/en/docs/claude-code/data-usage).



* * *

## Для команд

Zen также отлично подходит для команд. Вы можете приглашать товарищей по команде, назначать роли, выбирать модели, которые использует ваша команда, и многое другое.

Заметка

Рабочие пространства в настоящее время бесплатны для команд в рамках бета-тестирования.

Управление вашим рабочим пространством в настоящее время бесплатно для команд в рамках бета-тестирования. Мы вскоре поделимся более подробной информацией о ценах.

* * *

### Роли

Вы можете приглашать товарищей по команде в свое рабочее пространство и распределять роли:

  * **Администратор** : управляйте моделями, участниками, ключами API и выставлением счетов.
  * **Участник** : Управляйте только своими собственными ключами API.



Администраторы также могут установить ежемесячные лимиты расходов для каждого участника, чтобы держать расходы под контролем.

* * *

### Доступ к модели

Администраторы могут включать или отключать определенные модели для рабочей области. Запросы, сделанные к отключенной модели, вернут ошибку.

Это полезно в случаях, когда вы хотите отключить использование модели, которая собирает данные.

* * *

### Использование собственных API-ключей

Вы можете использовать свои собственные ключи API OpenAI или Anthropic, сохраняя при этом доступ к другим моделям в Zen.

Когда вы используете свои собственные ключи, счета за токены взимаются непосредственно провайдером, а не Zen.

Например, у вашей организации уже может быть ключ для OpenAI или Anthropic. и вы хотите использовать его вместо того, который предоставляет Zen.

* * *

## Цели

Мы создали OpenCode Zen, чтобы:

  1. **Сравнить** лучшие модели/поставщики кодинг-агентов.
  2. Получить доступ к вариантам **наивысшего качества** , не снижая производительность и не обращаясь к более дешевым поставщикам.
  3. Передавать **снижение цен** , продавая по себестоимости; поэтому единственная наценка предназначена для покрытия наших комиссий за обработку.
  4. Исключить **привязку** , позволяя использовать его с любым другим кодинг-агентом. И всегда позволяя вам использовать любого другого провайдера с OpenCode.



[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/zen.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-13"></a>
---
url: https://opencode.ai/docs/ru/share/
---

# Делиться

Поделитесь своими разговорами об opencode.

Функция общего доступа opencode позволяет вам создавать общедоступные ссылки на ваши беседы opencode, чтобы вы могли сотрудничать с товарищами по команде или получать помощь от других.

Заметка

Общие беседы общедоступны для всех, у кого есть ссылка.

* * *

## Как это работает

Когда вы делитесь беседой, opencode:

  1. Создает уникальный общедоступный URL-адрес для вашего сеанса.
  2. Синхронизирует историю ваших разговоров с нашими серверами
  3. Делает беседу доступной по общей ссылке — `opncd.ai/s/<share-id>`.



* * *

## Совместное использование

opencode поддерживает три режима общего доступа, которые контролируют общий доступ к разговорам:

* * *

### Ручной (по умолчанию)

По умолчанию opencode использует режим совместного использования вручную. Сессии не передаются автоматически, но вы можете поделиться ими вручную с помощью команды `/share`:
```
/share
```

Это создаст уникальный URL-адрес, который будет скопирован в буфер обмена.

Чтобы явно установить ручной режим в вашем [файле конфигурации](/docs/config):

opencode.json
```
{
      "$schema": "https://opncd.ai/config.json",
      "share": "manual"
    }
```

* * *

### Автоматическая публикация

Вы можете включить автоматический общий доступ для всех новых разговоров, установив для параметра `share` значение `"auto"` в вашем [файле конфигурации](/docs/config):

opencode.json
```
{
      "$schema": "https://opncd.ai/config.json",
      "share": "auto"
    }
```

Если функция автоматического обмена включена, каждый новый разговор будет автоматически опубликован и будет создана ссылка.

* * *

### Отключено

Вы можете полностью отключить общий доступ, установив для параметра `share` значение `"disabled"` в вашем [файле конфигурации](/docs/config):

opencode.json
```
{
      "$schema": "https://opncd.ai/config.json",
      "share": "disabled"
    }
```

Чтобы обеспечить соблюдение этого правила для всей вашей команды в конкретном проекте, добавьте его в `opencode.json` вашего проекта и зарегистрируйтесь в Git.

* * *

## Отменить совместное использование

Чтобы прекратить делиться беседой и удалить ее из общего доступа:
```
/unshare
```

Это приведет к удалению ссылки общего доступа и удалению данных, связанных с разговором.

* * *

## Конфиденциальность

Есть несколько вещей, которые следует учитывать при общении.

* * *

### Хранение данных

Общие разговоры остаются доступными до тех пор, пока вы явно не отмените общий доступ к ним. Этот включает в себя:

  * Полная история разговоров
  * Все сообщения и ответы
  * Метаданные сеанса



* * *

### Рекомендации

  * Делитесь только разговорами, которые не содержат конфиденциальной информации.
  * Прежде чем поделиться, просмотрите содержимое разговора.
  * Отмените общий доступ к разговорам после завершения сотрудничества.
  * Избегайте обмена разговорами с проприетарным кодом или конфиденциальными данными.
  * Для конфиденциальных проектов полностью отключите общий доступ.



* * *

## Для предприятий

Для корпоративных развертываний функция общего доступа может быть:

  * **Отключено** полностью из соображений безопасности.
  * **Доступно только** для пользователей, прошедших аутентификацию посредством единого входа.
  * **Автономное размещение** в вашей собственной инфраструктуре



[Узнайте больше](/docs/enterprise) об использовании opencode в вашей организации.

[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/share.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-14"></a>
---
url: https://opencode.ai/docs/ru/github/
---

# GitHub

Используйте opencode в задачах и пул-реквестах GitHub.

opencode интегрируется с вашим рабочим процессом GitHub. Упомяните `/opencode` или `/oc` в своем комментарии, и opencode выполнит задачи в вашем средстве выполнения действий GitHub.

* * *

## Возможности

  * **Триаж задач (Issue Triage)**. Попросите opencode разобраться в проблеме и объяснить ее вам.
  * **Исправление и реализация**. Попросите opencode исправить проблему или реализовать функцию. Он будет работать в новой ветке и создаст PR со всеми изменениями.
  * **Безопасность** : opencode запускается внутри ваших GitHub Runners.



* * *

## Установка

Запустите следующую команду в проекте, который находится в репозитории GitHub:

Окно терминала
```
opencode github install
```

Это поможет вам установить приложение GitHub, создать рабочий процесс и настроить secrets (секреты).

* * *

### Ручная настройка

Или вы можете настроить его вручную.

  1. **Установите приложение GitHub**

Перейдите на [**github.com/apps/opencode-agent**](https://github.com/apps/opencode-agent). Убедитесь, что он установлен в целевом репозитории.

  2. **Добавьте рабочий процесс**

Добавьте следующий файл рабочего процесса в `.github/workflows/opencode.yml` в своем репозитории. Обязательно установите соответствующий `model` и необходимые ключи API в `env`.

.github/workflows/opencode.yml
```
name: opencode
         
         
         on:
           issue_comment:
             types: [created]
           pull_request_review_comment:
             types: [created]
         
         
         jobs:
           opencode:
             if: |
               contains(github.event.comment.body, '/oc') ||
               contains(github.event.comment.body, '/opencode')
             runs-on: ubuntu-latest
             permissions:
               id-token: write
             steps:
                - name: Checkout repository
                  uses: actions/checkout@v6
                  with:
                    fetch-depth: 1
                    persist-credentials: false
         
         
                - name: Run OpenCode
                 uses: anomalyco/opencode/github@latest
                 env:
                   ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
                 with:
                   model: anthropic/claude-sonnet-4-20250514
                   # share: true
                   # github_token: xxxx
```

  3. **Храните ключи API в секрете**

В **настройках** вашей организации или проекта разверните **Секреты и переменные** слева и выберите **Действия**. И добавьте необходимые ключи API.




* * *

## Настройка

  * `model`: модель для использования с opencode. Принимает формат `provider/model`. Это **обязательно**.

  * `agent`: используемый агент. Должен быть основным агентом. Возвращается к `default_agent` из конфигурации или к `"build"`, если не найден.

  * `share`: следует ли предоставлять общий доступ к сеансу opencode. По умолчанию **true** для общедоступных репозиториев.

  * `prompt`: дополнительный настраиваемый запрос для переопределения поведения по умолчанию. Используйте это, чтобы настроить обработку запросов opencode.

  * `token`: дополнительный токен доступа GitHub для выполнения таких операций, как создание комментариев, фиксация изменений и открытие запросов на включение. По умолчанию opencode использует токен доступа к установке из приложения opencode GitHub, поэтому фиксации, комментарии и запросы на включение отображаются как исходящие из приложения.

Кроме того, вы можете использовать [встроенный `GITHUB_TOKEN`](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token) средства запуска действий GitHub без установки приложения opencode GitHub. Просто не забудьте предоставить необходимые разрешения в вашем рабочем процессе:
```
permissions:
          id-token: write
          contents: write
          pull-requests: write
          issues: write
```

Вы также можете использовать [токены личного доступа](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)(PAT), если предпочитаете.




* * *

## Поддерживаемые события

opencode может быть запущен следующими событиями GitHub:

Тип события| Инициировано| Подробности  
---|---|---  
`issue_comment`| Комментарий к проблеме или PR| Упомяните `/opencode` или `/oc` в своем комментарии. opencode считывает контекст и может создавать ветки, открывать PR или отвечать.  
`pull_request_review_comment`| Комментируйте конкретные строки кода в PR.| Упоминайте `/opencode` или `/oc` при просмотре кода. opencode получает путь к файлу, номера строк и контекст сравнения.  
`issues`| Issue открыт или изменен| Автоматически запускать opencode при создании или изменении проблем. Требуется ввод `prompt`.  
`pull_request`| PR открыт или обновлен| Автоматически запускать opencode при открытии, синхронизации или повторном открытии PR. Полезно для автоматических обзоров.  
`schedule`| Расписание на основе Cron| Запускайте opencode по расписанию. Требуется ввод `prompt`. Вывод поступает в журналы и PR (комментариев нет).  
`workflow_dispatch`| Ручной триггер из пользовательского интерфейса GitHub| Запускайте opencode по требованию на вкладке «Действия». Требуется ввод `prompt`. Вывод идет в логи и PR.  
  
### Пример: Расписание

Запускайте opencode по расписанию для выполнения автоматизированных задач:

.github/workflows/opencode-scheduled.yml
```
name: Scheduled OpenCode Task
    
    
    on:
      schedule:
        - cron: "0 9 * * 1" # Every Monday at 9am UTC
    
    
    jobs:
      opencode:
        runs-on: ubuntu-latest
        permissions:
          id-token: write
          contents: write
          pull-requests: write
          issues: write
        steps:
          - name: Checkout repository
            uses: actions/checkout@v6
            with:
              persist-credentials: false
    
    
          - name: Run OpenCode
            uses: anomalyco/opencode/github@latest
            env:
              ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
            with:
              model: anthropic/claude-sonnet-4-20250514
              prompt: |
                Review the codebase for any TODO comments and create a summary.
                If you find issues worth addressing, open an issue to track them.
```

Для запланированных событий вход `prompt` **обязателен** , поскольку нет комментария, из которого можно было бы извлечь инструкции. Запланированные рабочие процессы выполняются без пользовательского контекста для проверки разрешений, поэтому рабочий процесс должен предоставлять `contents: write` и `pull-requests: write`, если вы ожидаете, что opencode будет создавать ветки или PR.

* * *

### Пример: Pull Request

Автоматически просматривать PR при их открытии или обновлении:

.github/workflows/opencode-review.yml
```
name: opencode-review
    
    
    on:
      pull_request:
        types: [opened, synchronize, reopened, ready_for_review]
    
    
    jobs:
      review:
        runs-on: ubuntu-latest
        permissions:
          id-token: write
          contents: read
          pull-requests: read
          issues: read
        steps:
          - uses: actions/checkout@v6
            with:
              persist-credentials: false
          - uses: anomalyco/opencode/github@latest
            env:
              ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
              GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            with:
              model: anthropic/claude-sonnet-4-20250514
              use_github_token: true
              prompt: |
                Review this pull request:
                - Check for code quality issues
                - Look for potential bugs
                - Suggest improvements
```

Если для событий `pull_request` не указан `prompt`, opencode по умолчанию проверяет запрос на включение.

* * *

### Пример: Сортировка Issue

Автоматически сортируйте новые проблемы. В этом примере фильтруется аккаунты, созданные более 30 дней назад, чтобы уменьшить количество спама:

.github/workflows/opencode-triage.yml
```
name: Issue Triage
    
    
    on:
      issues:
        types: [opened]
    
    
    jobs:
      triage:
        runs-on: ubuntu-latest
        permissions:
          id-token: write
          contents: write
          pull-requests: write
          issues: write
        steps:
          - name: Check account age
            id: check
            uses: actions/github-script@v7
            with:
              script: |
                const user = await github.rest.users.getByUsername({
                  username: context.payload.issue.user.login
                });
                const created = new Date(user.data.created_at);
                const days = (Date.now() - created) / (1000 * 60 * 60 * 24);
                return days >= 30;
              result-encoding: string
    
    
          - uses: actions/checkout@v6
            if: steps.check.outputs.result == 'true'
            with:
              persist-credentials: false
    
    
          - uses: anomalyco/opencode/github@latest
            if: steps.check.outputs.result == 'true'
            env:
              ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
            with:
              model: anthropic/claude-sonnet-4-20250514
              prompt: |
                Review this issue. If there's a clear fix or relevant docs:
                - Provide documentation links
                - Add error handling guidance for code examples
                Otherwise, do not comment.
```

Для событий `issues` вход `prompt` **обязателен** , поскольку нет комментария, из которого можно было бы извлечь инструкции.

* * *

## Пользовательские промпты

Переопределите приглашение по умолчанию, чтобы настроить поведение opencode для вашего рабочего процесса.

.github/workflows/opencode.yml
```
- uses: anomalyco/opencode/github@latest
      with:
        model: anthropic/claude-sonnet-4-5
        prompt: |
          Review this pull request:
          - Check for code quality issues
          - Look for potential bugs
          - Suggest improvements
```

Это полезно для обеспечения соблюдения конкретных критериев проверки, стандартов кодирования или приоритетных областей, имеющих отношение к вашему проекту.

* * *

## Примеры

Вот несколько примеров того, как вы можете использовать opencode в GitHub.

  * **Объяснение проблемы**

Добавьте этот комментарий в выпуск GitHub.
```
/opencode explain this issue
```

opencode прочитает всю ветку, включая все комментарии, и ответит с четким объяснением.

  * **Исправление проблемы**

В выпуске GitHub скажите:
```
/opencode fix this
```

А opencode создаст новую ветку, внедрит изменения и откроет PR с изменениями.

  * **Проверка Pull Request и внесение изменений**

Оставьте следующий комментарий к PR на GitHub.
```
Delete the attachment from S3 when the note is removed /oc
```

opencode внедрит запрошенное изменение и зафиксирует его в том же PR.

  * **Проверка отдельных строк кода**

Оставляйте комментарии непосредственно к строкам кода на вкладке «Файлы» PR. opencode автоматически определяет файл, номера строк и контекст различий, чтобы предоставить точные ответы.
```
[Comment on specific lines in Files tab]
        /oc add error handling here
```

При комментировании определенных строк opencode получает:

    * Точный файл, который просматривается
    * Конкретные строки кода
    * Окружающий контекст различий
    * Информация о номере строки

Это позволяет выполнять более целевые запросы без необходимости вручную указывать пути к файлам или номера строк.




[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/github.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-15"></a>
---
url: https://opencode.ai/docs/ru/gitlab/
---

# GitLab

Используйте opencode в задачах GitLab и мерж-реквестах.

opencode интегрируется с вашим рабочим процессом GitLab через конвейер GitLab CI/CD или с GitLab Duo.

В обоих случаях opencode будет работать на ваших программах GitLab.

* * *

## GitLab

opencode работает в обычном конвейере GitLab. Вы можете встроить его в конвейер как [CI-компонент](https://docs.gitlab.com/ee/ci/components/)

Здесь мы используем созданный сообществом компонент CI/CD для opencode — [nagyv/gitlab-opencode](https://gitlab.com/nagyv/gitlab-opencode).

* * *

### Функции

  * **Использовать пользовательскую конфигурацию для каждого задания**. Настройте opencode с помощью пользовательского каталога конфигурации, например `./config/#custom-directory`, чтобы включать или отключать функциональность для каждого вызова opencode.
  * **Минимальная настройка** : компонент CI настраивает opencode в фоновом режиме, вам нужно только создать конфигурацию opencode и начальное приглашение.
  * **Гибкость** : компонент CI поддерживает несколько входных данных для настройки его поведения.



* * *

### Настройка

  1. Сохраните JSON аутентификации opencode как переменные среды CI типа файла в разделе **Настройки** > **CI/CD** > **Переменные**. Обязательно пометьте их как «Замаскированные и скрытые».

  2. Добавьте следующее в файл `.gitlab-ci.yml`.

.gitlab-ci.yml
```
include:
           - component: $CI_SERVER_FQDN/nagyv/gitlab-opencode/opencode@2
             inputs:
               config_dir: ${CI_PROJECT_DIR}/opencode-config
               auth_json: $OPENCODE_AUTH_JSON # The variable name for your OpenCode authentication JSON
               command: optional-custom-command
               message: "Your prompt here"
```




Дополнительные сведения и варианты использования см. в документации ](<https://gitlab.com/explore/catalog/nagyv/gitlab-opencode>) для этого компонента.

* * *

## GitLab Duo

opencode интегрируется с вашим рабочим процессом GitLab. Упомяните `@opencode` в комментарии, и opencode выполнит задачи в вашем конвейере GitLab CI.

* * *

### Функции

  * **Триаж задач (Issue Triage)**. Попросите opencode разобраться в проблеме и объяснить ее вам.
  * **Исправление и реализация**. Попросите opencode исправить проблему или реализовать функцию. Он создаст новую ветку и создаст мерж-реквест с изменениями.
  * **Безопасность** : opencode работает на ваших программах GitLab.



* * *

### Настройка

opencode работает в вашем конвейере GitLab CI/CD. Вот что вам понадобится для его настройки:

Совет

Ознакомьтесь с [**документацией GitLab**](https://docs.gitlab.com/user/duo_agent_platform/agent_assistant/) для получения актуальных инструкций.

  1. Настройте свою среду GitLab

  2. Настройка CI/CD

  3. Получите ключ API поставщика моделей ИИ

  4. Создать учетную запись службы

  5. Настройка переменных CI/CD

  6. Создайте файл конфигурации потока, вот пример:

Конфигурация потока
[/code]
```
Подробные инструкции можно найти в [GitLab CLI agents docs](https://docs.gitlab.com/user/duo_agent_platform/agent_assistant/).

* * *

### Примеры

Вот несколько примеров того, как вы можете использовать opencode в GitLab.

Совет

Вы можете настроить использование триггерной фразы, отличной от `@opencode`.

  * **Объяснение проблемы**

Добавьте этот комментарий в issue GitLab.
[code] @opencode explain this issue
```

opencode прочитает проблему и ответит с четким объяснением.

  * **Исправление проблемы**

В issue GitLab напишите:
```
@opencode fix this
```

opencode создаст новую ветку, внедрит изменения и откроет мерж-реквест с изменениями.

  * **Проверка Merge Request**

Оставьте следующий комментарий к мерж-реквесту GitLab.
```
@opencode review this merge request
```

opencode рассмотрит мерж-реквест и предоставит отзыв.




[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/gitlab.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-16"></a>
---
url: https://opencode.ai/docs/ru/tools/
---

# Инструменты

Управляйте инструментами, которые может использовать LLM.

Инструменты позволяют LLM выполнять действия в вашей кодовой базе. opencode поставляется с набором встроенных инструментов, но вы можете расширить его с помощью [пользовательских инструментов](/docs/custom-tools) или [MCP-серверов](/docs/mcp-servers).

По умолчанию все инструменты **включены** и не требуют разрешения для запуска. Вы можете контролировать поведение инструмента через [permissions](/docs/permissions).

* * *

## Настройка

Используйте поле `permission` для управления поведением инструмента. Вы можете разрешить, запретить или потребовать одобрения для каждого инструмента.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "permission": {
        "edit": "deny",
        "bash": "ask",
        "webfetch": "allow"
      }
    }
```

Вы также можете использовать подстановочные знаки для одновременного управления несколькими инструментами. Например, чтобы потребовать одобрения всех инструментов с сервера MCP:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "permission": {
        "mymcp_*": "ask"
      }
    }
```

[Подробнее](/docs/permissions) о настройке разрешений.

* * *

## Встроенный

Вот все встроенные инструменты, доступные в opencode.

* * *

### bash

Выполняйте shell-команды в среде вашего проекта.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "permission": {
        "bash": "allow"
      }
    }
```

Этот инструмент позволяет LLM запускать команды терминала, такие как `npm install`, `git status` или любую другую shell-команду.

* * *

### edit

Измените существующие файлы, используя точную замену строк.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "permission": {
        "edit": "allow"
      }
    }
```

Этот инструмент выполняет точное редактирование файлов, заменяя точные совпадения текста. Это основной способ изменения кода в LLM.

* * *

### write

Создавайте новые файлы или перезаписывайте существующие.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "permission": {
        "edit": "allow"
      }
    }
```

Используйте это, чтобы позволить LLM создавать новые файлы. Он перезапишет существующие файлы, если они уже существуют.

Заметка

Инструмент `write` контролируется разрешением `edit`, которое распространяется на все модификации файлов (`edit`, `write`, `patch`, `multiedit`).

* * *

### read

Прочитайте содержимое файла из вашей кодовой базы.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "permission": {
        "read": "allow"
      }
    }
```

Этот инструмент читает файлы и возвращает их содержимое. Он поддерживает чтение определенных диапазонов строк для больших файлов.

* * *

### grep

Поиск содержимого файла с помощью регулярных выражений.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "permission": {
        "grep": "allow"
      }
    }
```

Быстрый поиск контента по вашей кодовой базе. Поддерживает полный синтаксис регулярных выражений и фильтрацию шаблонов файлов.

* * *

### glob

Найдите файлы по шаблону.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "permission": {
        "glob": "allow"
      }
    }
```

Ищите файлы, используя шаблоны glob, например `**/*.js` или `src/**/*.ts`. Возвращает соответствующие пути к файлам, отсортированные по времени изменения.

* * *

### list

Список файлов и каталогов по заданному пути.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "permission": {
        "list": "allow"
      }
    }
```

Этот инструмент отображает содержимое каталога. Он принимает шаблоны glob для фильтрации результатов.

* * *

### lsp (экспериментальный)

Взаимодействуйте с настроенными серверами LSP, чтобы получить функции анализа кода, такие как определения, ссылки, информация о наведении и иерархия вызовов.

Заметка

Этот инструмент доступен только при `OPENCODE_EXPERIMENTAL_LSP_TOOL=true` (или `OPENCODE_EXPERIMENTAL=true`).

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "permission": {
        "lsp": "allow"
      }
    }
```

Поддерживаемые операции включают `goToDefinition`, `findReferences`, `hover`, `documentSymbol`, `workspaceSymbol`, `goToImplementation`, `prepareCallHierarchy`, `incomingCalls` и `outgoingCalls`.

Чтобы настроить серверы LSP, доступные для вашего проекта, см. [LSP Servers](/docs/lsp).

* * *

### patch

Применяйте патчи к файлам.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "permission": {
        "edit": "allow"
      }
    }
```

Этот инструмент применяет файлы исправлений к вашей кодовой базе. Полезно для применения различий и патчей из различных источников.

Заметка

Инструмент `patch` контролируется разрешением `edit`, которое распространяется на все модификации файлов (`edit`, `write`, `patch`, `multiedit`).

* * *

### skill

Загрузите [skill](/docs/skills) (файл `SKILL.md`) и верните его содержимое в диалог.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "permission": {
        "skill": "allow"
      }
    }
```

* * *

### todowrite

Управляйте списками дел во время сеансов кодирования.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "permission": {
        "todowrite": "allow"
      }
    }
```

Создает и обновляет списки задач для отслеживания прогресса во время сложных операций. LLM использует это для организации многоэтапных задач.

Заметка

По умолчанию этот инструмент отключен для субагентов, но вы можете включить его вручную. [Подробнее](/docs/agents/#permissions)

* * *

### todoread

Прочтите существующие списки дел.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "permission": {
        "todoread": "allow"
      }
    }
```

Считывает текущее состояние списка дел. Используется LLM для отслеживания задач, ожидающих или завершенных.

Заметка

По умолчанию этот инструмент отключен для субагентов, но вы можете включить его вручную. [Подробнее](/docs/agents/#permissions)

* * *

### webfetch

Получить веб-контент.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "permission": {
        "webfetch": "allow"
      }
    }
```

Позволяет LLM получать и читать веб-страницы. Полезно для поиска документации или исследования онлайн-ресурсов.

* * *

### websearch

Найдите информацию в Интернете.

Заметка

Этот инструмент доступен только при использовании поставщика opencode или когда для переменной среды `OPENCODE_ENABLE_EXA` установлено любое истинное значение (например, `true` или `1`).

Чтобы включить при запуске opencode:

Окно терминала
```
OPENCODE_ENABLE_EXA=1 opencode
```

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "permission": {
        "websearch": "allow"
      }
    }
```

Выполняет поиск в Интернете с помощью Exa AI для поиска соответствующей информации в Интернете. Полезно для исследования тем, поиска текущих событий или сбора информации, выходящей за рамки данных обучения.

Ключ API не требуется — инструмент подключается напрямую к сервису MCP, размещенному на Exa AI, без аутентификации.

Совет

Используйте `websearch`, когда вам нужно найти информацию (обнаружение), и `webfetch`, когда вам нужно получить контент с определенного URL-адреса (извлечение).

* * *

### question

Задавайте вопросы пользователю во время выполнения.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "permission": {
        "question": "allow"
      }
    }
```

Этот инструмент позволяет LLM задавать вопросы пользователю во время выполнения задачи. Это полезно для:

  * Сбор предпочтений или требований пользователей
  * Уточнение двусмысленных инструкций
  * Получение решений по вариантам реализации
  * Предлагая выбор, в каком направлении двигаться



Каждый вопрос включает заголовок, текст вопроса и список вариантов. Пользователи могут выбрать один из предложенных вариантов или ввести собственный ответ. Если вопросов несколько, пользователи могут перемещаться между ними, прежде чем отправлять все ответы.

* * *

## Пользовательские инструменты

Пользовательские инструменты позволяют вам определять собственные функции, которые может вызывать LLM. Они определены в вашем файле конфигурации и могут выполнять произвольный код.

[Подробнее](/docs/custom-tools) о создании собственных инструментов.

* * *

## MCP-серверы

Серверы MCP (Model Context Protocol) позволяют интегрировать внешние инструменты и сервисы. Сюда входит доступ к базе данных, интеграция API и сторонние сервисы.

[Подробнее](/docs/mcp-servers) о настройке серверов MCP.

* * *

## Внутреннее устройство

Внутренне такие инструменты, как `grep`, `glob` и `list`, используют [ripgrep](https://github.com/BurntSushi/ripgrep). По умолчанию ripgrep учитывает шаблоны `.gitignore`, что означает, что файлы и каталоги, перечисленные в вашем `.gitignore`, будут исключены из поиска и списков.

* * *

### Игнорировать шаблоны

Чтобы включить файлы, которые обычно игнорируются, создайте файл `.ignore` в корне вашего проекта. Этот файл может явно разрешать определенные пути.

.ignore
```
!node_modules/
    !dist/
    !build/
```

Например, этот файл `.ignore` позволяет ripgrep выполнять поиск в каталогах `node_modules/`, `dist/` и `build/`, даже если они указаны в `.gitignore`.

[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/tools.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-17"></a>
---
url: https://opencode.ai/docs/ru/rules/
---

# Правила

Установите пользовательские инструкции для opencode.

Вы можете предоставить собственные инструкции для opencode, создав файл `AGENTS.md`. Это похоже на правила Cursor. Он содержит инструкции, которые будут включены в контекст LLM для настройки его поведения для вашего конкретного проекта.

* * *

## Инициализировать

Чтобы создать новый файл `AGENTS.md`, вы можете запустить команду `/init` в opencode.

Совет

Вам следует закоммитить файл `AGENTS.md` вашего проекта в Git.

Это позволит отсканировать ваш проект и все его содержимое, чтобы понять, о чем этот проект, и сгенерировать с его помощью файл `AGENTS.md`. Это помогает opencode лучше ориентироваться в проекте.

Если у вас есть существующий файл `AGENTS.md`, мы попытаемся добавить его.

* * *

## Пример

Вы также можете просто создать этот файл вручную. Вот пример того, что вы можете поместить в файл `AGENTS.md`.

AGENTS.md
```
# SST v3 Monorepo Project
    
    
    This is an SST v3 monorepo with TypeScript. The project uses bun workspaces for package management.
    
    
    ## Project Structure
    
    
    - `packages/` - Contains all workspace packages (functions, core, web, etc.)
    - `infra/` - Infrastructure definitions split by service (storage.ts, api.ts, web.ts)
    - `sst.config.ts` - Main SST configuration with dynamic imports
    
    
    ## Code Standards
    
    
    - Use TypeScript with strict mode enabled
    - Shared code goes in `packages/core/` with proper exports configuration
    - Functions go in `packages/functions/`
    - Infrastructure should be split into logical files in `infra/`
    
    
    ## Monorepo Conventions
    
    
    - Import shared modules using workspace names: `@my-app/core/example`
```

Мы добавляем сюда инструкции для конкретного проекта, и они будут доступны всей вашей команде.

* * *

## Типы

opencode также поддерживает чтение файла `AGENTS.md` из нескольких мест. И это служит разным целям.

### Проект

Поместите `AGENTS.md` в корень вашего проекта для правил, специфичных для проекта. Они применяются только тогда, когда вы работаете в этом каталоге или его подкаталогах.

### Глобальный

Вы также можете иметь глобальные правила в файле `~/.config/opencode/AGENTS.md`. Это применяется ко всем сеансам opencode.

Поскольку это не коммитится в Git и не передается вашей команде, мы рекомендуем использовать его для указания любых личных правил, которым должен следовать LLM.

### Совместимость кода Клода

Для пользователей, переходящих с Claude Code, opencode поддерживает файловые соглашения Claude Code в качестве резерва:

  * **Правила проекта** : `CLAUDE.md` в каталоге вашего проекта (используется, если `AGENTS.md` не существует).
  * **Глобальные правила** : `~/.claude/CLAUDE.md` (используется, если `~/.config/opencode/AGENTS.md` не существует).
  * **Навыки** : `~/.claude/skills/` — подробности см. в [Навыки агента](/docs/skills/).



Чтобы отключить совместимость Claude Code, установите одну из этих переменных среды:

Окно терминала
```
export OPENCODE_DISABLE_CLAUDE_CODE=1        # Disable all .claude support
    export OPENCODE_DISABLE_CLAUDE_CODE_PROMPT=1 # Disable only ~/.claude/CLAUDE.md
    export OPENCODE_DISABLE_CLAUDE_CODE_SKILLS=1 # Disable only .claude/skills
```

* * *

## Приоритет

Когда opencode запускается, он ищет файлы правил в следующем порядке:

  1. **Локальные файлы** путем перехода вверх из текущего каталога (`AGENTS.md`, `CLAUDE.md`)
  2. **Глобальный файл** в `~/.config/opencode/AGENTS.md`.
  3. **Файл кода Клауда** по адресу `~/.claude/CLAUDE.md` (если не отключено)



Первый совпадающий файл побеждает в каждой категории. Например, если у вас есть и `AGENTS.md`, и `CLAUDE.md`, используется только `AGENTS.md`. Аналогично, `~/.config/opencode/AGENTS.md` имеет приоритет над `~/.claude/CLAUDE.md`.

* * *

## Пользовательские инструкции

Вы можете указать собственные файлы инструкций в `opencode.json` или в глобальном `~/.config/opencode/opencode.json`. Это позволит вам и вашей команде повторно использовать существующие правила вместо того, чтобы дублировать их на AGENTS.md.

Пример:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "instructions": ["CONTRIBUTING.md", "docs/guidelines.md", ".cursor/rules/*.md"]
    }
```

Вы также можете использовать удаленные URL-адреса для загрузки инструкций из Интернета.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "instructions": ["https://raw.githubusercontent.com/my-org/shared-rules/main/style.md"]
    }
```

Удаленные инструкции извлекаются с таймаутом в 5 секунд.

Все файлы инструкций объединяются с вашими файлами `AGENTS.md`.

* * *

## Ссылки на внешние файлы

Хотя opencode не анализирует автоматически ссылки на файлы в `AGENTS.md`, аналогичной функциональности можно добиться двумя способами:

### Использование opencode.json

Рекомендуемый подход — использовать поле `instructions` в `opencode.json`:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "instructions": ["docs/development-standards.md", "test/testing-guidelines.md", "packages/*/AGENTS.md"]
    }
```

### Ручные инструкции в AGENTS.md

Вы можете научить opencode читать внешние файлы, предоставив явные инструкции в файле `AGENTS.md`. Вот практический пример:

AGENTS.md
```
# TypeScript Project Rules
    
    
    ## External File Loading
    
    
    CRITICAL: When you encounter a file reference (e.g., @rules/general.md), use your Read tool to load it on a need-to-know basis. They're relevant to the SPECIFIC task at hand.
    
    
    Instructions:
    
    
    - Do NOT preemptively load all references - use lazy loading based on actual need
    - When loaded, treat content as mandatory instructions that override defaults
    - Follow references recursively when needed
    
    
    ## Development Guidelines
    
    
    For TypeScript code style and best practices: @docs/typescript-guidelines.md
    For React component architecture and hooks patterns: @docs/react-patterns.md
    For REST API design and error handling: @docs/api-standards.md
    For testing strategies and coverage requirements: @test/testing-guidelines.md
    
    
    ## General Guidelines
    
    
    Read the following file immediately as it's relevant to all workflows: @rules/general-guidelines.md.
```

Такой подход позволяет:

  * Создавайте модульные файлы правил многократного использования.
  * Делитесь правилами между проектами с помощью символических ссылок или подмодулей git.
  * Сохраняйте AGENTS.md кратким, ссылаясь на подробные инструкции.
  * Убедитесь, что opencode загружает файлы только тогда, когда это необходимо для конкретной задачи.



Совет

Для монорепозиториев или проектов с общими стандартами использование `opencode.json` с шаблонами glob (например, `packages/*/AGENTS.md`) более удобно в обслуживании, чем инструкции вручную.

[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/rules.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-18"></a>
---
url: https://opencode.ai/docs/ru/agents/
---

# Агенты

Настройте и используйте специализированные агенты.

Агенты — это специализированные ИИ-помощники, которых можно настроить для конкретных задач и рабочих процессов. Они позволяют создавать специализированные инструменты с настраиваемыми подсказками, моделями и доступом к инструментам.

Совет

Используйте агент плана для анализа кода и просмотра предложений без внесения каких-либо изменений в код.

Вы можете переключаться между агентами во время сеанса или вызывать их с помощью упоминания `@`.

* * *

## Типы

В opencode есть два типа агентов; Первичные агенты и субагенты.

* * *

### Первичные агенты

Первичные агенты — это основные помощники, с которыми вы взаимодействуете напрямую. Вы можете переключаться между ними, используя клавишу **Tab** или настроенную привязку клавиш `switch_agent`. Эти агенты ведут ваш основной разговор. Доступ к инструментам настраивается с помощью разрешений — например, при сборке все инструменты включены, а при планировании — ограничены.

Совет

Вы можете использовать клавишу **Tab** для переключения между основными агентами во время сеанса.

opencode поставляется с двумя встроенными основными агентами: **Build** и **Plan**. Мы рассмотрим их ниже.

* * *

### Субагенты

Субагенты — это специализированные помощники, которых основные агенты могут вызывать для выполнения определенных задач. Вы также можете вызвать их вручную, **@ упомянув** их в своих сообщениях.

opencode поставляется с двумя встроенными субагентами: **General** и **Explore**. Мы рассмотрим это ниже.

* * *

## Встроенные агенты

opencode поставляется с двумя встроенными основными агентами и двумя встроенными субагентами.

* * *

### Использование Build

_Режим_ : `primary`

Build — основной агент **по умолчанию** со всеми включенными инструментами. Это стандартный агент для разработки, где вам необходим полный доступ к файловым операциям и системным командам.

* * *

### Использование Plan

_Режим_ : `primary`

Агент с ограниченным доступом, предназначенный для планирования и анализа. Мы используем систему разрешений, чтобы предоставить вам больше контроля и предотвратить непреднамеренные изменения. По умолчанию для всех следующих параметров установлено значение `ask`:

  * `file edits`: Все записи, исправления и изменения.
  * `bash`: все команды bash.



Этот агент полезен, если вы хотите, чтобы LLM анализировал код, предлагал изменения или создавал планы без внесения каких-либо фактических изменений в вашу кодовую базу.

* * *

### Использование General

_Режим_ : `subagent`

Универсальный агент для исследования сложных вопросов и выполнения многоэтапных задач. Имеет полный доступ к инструментам (кроме задач), поэтому при необходимости может вносить изменения в файлы. Используйте это для параллельного выполнения нескольких единиц работы.

* * *

### Использование Explore

_Режим_ : `subagent`

Быстрый агент только для чтения для изучения кодовых баз. Невозможно изменить файлы. Используйте это, когда вам нужно быстро найти файлы по шаблонам, выполнить поиск кода по ключевым словам или ответить на вопросы о кодовой базе.

* * *

### Использование Compact

_Режим_ : `primary`

Скрытый системный агент, который сжимает длинный контекст в меньшее резюме. Он запускается автоматически при необходимости и не может быть выбран в пользовательском интерфейсе.

* * *

### Использование Title

_Режим_ : `primary`

Скрытый системный агент, генерирующий короткие заголовки сессий. Он запускается автоматически и не может быть выбран в пользовательском интерфейсе.

* * *

### Использование Summary

_Режим_ : `primary`

Скрытый системный агент, создающий сводки сеансов. Он запускается автоматически и не может быть выбран в пользовательском интерфейсе.

* * *

## Использование

  1. Для основных агентов используйте клавишу **Tab** для переключения между ними во время сеанса. Вы также можете использовать настроенную привязку клавиш `switch_agent`.

  2. Субагенты могут быть вызваны:

     * **Автоматически** основными агентами для выполнения специализированных задач на основе их описаний.

     * Вручную, **@ упомянув** субагента в своем сообщении. Например.
```
@general help me search for this function
```

  3. **Навигация между сеансами**. Когда субагенты создают свои собственные дочерние сеансы, вы можете перемещаться между родительским сеансом и всеми дочерними сеансами, используя:

     * **< Leader>+Right** (или настроенная вами комбинация клавиш `session_child_cycle`) для перехода вперед через родительский элемент → дочерний элемент1 → дочерний элемент2 → … → родительский элемент.
     * **< Leader>+Left** (или настроенная вами комбинация клавиш `session_child_cycle_reverse`) для перехода назад по родительскому элементу ← дочерний элемент1 ← дочерний элемент2 ← … ← родительский элемент

Это позволяет плавно переключаться между основным разговором и работой специализированного субагента.




* * *

## Настройка

Вы можете настроить встроенные агенты или создать свои собственные посредством настройки. Агенты можно настроить двумя способами:

* * *

### JSON

Настройте агентов в файле конфигурации `opencode.json`:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "agent": {
        "build": {
          "mode": "primary",
          "model": "anthropic/claude-sonnet-4-20250514",
          "prompt": "{file:./prompts/build.txt}",
          "tools": {
            "write": true,
            "edit": true,
            "bash": true
          }
        },
        "plan": {
          "mode": "primary",
          "model": "anthropic/claude-haiku-4-20250514",
          "tools": {
            "write": false,
            "edit": false,
            "bash": false
          }
        },
        "code-reviewer": {
          "description": "Reviews code for best practices and potential issues",
          "mode": "subagent",
          "model": "anthropic/claude-sonnet-4-20250514",
          "prompt": "You are a code reviewer. Focus on security, performance, and maintainability.",
          "tools": {
            "write": false,
            "edit": false
          }
        }
      }
    }
```

* * *

### Markdown

Вы также можете определить агентов, используя файлы Markdown. Поместите их в:

  * Глобальный: `~/.config/opencode/agents/`
  * Для каждого проекта: `.opencode/agents/`



~/.config/opencode/agents/review.md
```
---
    description: Reviews code for quality and best practices
    mode: subagent
    model: anthropic/claude-sonnet-4-20250514
    temperature: 0.1
    tools:
      write: false
      edit: false
      bash: false
    ---
    
    
    You are in code review mode. Focus on:
    
    
    - Code quality and best practices
    - Potential bugs and edge cases
    - Performance implications
    - Security considerations
    
    
    Provide constructive feedback without making direct changes.
```

Имя Markdown файла становится именем агента. Например, `review.md` создает агент `review`.

* * *

## Параметры

Давайте рассмотрим эти параметры конфигурации подробно.

* * *

### Описание

Используйте опцию `description`, чтобы предоставить краткое описание того, что делает агент и когда его использовать.

opencode.json
```
{
      "agent": {
        "review": {
          "description": "Reviews code for best practices and potential issues"
        }
      }
    }
```

Это **обязательный** параметр конфигурации.

* * *

### Температура

Контролируйте случайность и креативность ответов LLM с помощью конфигурации `temperature`.

Более низкие значения делают ответы более целенаправленными и детерминированными, а более высокие значения повышают креативность и вариативность.

opencode.json
```
{
      "agent": {
        "plan": {
          "temperature": 0.1
        },
        "creative": {
          "temperature": 0.8
        }
      }
    }
```

Значения температуры обычно находятся в диапазоне от 0,0 до 1,0:

  * **0,0–0,2** : очень целенаправленные и детерминированные ответы, идеальные для анализа кода и планирования.
  * **0,3–0,5** : сбалансированные ответы с некоторой креативностью, подходят для общих задач разработки.
  * **0,6–1,0** : более творческие и разнообразные ответы, полезные для мозгового штурма и исследования.



opencode.json
```
{
      "agent": {
        "analyze": {
          "temperature": 0.1,
          "prompt": "{file:./prompts/analysis.txt}"
        },
        "build": {
          "temperature": 0.3
        },
        "brainstorm": {
          "temperature": 0.7,
          "prompt": "{file:./prompts/creative.txt}"
        }
      }
    }
```

Если температура не указана, opencode использует значения по умолчанию, специфичные для модели; обычно 0 для большинства моделей, 0,55 для моделей Qwen.

* * *

### Максимальное количество шагов

Управляйте максимальным количеством агентных итераций, которые агент может выполнить, прежде чем ему придется отвечать только текстом. Это позволяет пользователям, желающим контролировать расходы, устанавливать лимит на агентские действия.

Если этот параметр не установлен, агент будет продолжать выполнять итерацию до тех пор, пока модель не решит остановиться или пока пользователь не прервет сеанс.

opencode.json
```
{
      "agent": {
        "quick-thinker": {
          "description": "Fast reasoning with limited iterations",
          "prompt": "You are a quick thinker. Solve problems with minimal steps.",
          "steps": 5
        }
      }
    }
```

При достижении лимита агент получает специальную системную подсказку с указанием в ответ краткой информации о своей работе и рекомендуемых оставшихся задачах.

Осторожно

Устаревшее поле `maxSteps` устарело. Вместо этого используйте `steps`.

* * *

### Отключение

Установите `true`, чтобы отключить агент.

opencode.json
```
{
      "agent": {
        "review": {
          "disable": true
        }
      }
    }
```

* * *

### Промпт

Укажите собственный файл системных приглашений для этого агента с помощью конфигурации `prompt`. Файл подсказки должен содержать инструкции, специфичные для целей агента.

opencode.json
```
{
      "agent": {
        "review": {
          "prompt": "{file:./prompts/code-review.txt}"
        }
      }
    }
```

Этот путь указан относительно того, где находится файл конфигурации. Таким образом, это работает как для глобальной конфигурации opencode, так и для конфигурации конкретного проекта.

* * *

### Модель

Используйте конфигурацию `model`, чтобы переопределить модель этого агента. Полезно для использования разных моделей, оптимизированных под разные задачи. Например, более быстрая модель планирования и более эффективная модель реализации.

Совет

Если вы не укажете модель, основные агенты будут использовать глобально настроенную модель](/docs/config#models), а субагенты будут использовать модель основного агента, вызвавшего субагент.

opencode.json
```
{
      "agent": {
        "plan": {
          "model": "anthropic/claude-haiku-4-20250514"
        }
      }
    }
```

Идентификатор модели в вашей конфигурации opencode использует формат `provider/model-id`. Например, если вы используете [OpenCode Zen](/docs/zen), вы должны использовать `opencode/gpt-5.1-codex` для кодекса GPT 5.1.

* * *

### Инструменты

Контролируйте, какие инструменты доступны в этом агенте, с помощью конфигурации `tools`. Вы можете включить или отключить определенные инструменты, установив для них значение `true` или `false`.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "tools": {
        "write": true,
        "bash": true
      },
      "agent": {
        "plan": {
          "tools": {
            "write": false,
            "bash": false
          }
        }
      }
    }
```

Заметка

Конфигурация, специфичная для агента, переопределяет глобальную конфигурацию.

Вы также можете использовать подстановочные знаки для одновременного управления несколькими инструментами. Например, чтобы отключить все инструменты с сервера MCP:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "agent": {
        "readonly": {
          "tools": {
            "mymcp_*": false,
            "write": false,
            "edit": false
          }
        }
      }
    }
```

[Подробнее об инструментах](/docs/tools).

* * *

### Разрешения

Вы можете настроить разрешения, чтобы управлять действиями, которые может выполнять агент. В настоящее время разрешения для инструментов `edit`, `bash` и `webfetch` можно настроить на:

  * `"ask"` — Запросить подтверждение перед запуском инструмента.
  * `"allow"` — Разрешить все операции без одобрения.
  * `"deny"` — отключить инструмент



opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "permission": {
        "edit": "deny"
      }
    }
```

Вы можете переопределить эти разрешения для каждого агента.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "permission": {
        "edit": "deny"
      },
      "agent": {
        "build": {
          "permission": {
            "edit": "ask"
          }
        }
      }
    }
```

Вы также можете установить разрешения в агентах Markdown.

~/.config/opencode/agents/review.md
```
---
    description: Code review without edits
    mode: subagent
    permission:
      edit: deny
      bash:
        "*": ask
        "git diff": allow
        "git log*": allow
        "grep *": allow
      webfetch: deny
    ---
    
    
    Only analyze code and suggest changes.
```

Вы можете установить разрешения для определенных команд bash.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "agent": {
        "build": {
          "permission": {
            "bash": {
              "git push": "ask",
              "grep *": "allow"
            }
          }
        }
      }
    }
```

Это может использовать glob pattern.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "agent": {
        "build": {
          "permission": {
            "bash": {
              "git *": "ask"
            }
          }
        }
      }
    }
```

Вы также можете использовать подстановочный знак `*` для управления разрешениями для всех команд. Поскольку последнее правило сопоставления имеет приоритет, сначала поместите подстановочный знак `*`, а затем конкретные правила.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "agent": {
        "build": {
          "permission": {
            "bash": {
              "*": "ask",
              "git status *": "allow"
            }
          }
        }
      }
    }
```

[Подробнее о разрешениях](/docs/permissions).

* * *

### Режим

Управляйте режимом агента с помощью конфигурации `mode`. Опция `mode` используется для определения того, как можно использовать агент.

opencode.json
```
{
      "agent": {
        "review": {
          "mode": "subagent"
        }
      }
    }
```

Опция `mode` может быть установлена ​​на `primary`, `subagent` или `all`. Если `mode` не указан, по умолчанию используется `all`.

* * *

### Скрытый

Скройте субагент из меню автозаполнения `@` с помощью `hidden: true`. Полезно для внутренних субагентов, которые другие агенты должны вызывать только программно с помощью инструмента Task.

opencode.json
```
{
      "agent": {
        "internal-helper": {
          "mode": "subagent",
          "hidden": true
        }
      }
    }
```

Это влияет только на видимость пользователя в меню автозаполнения. Скрытые агенты по-прежнему могут быть вызваны моделью с помощью инструмента «Задачи», если разрешения позволяют.

Заметка

Применяется только к агентам `mode: subagent`.

* * *

### Разрешения задач

Управляйте тем, какие субагенты агент может вызывать с помощью инструмента задач с помощью `permission.task`. Использует шаблоны glob для гибкого сопоставления.

opencode.json
```
{
      "agent": {
        "orchestrator": {
          "mode": "primary",
          "permission": {
            "task": {
              "*": "deny",
              "orchestrator-*": "allow",
              "code-reviewer": "ask"
            }
          }
        }
      }
    }
```

Если установлено значение `deny`, субагент полностью удаляется из описания инструмента «Задача», поэтому модель не будет пытаться его вызвать.

Совет

Правила оцениваются по порядку, и **побеждает последнее подходящее правило**. В приведенном выше примере `orchestrator-planner` соответствует как `*` (запретить), так и `orchestrator-*` (разрешить), но поскольку `orchestrator-*` идет после `*`, результатом будет `allow`.

Совет

Пользователи всегда могут вызвать любой субагент напрямую через меню автозаполнения `@`, даже если разрешения задач агента запрещают это.

* * *

### Цвет

Настройте внешний вид агента в пользовательском интерфейсе с помощью параметра `color`. Это влияет на то, как агент будет отображаться в интерфейсе.

Используйте допустимый шестнадцатеричный цвет (например, `#FF5733`) или цвет темы: `primary`, `secondary`, `accent`, `success`, `warning`, `error`, `info`.

opencode.json
```
{
      "agent": {
        "creative": {
          "color": "#ff6b6b"
        },
        "code-reviewer": {
          "color": "accent"
        }
      }
    }
```

* * *

### Top P

Управляйте разнообразием ответов с помощью опции `top_p`. Альтернатива температуре для контроля случайности.

opencode.json
```
{
      "agent": {
        "brainstorm": {
          "top_p": 0.9
        }
      }
    }
```

Значения варьируются от 0,0 до 1,0. Низкие значения делают ответы более целенаправленными, высокие — более разнообразными.

* * *

### Дополнительно

Любые другие параметры, указанные вами в конфигурации вашего агента, будут **передаваться напрямую** поставщику в качестве параметров модели. Это позволяет использовать функции и параметры, специфичные для поставщика.

Например, с помощью моделей рассуждения OpenAI вы можете контролировать усилия по рассуждению:

opencode.json
```
{
      "agent": {
        "deep-thinker": {
          "description": "Agent that uses high reasoning effort for complex problems",
          "model": "openai/gpt-5",
          "reasoningEffort": "high",
          "textVerbosity": "low"
        }
      }
    }
```

Эти дополнительные параметры зависят от модели и поставщика. Проверьте документацию вашего провайдера на наличие доступных параметров.

Совет

Запустите `opencode models`, чтобы просмотреть список доступных моделей.

* * *

## Создание агентов

Вы можете создать новых агентов, используя следующую команду:

Окно терминала
```
opencode agent create
```

Эта интерактивная команда:

  1. Спрашивает, где сохранить агента: глобально или в проекте.
  2. Запрашивает описание того, что должен делать агент.
  3. Создает соответствующий системный промпт и идентификатор.
  4. Позволяет выбрать, к каким инструментам агент будет иметь доступ.
  5. Наконец, создает файл Markdown с конфигурацией агента.



* * *

## Варианты использования

Вот несколько распространенных случаев использования различных агентов.

  * **Агент сборки** : полная работа по разработке со всеми включенными инструментами.
  * **Агент планирования** : анализ и планирование без внесения изменений.
  * **Агент проверки** : проверка кода с доступом только для чтения и инструментами документирования.
  * **Агент отладки** : сосредоточен на исследовании с включенными инструментами bash и чтения.
  * **Агент документов** : запись документации с помощью файловых операций, но без системных команд.



* * *

## Примеры

Вот несколько примеров агентов, которые могут оказаться вам полезными.

Совет

У вас есть агент, которым вы хотели бы поделиться? [Отправьте PR](https://github.com/anomalyco/opencode).

* * *

### Агент документации

~/.config/opencode/agents/docs-writer.md
```
---
    description: Writes and maintains project documentation
    mode: subagent
    tools:
      bash: false
    ---
    
    
    You are a technical writer. Create clear, comprehensive documentation.
    
    
    Focus on:
    
    
    - Clear explanations
    - Proper structure
    - Code examples
    - User-friendly language
```

* * *

### Аудитор безопасности

~/.config/opencode/agents/security-auditor.md
```
---
    description: Performs security audits and identifies vulnerabilities
    mode: subagent
    tools:
      write: false
      edit: false
    ---
    
    
    You are a security expert. Focus on identifying potential security issues.
    
    
    Look for:
    
    
    - Input validation vulnerabilities
    - Authentication and authorization flaws
    - Data exposure risks
    - Dependency vulnerabilities
    - Configuration security issues
```

[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/agents.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-19"></a>
---
url: https://opencode.ai/docs/ru/models/
---

# Модели

Настройка поставщика и модели LLM.

opencode использует [AI SDK](https://ai-sdk.dev/) и [Models.dev](https://models.dev) для поддержки **более 75 поставщиков LLM** и поддерживает запуск локальных моделей.

* * *

## Провайдеры

Большинство популярных провайдеров предварительно загружены по умолчанию. Если вы добавили учетные данные для поставщика с помощью команды `/connect`, они будут доступны при запуске opencode.

Узнайте больше о [providers](/docs/providers).

* * *

## Выберите модель

После того, как вы настроили своего провайдера, вы можете выбрать нужную модель, введя:
```
/models
```

* * *

## Рекомендуемые модели

Моделей очень много, новые выходят каждую неделю.

Совет

Рассмотрите возможность использования одной из моделей, которые мы рекомендуем.

Однако лишь немногие из них хороши как в генерации кода, так и в вызове инструментов.

Вот несколько моделей, которые хорошо работают с opencode (в произвольном порядке). (Это не исчерпывающий список и не обязательно актуальный):

  * GPT 5.2
  * Кодекс GPT 5.1
  * Claude Opus 4.5
  * Claude Sonnet 4.5
  * MiniMax M2.1
  * Gemini 3 Pro



* * *

## Установить значение по умолчанию

Чтобы установить одну из них в качестве модели по умолчанию, вы можете установить ключ `model` в вашем Конфигурация opencode.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "model": "lmstudio/google/gemma-3n-e4b"
    }
```

Здесь полный идентификатор `provider_id/model_id`. Например, если вы используете [OpenCode Zen](/docs/zen), вы должны использовать `opencode/gpt-5.1-codex` для кодекса GPT 5.1.

Если вы настроили [пользовательский поставщик](/docs/providers#custom), `provider_id` — это ключ из части `provider` вашей конфигурации, а `model_id` — это ключ из `provider.models`.

* * *

## Настройка моделей

Вы можете глобально настроить параметры модели через файл config.

opencode.jsonc
```
{
      "$schema": "https://opencode.ai/config.json",
      "provider": {
        "openai": {
          "models": {
            "gpt-5": {
              "options": {
                "reasoningEffort": "high",
                "textVerbosity": "low",
                "reasoningSummary": "auto",
                "include": ["reasoning.encrypted_content"],
              },
            },
          },
        },
        "anthropic": {
          "models": {
            "claude-sonnet-4-5-20250929": {
              "options": {
                "thinking": {
                  "type": "enabled",
                  "budgetTokens": 16000,
                },
              },
            },
          },
        },
      },
    }
```

Здесь мы настраиваем глобальные параметры для двух встроенных моделей: `gpt-5` при доступе через поставщика `openai` и `claude-sonnet-4-20250514` при доступе через поставщика `anthropic`. Названия встроенных поставщиков и моделей можно найти на сайте [Models.dev](https://models.dev).

Вы также можете настроить эти параметры для любых используемых вами агентов. Конфигурация агента переопределяет любые глобальные параметры здесь. [Подробнее](/docs/agents/#additional).

Вы также можете определить собственные варианты, расширяющие встроенные. Варианты позволяют настраивать разные параметры для одной и той же модели без создания повторяющихся записей:

opencode.jsonc
```
{
      "$schema": "https://opencode.ai/config.json",
      "provider": {
        "opencode": {
          "models": {
            "gpt-5": {
              "variants": {
                "high": {
                  "reasoningEffort": "high",
                  "textVerbosity": "low",
                  "reasoningSummary": "auto",
                },
                "low": {
                  "reasoningEffort": "low",
                  "textVerbosity": "low",
                  "reasoningSummary": "auto",
                },
              },
            },
          },
        },
      },
    }
```

* * *

## Варианты

Многие модели поддерживают несколько вариантов с разными конфигурациями. opencode поставляется со встроенными вариантами по умолчанию для популярных провайдеров.

### Встроенные варианты

opencode поставляется с вариантами по умолчанию для многих провайдеров:

**Anthropic** :

  * `high` — Бюджет рассуждений: высокий (по умолчанию)
  * `max` — Максимальный бюджет рассуждений



**OpenAI** :

Зависит от модели, но примерно:

  * `none` — Без рассуждений.
  * `minimal` — Минимальные усилия для рассуждений
  * `low` — Низкие усилия для рассуждений.
  * `medium` — Средние усилия для рассуждений.
  * `high` — Высокие усилия для рассуждений.
  * `xhigh` — Сверхвысокие усилия для рассуждений.



**Google** :

  * `low` – меньший бюджет усилий/токенов.
  * `high` — более высокий бюджет усилий/токенов



Совет

Этот список не является исчерпывающим. Многие другие провайдеры также имеют встроенные настройки по умолчанию.

### Пользовательские варианты

Вы можете переопределить существующие варианты или добавить свои собственные:

opencode.jsonc
```
{
      "$schema": "https://opencode.ai/config.json",
      "provider": {
        "openai": {
          "models": {
            "gpt-5": {
              "variants": {
                "thinking": {
                  "reasoningEffort": "high",
                  "textVerbosity": "low",
                },
                "fast": {
                  "disabled": true,
                },
              },
            },
          },
        },
      },
    }
```

### Переключение вариантов

Используйте сочетание клавиш `variant_cycle` для быстрого переключения между вариантами. [Подробнее ](/docs/keybinds).

* * *

## Загрузка моделей

Когда opencode запускается, он проверяет модели в следующем порядке приоритета:

  1. CLI-флаг `--model` или `-m`. Формат тот же, что и в файле конфигурации: `provider_id/model_id`.

  2. Список моделей в конфигурации opencode.

opencode.json
```
{
           "$schema": "https://opencode.ai/config.json",
           "model": "anthropic/claude-sonnet-4-20250514"
         }
```

Здесь используется формат `provider/model`.

  3. Последняя использованная модель.

  4. Первая модель, использующая внутренний приоритет.




[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/models.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-20"></a>
---
url: https://opencode.ai/docs/ru/themes/
---

# Темы

Выберите встроенную тему или определите свою собственную.

С помощью opencode вы можете выбрать одну из нескольких встроенных тем, использовать тему, которая адаптируется к теме вашего терминала, или определить свою собственную тему.

По умолчанию opencode использует нашу собственную тему `opencode`.

* * *

## Требования к терминалу

Чтобы темы корректно отображались в полной цветовой палитре, ваш терминал должен поддерживать **truecolor** (24-битный цвет). Большинство современных терминалов поддерживают это по умолчанию, но вам может потребоваться включить его:

  * **Проверьте поддержку** : запустите `echo $COLORTERM` — должен появиться `truecolor` или `24bit`.
  * **Включить truecolor** : установите переменную среды `COLORTERM=truecolor` в профиле shell.
  * **Совместимость терминала** : убедитесь, что ваш эмулятор терминала поддерживает 24-битный цвет (большинство современных терминалов, таких как iTerm2, Alacritty, Kitty, Windows Terminal и последние версии GNOME Terminal, поддерживают).



Без поддержки truecolor темы могут отображаться с пониженной точностью цветопередачи или вернуться к ближайшему приближению к 256 цветам.

* * *

## Встроенные темы

opencode поставляется с несколькими встроенными темами.

Имя| Описание  
---|---  
`system`| Адаптируется к фоновому цвету терминала  
`tokyonight`| Based on the [tokyonight](https://github.com/folke/tokyonight.nvim) theme  
`everforest`| Based on the [Everforest](https://github.com/sainnhe/everforest) theme  
`ayu`| Based on the [Ayu](https://github.com/ayu-theme) dark theme  
`catppuccin`| Based on the [Catppuccin](https://github.com/catppuccin) theme  
`catppuccin-macchiato`| Based on the [Catppuccin](https://github.com/catppuccin) theme  
`gruvbox`| Based on the [Gruvbox](https://github.com/morhetz/gruvbox) theme  
`kanagawa`| Based on the [Kanagawa](https://github.com/rebelot/kanagawa.nvim) theme  
`nord`| Based on the [Nord](https://github.com/nordtheme/nord) theme  
`matrix`| Хакерская тема: зеленый на черном  
`one-dark`| Based on the [Atom One](https://github.com/Th3Whit3Wolf/one-nvim) Dark theme  
  
И более того, мы постоянно добавляем новые темы.

* * *

## Системная тема

Тема `system` автоматически адаптируется к цветовой схеме вашего терминала. В отличие от традиционных тем, использующих фиксированные цвета, тема _system_ :

  * **Создает шкалу серого** : создает пользовательскую шкалу серого на основе цвета фона вашего терминала, обеспечивая оптимальный контраст.
  * **Использует цвета ANSI** : использует стандартные цвета ANSI (0–15) для подсветки синтаксиса и элементов пользовательского интерфейса, которые соответствуют цветовой палитре вашего терминала.
  * **Сохраняет настройки терминала по умолчанию** : использует `none` для цветов текста и фона, чтобы сохранить естественный вид вашего терминала.



Системная тема предназначена для пользователей, которые:

  * Хотите, чтобы opencode соответствовал внешнему виду их терминала
  * Используйте пользовательские цветовые схемы терминала
  * Предпочитайте единообразный вид для всех терминальных приложений.



* * *

## Использование темы

Вы можете выбрать тему, вызвав выбор темы с помощью команды `/theme`. Или вы можете указать это в файле [config](/docs/config).

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "theme": "tokyonight"
    }
```

* * *

## Пользовательские темы

opencode поддерживает гибкую систему тем на основе JSON, которая позволяет пользователям легко создавать и настраивать темы.

* * *

### Иерархия

Темы загружаются из нескольких каталогов в следующем порядке: более поздние каталоги переопределяют предыдущие:

  1. **Встроенные темы** – они встроены в двоичный файл.
  2. **Каталог конфигурации пользователя** – определяется в `~/.config/opencode/themes/*.json` или `$XDG_CONFIG_HOME/opencode/themes/*.json`.
  3. **Корневой каталог проекта** – определено в `<project-root>/.opencode/themes/*.json`.
  4. **Текущий рабочий каталог** – определено в `./.opencode/themes/*.json`.



Если несколько каталогов содержат тему с одинаковым именем, будет использоваться тема из каталога с более высоким приоритетом.

* * *

### Создание темы

Чтобы создать собственную тему, создайте файл JSON в одном из каталогов темы.

Для глобальных тем:

Окно терминала
```
mkdir -p ~/.config/opencode/themes
    vim ~/.config/opencode/themes/my-theme.json
```

Для тем проекта:

Окно терминала
```
mkdir -p .opencode/themes
    vim .opencode/themes/my-theme.json
```

* * *

### Формат JSON

В темах используется гибкий формат JSON с поддержкой:

  * **Шестнадцатеричные цвета** : `"#ffffff"`
  * **Цвета ANSI** : `3` (0–255).
  * **Ссылки на цвета** : `"primary"` или пользовательские определения.
  * **Темный/светлый варианты** : `{"dark": "#000", "light": "#fff"}`
  * **Нет цвета** : `"none"` — используется цвет терминала по умолчанию или прозрачный.



* * *

### Определения цвета

Раздел `defs` является необязательным и позволяет вам определять повторно используемые цвета, на которые можно ссылаться в теме.

* * *

### Настройки терминала по умолчанию

Специальное значение `"none"` можно использовать для любого цвета, чтобы наследовать цвет терминала по умолчанию. Это особенно полезно для создания тем, которые органично сочетаются с цветовой схемой вашего терминала:

  * `"text": "none"` — использует цвет переднего плана терминала по умолчанию.
  * `"background": "none"` — использует цвет фона терминала по умолчанию.



* * *

### Пример

Вот пример пользовательской темы:

my-theme.json
```
{
      "$schema": "https://opencode.ai/theme.json",
      "defs": {
        "nord0": "#2E3440",
        "nord1": "#3B4252",
        "nord2": "#434C5E",
        "nord3": "#4C566A",
        "nord4": "#D8DEE9",
        "nord5": "#E5E9F0",
        "nord6": "#ECEFF4",
        "nord7": "#8FBCBB",
        "nord8": "#88C0D0",
        "nord9": "#81A1C1",
        "nord10": "#5E81AC",
        "nord11": "#BF616A",
        "nord12": "#D08770",
        "nord13": "#EBCB8B",
        "nord14": "#A3BE8C",
        "nord15": "#B48EAD"
      },
      "theme": {
        "primary": {
          "dark": "nord8",
          "light": "nord10"
        },
        "secondary": {
          "dark": "nord9",
          "light": "nord9"
        },
        "accent": {
          "dark": "nord7",
          "light": "nord7"
        },
        "error": {
          "dark": "nord11",
          "light": "nord11"
        },
        "warning": {
          "dark": "nord12",
          "light": "nord12"
        },
        "success": {
          "dark": "nord14",
          "light": "nord14"
        },
        "info": {
          "dark": "nord8",
          "light": "nord10"
        },
        "text": {
          "dark": "nord4",
          "light": "nord0"
        },
        "textMuted": {
          "dark": "nord3",
          "light": "nord1"
        },
        "background": {
          "dark": "nord0",
          "light": "nord6"
        },
        "backgroundPanel": {
          "dark": "nord1",
          "light": "nord5"
        },
        "backgroundElement": {
          "dark": "nord1",
          "light": "nord4"
        },
        "border": {
          "dark": "nord2",
          "light": "nord3"
        },
        "borderActive": {
          "dark": "nord3",
          "light": "nord2"
        },
        "borderSubtle": {
          "dark": "nord2",
          "light": "nord3"
        },
        "diffAdded": {
          "dark": "nord14",
          "light": "nord14"
        },
        "diffRemoved": {
          "dark": "nord11",
          "light": "nord11"
        },
        "diffContext": {
          "dark": "nord3",
          "light": "nord3"
        },
        "diffHunkHeader": {
          "dark": "nord3",
          "light": "nord3"
        },
        "diffHighlightAdded": {
          "dark": "nord14",
          "light": "nord14"
        },
        "diffHighlightRemoved": {
          "dark": "nord11",
          "light": "nord11"
        },
        "diffAddedBg": {
          "dark": "#3B4252",
          "light": "#E5E9F0"
        },
        "diffRemovedBg": {
          "dark": "#3B4252",
          "light": "#E5E9F0"
        },
        "diffContextBg": {
          "dark": "nord1",
          "light": "nord5"
        },
        "diffLineNumber": {
          "dark": "nord2",
          "light": "nord4"
        },
        "diffAddedLineNumberBg": {
          "dark": "#3B4252",
          "light": "#E5E9F0"
        },
        "diffRemovedLineNumberBg": {
          "dark": "#3B4252",
          "light": "#E5E9F0"
        },
        "markdownText": {
          "dark": "nord4",
          "light": "nord0"
        },
        "markdownHeading": {
          "dark": "nord8",
          "light": "nord10"
        },
        "markdownLink": {
          "dark": "nord9",
          "light": "nord9"
        },
        "markdownLinkText": {
          "dark": "nord7",
          "light": "nord7"
        },
        "markdownCode": {
          "dark": "nord14",
          "light": "nord14"
        },
        "markdownBlockQuote": {
          "dark": "nord3",
          "light": "nord3"
        },
        "markdownEmph": {
          "dark": "nord12",
          "light": "nord12"
        },
        "markdownStrong": {
          "dark": "nord13",
          "light": "nord13"
        },
        "markdownHorizontalRule": {
          "dark": "nord3",
          "light": "nord3"
        },
        "markdownListItem": {
          "dark": "nord8",
          "light": "nord10"
        },
        "markdownListEnumeration": {
          "dark": "nord7",
          "light": "nord7"
        },
        "markdownImage": {
          "dark": "nord9",
          "light": "nord9"
        },
        "markdownImageText": {
          "dark": "nord7",
          "light": "nord7"
        },
        "markdownCodeBlock": {
          "dark": "nord4",
          "light": "nord0"
        },
        "syntaxComment": {
          "dark": "nord3",
          "light": "nord3"
        },
        "syntaxKeyword": {
          "dark": "nord9",
          "light": "nord9"
        },
        "syntaxFunction": {
          "dark": "nord8",
          "light": "nord8"
        },
        "syntaxVariable": {
          "dark": "nord7",
          "light": "nord7"
        },
        "syntaxString": {
          "dark": "nord14",
          "light": "nord14"
        },
        "syntaxNumber": {
          "dark": "nord15",
          "light": "nord15"
        },
        "syntaxType": {
          "dark": "nord7",
          "light": "nord7"
        },
        "syntaxOperator": {
          "dark": "nord9",
          "light": "nord9"
        },
        "syntaxPunctuation": {
          "dark": "nord4",
          "light": "nord0"
        }
      }
    }
```

[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/themes.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-21"></a>
---
url: https://opencode.ai/docs/ru/keybinds/
---

# Сочетания клавиш

Настройте свои сочетания клавиш.

opencode имеет список сочетаний клавиш, которые вы можете настроить через конфигурацию opencode.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "keybinds": {
        "leader": "ctrl+x",
        "app_exit": "ctrl+c,ctrl+d,<leader>q",
        "editor_open": "<leader>e",
        "theme_list": "<leader>t",
        "sidebar_toggle": "<leader>b",
        "scrollbar_toggle": "none",
        "username_toggle": "none",
        "status_view": "<leader>s",
        "tool_details": "none",
        "session_export": "<leader>x",
        "session_new": "<leader>n",
        "session_list": "<leader>l",
        "session_timeline": "<leader>g",
        "session_fork": "none",
        "session_rename": "none",
        "session_share": "none",
        "session_unshare": "none",
        "session_interrupt": "escape",
        "session_compact": "<leader>c",
        "session_child_cycle": "<leader>right",
        "session_child_cycle_reverse": "<leader>left",
        "session_parent": "<leader>up",
        "messages_page_up": "pageup,ctrl+alt+b",
        "messages_page_down": "pagedown,ctrl+alt+f",
        "messages_line_up": "ctrl+alt+y",
        "messages_line_down": "ctrl+alt+e",
        "messages_half_page_up": "ctrl+alt+u",
        "messages_half_page_down": "ctrl+alt+d",
        "messages_first": "ctrl+g,home",
        "messages_last": "ctrl+alt+g,end",
        "messages_next": "none",
        "messages_previous": "none",
        "messages_copy": "<leader>y",
        "messages_undo": "<leader>u",
        "messages_redo": "<leader>r",
        "messages_last_user": "none",
        "messages_toggle_conceal": "<leader>h",
        "model_list": "<leader>m",
        "model_cycle_recent": "f2",
        "model_cycle_recent_reverse": "shift+f2",
        "model_cycle_favorite": "none",
        "model_cycle_favorite_reverse": "none",
        "variant_cycle": "ctrl+t",
        "command_list": "ctrl+p",
        "agent_list": "<leader>a",
        "agent_cycle": "tab",
        "agent_cycle_reverse": "shift+tab",
        "input_clear": "ctrl+c",
        "input_paste": "ctrl+v",
        "input_submit": "return",
        "input_newline": "shift+return,ctrl+return,alt+return,ctrl+j",
        "input_move_left": "left,ctrl+b",
        "input_move_right": "right,ctrl+f",
        "input_move_up": "up",
        "input_move_down": "down",
        "input_select_left": "shift+left",
        "input_select_right": "shift+right",
        "input_select_up": "shift+up",
        "input_select_down": "shift+down",
        "input_line_home": "ctrl+a",
        "input_line_end": "ctrl+e",
        "input_select_line_home": "ctrl+shift+a",
        "input_select_line_end": "ctrl+shift+e",
        "input_visual_line_home": "alt+a",
        "input_visual_line_end": "alt+e",
        "input_select_visual_line_home": "alt+shift+a",
        "input_select_visual_line_end": "alt+shift+e",
        "input_buffer_home": "home",
        "input_buffer_end": "end",
        "input_select_buffer_home": "shift+home",
        "input_select_buffer_end": "shift+end",
        "input_delete_line": "ctrl+shift+d",
        "input_delete_to_line_end": "ctrl+k",
        "input_delete_to_line_start": "ctrl+u",
        "input_backspace": "backspace,shift+backspace",
        "input_delete": "ctrl+d,delete,shift+delete",
        "input_undo": "ctrl+-,super+z",
        "input_redo": "ctrl+.,super+shift+z",
        "input_word_forward": "alt+f,alt+right,ctrl+right",
        "input_word_backward": "alt+b,alt+left,ctrl+left",
        "input_select_word_forward": "alt+shift+f,alt+shift+right",
        "input_select_word_backward": "alt+shift+b,alt+shift+left",
        "input_delete_word_forward": "alt+d,alt+delete,ctrl+delete",
        "input_delete_word_backward": "ctrl+w,ctrl+backspace,alt+backspace",
        "history_previous": "up",
        "history_next": "down",
        "terminal_suspend": "ctrl+z",
        "terminal_title_toggle": "none",
        "tips_toggle": "<leader>h",
        "display_thinking": "none"
      }
    }
```

* * *

## Клавиша Leader

opencode использует клавишу `leader` для большинства сочетаний клавиш. Это позволяет избежать конфликтов в вашем терминале.

По умолчанию `ctrl+x` является клавишей leader, и для большинства действий требуется сначала нажать клавишу leader, а затем сочетание клавиш. Например, чтобы начать новый сеанс, сначала нажмите `ctrl+x`, а затем нажмите `n`.

Вам не обязательно использовать клавишу leader для привязок клавиш, но мы рекомендуем это сделать.

* * *

## Отключение привязки клавиш

Вы можете отключить привязку клавиш, добавив ключ в свою конфигурацию со значением «none».

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "keybinds": {
        "session_compact": "none"
      }
    }
```

* * *

## Шорткаты в Desktop-приложении

Ввод приглашения настольного приложения opencode поддерживает распространенные сочетания клавиш в стиле Readline/Emacs для редактирования текста. Они встроены и в настоящее время не настраиваются через `opencode.json`.

Ярлык| Действие  
---|---  
`ctrl+a`| Перейти к началу текущей строки  
`ctrl+e`| Перейти к концу текущей строки  
`ctrl+b`| Переместить курсор на один символ назад  
`ctrl+f`| Переместить курсор на один символ вперед  
`alt+b`| Переместить курсор на одно слово назад  
`alt+f`| Переместить курсор вперед на одно слово  
`ctrl+d`| Удалить символ под курсором  
`ctrl+k`| Удалить до конца строки  
`ctrl+u`| Удалить до начала строки  
`ctrl+w`| Удалить предыдущее слово  
`alt+d`| Удалить следующее слово  
`ctrl+t`| Поменять местами символы  
`ctrl+g`| Отменить всплывающие окна/прервать выполнение ответа  
  
* * *

## Shift+Enter

Некоторые терминалы по умолчанию не отправляют клавиши-модификаторы с Enter. Возможно, вам придется настроить терминал на отправку `Shift+Enter` в качестве escape-последовательности.

### Windows Terminal

Откройте свой `settings.json` по адресу:
```
%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json
```

Добавьте это в массив `actions` корневого уровня:
```
"actions": [
      {
        "command": {
          "action": "sendInput",
          "input": "\u001b[13;2u"
        },
        "id": "User.sendInput.ShiftEnterCustom"
      }
    ]
```

Добавьте это в массив `keybindings` корневого уровня:
```
"keybindings": [
      {
        "keys": "shift+enter",
        "id": "User.sendInput.ShiftEnterCustom"
      }
    ]
```

Сохраните файл и перезапустите Windows Terminal или откройте новую вкладку.

[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/keybinds.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-22"></a>
---
url: https://opencode.ai/docs/ru/commands/
---

# Команды

Создавайте собственные команды для повторяющихся задач.

Пользовательские команды позволяют указать подсказку, которую вы хотите запускать при выполнении этой команды в TUI.
```
/my-command
```

Пользовательские команды дополняют встроенные команды, такие как `/init`, `/undo`, `/redo`, `/share`, `/help`. [Подробнее](/docs/tui#commands).

* * *

## Создание файлов команд

Создайте Markdown файлы в каталоге `commands/` для определения пользовательских команд.

Создайте `.opencode/commands/test.md`:

.opencode/commands/test.md
```
---
    description: Run tests with coverage
    agent: build
    model: anthropic/claude-3-5-sonnet-20241022
    ---
    
    
    Run the full test suite with coverage report and show any failures.
    Focus on the failing tests and suggest fixes.
```

Фронтматтер (frontmatter) определяет свойства команды. Содержимое становится шаблоном.

Используйте команду, набрав `/`, а затем имя команды.
```
"/test"
```

* * *

## Настройка

Вы можете добавлять собственные команды через конфигурацию opencode или создав файлы Markdown в каталоге `commands/`.

* * *

### JSON

Используйте опцию `command` в вашем opencode [config](/docs/config):

opencode.jsonc
```
{
      "$schema": "https://opencode.ai/config.json",
      "command": {
        // This becomes the name of the command
        "test": {
          // This is the prompt that will be sent to the LLM
          "template": "Run the full test suite with coverage report and show any failures.\nFocus on the failing tests and suggest fixes.",
          // This is shown as the description in the TUI
          "description": "Run tests with coverage",
          "agent": "build",
          "model": "anthropic/claude-3-5-sonnet-20241022"
        }
      }
    }
```

Теперь вы можете запустить эту команду в TUI:
```
/test
```

* * *

### Markdown

Вы также можете определять команды, используя Markdown файлы. Поместите их в:

  * Глобальный: `~/.config/opencode/commands/`
  * Для каждого проекта: `.opencode/commands/`



~/.config/opencode/commands/test.md
```
---
    description: Run tests with coverage
    agent: build
    model: anthropic/claude-3-5-sonnet-20241022
    ---
    
    
    Run the full test suite with coverage report and show any failures.
    Focus on the failing tests and suggest fixes.
```

Имя Markdown файла становится именем команды. Например, `test.md` позволяет вам запустить:
```
/test
```

* * *

## Настройка промпта

Подсказки для пользовательских команд поддерживают несколько специальных заполнителей и синтаксиса.

* * *

### Аргументы

Передавайте аргументы командам, используя заполнитель `$ARGUMENTS`.

.opencode/commands/component.md
```
---
    description: Create a new component
    ---
    
    
    Create a new React component named $ARGUMENTS with TypeScript support.
    Include proper typing and basic structure.
```

Запустите команду с аргументами:
```
/component Button
```

И `$ARGUMENTS` будет заменен на `Button`.

Вы также можете получить доступ к отдельным аргументам, используя позиционные параметры:

  * `$1` — первый аргумент
  * `$2` — Второй аргумент
  * `$3` — Третий аргумент
  * И так далее…



Например:

.opencode/commands/create-file.md
```
---
    description: Create a new file with content
    ---
    
    
    Create a file named $1 in the directory $2
    with the following content: $3
```

Запустите команду:
```
/create-file config.json src "{ \"key\": \"value\" }"
```

Это заменяет:

  * `$1` с `config.json`
  * `$2` с `src`
  * `$3` с `{ "key": "value" }`



* * *

### Вывод shell

Используйте _!`command`_, чтобы ввести вывод команды bash](/docs/tui#bash-commands) в приглашение.

Например, чтобы создать пользовательскую команду, которая анализирует тестовое покрытие:

.opencode/commands/analyze-coverage.md
```
---
    description: Analyze test coverage
    ---
    
    
    Here are the current test results:
    !`npm test`
    
    
    Based on these results, suggest improvements to increase coverage.
```

Или просмотреть последние изменения:

.opencode/commands/review-changes.md
```
---
    description: Review recent changes
    ---
    
    
    Recent git commits:
    !`git log --oneline -10`
    
    
    Review these changes and suggest any improvements.
```

Команды выполняются в корневом каталоге вашего проекта, и их вывод становится частью приглашения.

* * *

### Ссылки на файлы

Включите файлы в свою команду, используя `@`, за которым следует имя файла.

.opencode/commands/review-component.md
```
---
    description: Review component
    ---
    
    
    Review the component in @src/components/Button.tsx.
    Check for performance issues and suggest improvements.
```

Содержимое файла автоматически включается в приглашение.

* * *

## Параметры

Рассмотрим варианты конфигурации подробнее.

* * *

### Template

Параметр `template` определяет приглашение, которое будет отправлено в LLM при выполнении команды.

opencode.json
```
{
      "command": {
        "test": {
          "template": "Run the full test suite with coverage report and show any failures.\nFocus on the failing tests and suggest fixes."
        }
      }
    }
```

Это **обязательный** параметр конфигурации.

* * *

### Описание

Используйте опцию `description`, чтобы предоставить краткое описание того, что делает команда.

opencode.json
```
{
      "command": {
        "test": {
          "description": "Run tests with coverage"
        }
      }
    }
```

Это отображается в виде описания в TUI при вводе команды.

* * *

### Агент

Используйте конфигурацию `agent`, чтобы дополнительно указать, какой [агент](/docs/agents) должен выполнить эту команду. Если это [subagent](/docs/agents/#subagents), команда по умолчанию инициирует вызов субагента. Чтобы отключить это поведение, установите для `subtask` значение `false`.

opencode.json
```
{
      "command": {
        "review": {
          "agent": "plan"
        }
      }
    }
```

Это **необязательный** параметр конфигурации. Если не указано, по умолчанию используется текущий агент.

* * *

### Subtask

Используйте логическое значение `subtask`, чтобы заставить команду инициировать вызов [subagent](/docs/agents/#subagents). Это полезно, если вы хотите, чтобы команда не загрязняла ваш основной контекст и **заставляла** агента действовать как субагент. даже если для `mode` установлено значение `primary` в конфигурации [agent](/docs/agents).

opencode.json
```
{
      "command": {
        "analyze": {
          "subtask": true
        }
      }
    }
```

Это **необязательный** параметр конфигурации.

* * *

### Модель

Используйте конфигурацию `model`, чтобы переопределить модель по умолчанию для этой команды.

opencode.json
```
{
      "command": {
        "analyze": {
          "model": "anthropic/claude-3-5-sonnet-20241022"
        }
      }
    }
```

Это **необязательный** параметр конфигурации.

* * *

## Встроенные команды

opencode включает несколько встроенных команд, таких как `/init`, `/undo`, `/redo`, `/share`, `/help`; [подробнее](/docs/tui#commands).

Заметка

Пользовательские команды могут переопределять встроенные команды.

Если вы определите пользовательскую команду с тем же именем, она переопределит встроенную команду.

[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/commands.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-23"></a>
---
url: https://opencode.ai/docs/ru/formatters/
---

# Форматтеры

opencode использует средства форматирования, специфичные для языка.

opencode автоматически форматирует файлы после их записи или редактирования с использованием средств форматирования для конкретного языка. Это гарантирует, что создаваемый код будет соответствовать стилям кода вашего проекта.

* * *

## Встроенные

opencode поставляется с несколькими встроенными форматировщиками для популярных языков и платформ. Ниже приведен список форматтеров, поддерживаемых расширений файлов, а также необходимых команд или параметров конфигурации.

Formatter| Расширения| Требования  
---|---|---  
gofmt| .go| Доступна команда `gofmt`  
mix| .ex, .exs, .eex, .heex, .leex, .neex, .sface| Доступна команда `mix`  
prettier| .js, .jsx, .ts, .tsx, .html, .css, .md, .json, .yaml и [подробнее](https://prettier.io/docs/en/index.html)| Зависимость `prettier` в `package.json`  
biome| .js, .jsx, .ts, .tsx, .html, .css, .md, .json, .yaml и [подробнее](https://biomejs.dev/)| Конфигурационный файл `biome.json(c)`  
zig| .zig, .zon| Доступна команда `zig`  
clang-format| .c, .cpp, .h, .hpp, .ino и [подробнее](https://clang.llvm.org/docs/ClangFormat.html)| Конфигурационный файл `.clang-format`  
ktlint| .kt, .kts| Доступна команда `ktlint`  
ruff| .py, .pyi| Команда `ruff` доступна в конфигурации  
rustfmt| .rs| Доступна команда `rustfmt`  
cargofmt| .rs| Доступна команда `cargo fmt`  
uv| .py, .pyi| Доступна команда `uv`  
rubocop| .rb, .rake, .gemspec, .ru| Доступна команда `rubocop`  
standardrb| .rb, .rake, .gemspec, .ru| Доступна команда `standardrb`  
htmlbeautifier| .erb, .html.erb| Доступна команда `htmlbeautifier`  
air| .R| Доступна команда `air`  
dart| .dart| Доступна команда `dart`  
dfmt| .d| Доступна команда `dfmt`  
ocamlformat| .ml, .mli| Доступна команда `ocamlformat` и файл конфигурации `.ocamlformat`.  
terraform| .tf, .tfvars| Доступна команда `terraform`  
gleam| .gleam| Доступна команда `gleam`  
nixfmt| .nix| Доступна команда `nixfmt`  
shfmt| .sh, .bash| Доступна команда `shfmt`  
pint| .php| Зависимость `laravel/pint` в `composer.json`  
oxfmt (Experimental)| .js, .jsx, .ts, .tsx| Зависимость `oxfmt` в `package.json` и [экспериментальный флаг переменной окружения](/docs/cli/#experimental)  
ormolu| .hs| Доступна команда `ormolu`  
  
Поэтому, если ваш проект имеет `prettier` в вашем `package.json`, opencode автоматически будет использовать его.

* * *

## Настройка

Вы можете настроить форматтеры через раздел `formatter` в конфигурации opencode.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "formatter": {}
    }
```

Каждая конфигурация форматтера поддерживает следующее:

Свойство| Тип| Описание  
---|---|---  
`disabled`| boolean| Установите для этого параметра значение `true`, чтобы отключить форматтер.  
`command`| string[]| Команда для форматирования  
`environment`| объект| Переменные среды, которые необходимо установить при запуске средства форматирования  
`extensions`| string[]| Расширения файлов, которые должен обрабатывать этот форматтер  
  
Давайте посмотрим на несколько примеров.

* * *

### Отключение форматтеров

Чтобы глобально отключить **все** средства форматирования, установите для `formatter` значение `false`:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "formatter": false
    }
```

Чтобы отключить **конкретный** форматтер, установите для `disabled` значение `true`:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "formatter": {
        "prettier": {
          "disabled": true
        }
      }
    }
```

* * *

### Пользовательские форматтеры

Вы можете переопределить встроенные средства форматирования или добавить новые, указав команду, переменные среды и расширения файлов:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "formatter": {
        "prettier": {
          "command": ["npx", "prettier", "--write", "$FILE"],
          "environment": {
            "NODE_ENV": "development"
          },
          "extensions": [".js", ".ts", ".jsx", ".tsx"]
        },
        "custom-markdown-formatter": {
          "command": ["deno", "fmt", "$FILE"],
          "extensions": [".md"]
        }
      }
    }
```

Заполнитель **`$FILE`** в команде будет заменен путем к форматируемому файлу.

[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/formatters.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-24"></a>
---
url: https://opencode.ai/docs/ru/permissions/
---

# Разрешения

Контролируйте, какие действия требуют одобрения для выполнения.

opencode использует конфигурацию `permission`, чтобы решить, должно ли данное действие выполняться автоматически, запрашивать вас или блокироваться.

Начиная с `v1.1.1`, устаревшая логическая конфигурация `tools` устарела и была объединена с `permission`. Старая конфигурация `tools` по-прежнему поддерживается для обеспечения обратной совместимости.

* * *

## Действия

Каждое правило разрешения разрешается в одно из:

  * `"allow"` — запуск без одобрения
  * `"ask"` — запрос на одобрение
  * `"deny"` — заблокировать действие



* * *

## Конфигурация

Вы можете устанавливать разрешения глобально (с помощью `*`) и переопределять определенные инструменты.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "permission": {
        "*": "ask",
        "bash": "allow",
        "edit": "deny"
      }
    }
```

Вы также можете установить все разрешения одновременно:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "permission": "allow"
    }
```

* * *

## Детальные правила (синтаксис объекта)

Для большинства разрешений вы можете использовать объект для применения различных действий на основе входных данных инструмента.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "permission": {
        "bash": {
          "*": "ask",
          "git *": "allow",
          "npm *": "allow",
          "rm *": "deny",
          "grep *": "allow"
        },
        "edit": {
          "*": "deny",
          "packages/web/src/content/docs/*.mdx": "allow"
        }
      }
    }
```

Правила оцениваются по шаблону, при этом **выигрывает последнее совпадающее правило**. Обычно сначала ставится универсальное правило `"*"`, а после него — более конкретные правила.

### Подстановочные знаки

В шаблонах разрешений используется простое сопоставление с подстановочными знаками:

  * `*` соответствует нулю или более любого символа.
  * `?` соответствует ровно одному символу
  * Все остальные символы совпадают буквально



### Расширение домашнего каталога

Вы можете использовать `~` или `$HOME` в начале шаблона для ссылки на ваш домашний каталог. Это особенно полезно для правил `external_directory`.

  * `~/projects/*` -> `/Users/username/projects/*`
  * `$HOME/projects/*` -> `/Users/username/projects/*`
  * `~` -> `/Users/username`



### Внешние каталоги

Используйте `external_directory`, чтобы разрешить вызовы инструментов, затрагивающие пути за пределами рабочего каталога, в котором был запущен opencode. Это применимо к любому инструменту, который принимает путь в качестве входных данных (например, `read`, `edit`, `list`, `glob`, `grep` и многие команды `bash`).

Расширение дома (например, `~/...`) влияет только на запись шаблона. Он не делает внешний путь частью текущего рабочего пространства, поэтому пути за пределами рабочего каталога все равно должны быть разрешены через `external_directory`.

Например, это позволяет получить доступ ко всему, что находится под `~/projects/personal/`:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "permission": {
        "external_directory": {
          "~/projects/personal/**": "allow"
        }
      }
    }
```

Любой каталог, разрешенный здесь, наследует те же настройки по умолчанию, что и текущая рабочая область. Поскольку для `read` по умолчанию установлено значение `allow`, чтение также разрешено для записей под `external_directory`, если оно не переопределено. Добавьте явные правила, когда инструмент должен быть ограничен в этих путях, например, блокировать редактирование при сохранении чтения:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "permission": {
        "external_directory": {
          "~/projects/personal/**": "allow"
        },
        "edit": {
          "~/projects/personal/**": "deny"
        }
      }
    }
```

Держите список сосредоточенным на доверенных путях и добавляйте дополнительные правила разрешения или запрета по мере необходимости для других инструментов (например, `bash`).

* * *

## Доступные разрешения

Разрешения opencode привязаны к имени инструмента, а также к нескольким мерам безопасности:

  * `read` — чтение файла (соответствует пути к файлу)
  * `edit` — все модификации файлов (охватывает `edit`, `write`, `patch`, `multiedit`)
  * `glob` — подстановка файла (соответствует шаблону подстановки)
  * `grep` — поиск по контенту (соответствует шаблону регулярного выражения)
  * `list` — список файлов в каталоге (соответствует пути к каталогу)
  * `bash` — запуск shell-команд (соответствует проанализированным командам, например `git status --porcelain`)
  * `task` — запуск субагентов (соответствует типу субагента)
  * `skill` — загрузка навыка (соответствует названию навыка)
  * `lsp` — выполнение запросов LSP (в настоящее время не детализированных)
  * `todoread`, `todowrite` — чтение/обновление списка дел.
  * `webfetch` — получение URL-адреса (соответствует URL-адресу)
  * `websearch`, `codesearch` — поиск в сети/коде (соответствует запросу)
  * `external_directory` — срабатывает, когда инструмент касается путей за пределами рабочего каталога проекта.
  * `doom_loop` — срабатывает, когда один и тот же вызов инструмента повторяется 3 раза с одинаковым вводом.



* * *

## По умолчанию

Если вы ничего не укажете, opencode запустится с разрешенных значений по умолчанию:

  * Большинство разрешений по умолчанию имеют значение `"allow"`.
  * `doom_loop` и `external_directory` по умолчанию равны `"ask"`.
  * `read` — это `"allow"`, но файлы `.env` по умолчанию запрещены:



opencode.json
```
{
      "permission": {
        "read": {
          "*": "allow",
          "*.env": "deny",
          "*.env.*": "deny",
          "*.env.example": "allow"
        }
      }
    }
```

* * *

## Что означает «ask»

Когда opencode запрашивает одобрение, пользовательский интерфейс предлагает три результата:

  * `once` — утвердить только этот запрос
  * `always` — одобрять будущие запросы, соответствующие предложенным шаблонам (до конца текущего сеанса opencode).
  * `reject` — отклонить запрос



Набор шаблонов, которые одобрит `always`, предоставляется инструментом (например, разрешения bash обычно включают в белый список безопасный префикс команды, такой как `git status*`).

* * *

## Агенты

Вы можете переопределить разрешения для каждого агента. Разрешения агента объединяются с глобальной конфигурацией, и правила агента имеют приоритет. [Подробнее](/docs/agents#permissions) о разрешениях агента.

Заметка

Более подробные примеры сопоставления с образцом см. в разделе Детальные правила (синтаксис объекта) выше.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "permission": {
        "bash": {
          "*": "ask",
          "git *": "allow",
          "git commit *": "deny",
          "git push *": "deny",
          "grep *": "allow"
        }
      },
      "agent": {
        "build": {
          "permission": {
            "bash": {
              "*": "ask",
              "git *": "allow",
              "git commit *": "ask",
              "git push *": "deny",
              "grep *": "allow"
            }
          }
        }
      }
    }
```

Вы также можете настроить разрешения агента в Markdown:

~/.config/opencode/agents/review.md
```
---
    description: Code review without edits
    mode: subagent
    permission:
      edit: deny
      bash: ask
      webfetch: deny
    ---
    
    
    Only analyze code and suggest changes.
```

Совет

Используйте сопоставление с образцом для команд с аргументами. `"grep *"` разрешает `grep pattern file.txt`, а сам `"grep"` блокирует его. Такие команды, как `git status`, работают по умолчанию, но требуют явного разрешения (например, `"git status *"`) при передаче аргументов.

[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/permissions.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-25"></a>
---
url: https://opencode.ai/docs/ru/lsp/
---

# LSP-серверы

opencode интегрируется с вашими серверами LSP.

opencode интегрируется с вашим протоколом языкового сервера (LSP), чтобы помочь LLM взаимодействовать с вашей кодовой базой. Он использует диагностику для предоставления обратной связи LLM.

* * *

## Встроенные

opencode поставляется с несколькими встроенными LSP-серверами для популярных языков:

LSP Server| Extensions| Requirements  
---|---|---  
astro| .astro| Автоматически устанавливается для проектов Astro  
bash| .sh, .bash, .zsh, .ksh| Автоматически устанавливает bash-language-server  
clangd| .c, .cpp, .cc, .cxx, .c++, .h, .hpp, .hh, .hxx, .h++| Автоматически устанавливается для проектов C/C++  
csharp| .cs| `.NET SDK` установлен  
clojure-lsp| .clj, .cljs, .cljc, .edn| `clojure-lsp` команда доступна  
dart| .dart| `dart` команда доступна  
deno| .ts, .tsx, .js, .jsx, .mjs| `deno` команда доступна (автоматически обнаруживает deno.json/deno.jsonc)  
elixir-ls| .ex, .exs| `elixir` команда доступна  
eslint| .ts, .tsx, .js, .jsx, .mjs, .cjs, .mts, .cts, .vue| `eslint` зависимость в проекте  
fsharp| .fs, .fsi, .fsx, .fsscript| `.NET SDK` установлен  
gleam| .gleam| `gleam` команда доступна  
gopls| .go| `go` команда доступна  
hls| .hs, .lhs| `haskell-language-server-wrapper` команда доступна  
jdtls| .java| `Java SDK (version 21+)` установлен  
kotlin-ls| .kt, .kts| Автоматически устанавливается для проектов Kotlin  
lua-ls| .lua| Автоматически устанавливается для проектов Lua  
nixd| .nix| `nixd` команда доступна  
ocaml-lsp| .ml, .mli| `ocamllsp` команда доступна  
oxlint| .ts, .tsx, .js, .jsx, .mjs, .cjs, .mts, .cts, .vue, .astro, .svelte| `oxlint` зависимость в проекте  
php intelephense| .php| Автоматически устанавливается для проектов PHP  
prisma| .prisma| `prisma` команда доступна  
pyright| .py, .pyi| `pyright` зависимость установлена  
ruby-lsp (rubocop)| .rb, .rake, .gemspec, .ru| `ruby` и `gem` команды доступны  
rust| .rs| `rust-analyzer` команда доступна  
sourcekit-lsp| .swift, .objc, .objcpp| `swift` установлен (`xcode` на macOS)  
svelte| .svelte| Автоматически устанавливается для проектов Svelte  
terraform| .tf, .tfvars| Автоматически устанавливается из релизов GitHub  
tinymist| .typ, .typc| Автоматически устанавливается из релизов GitHub  
typescript| .ts, .tsx, .js, .jsx, .mjs, .cjs, .mts, .cts| `typescript` зависимость в проекте  
vue| .vue| Автоматически устанавливается для проектов Vue  
yaml-ls| .yaml, .yml| Автоматически устанавливает Red Hat yaml-language-server  
zls| .zig, .zon| `zig` команда доступна  
  
Серверы LSP автоматически включаются при обнаружении одного из указанных выше расширений файлов и выполнении требований.

Заметка

Вы можете отключить автоматическую загрузку LSP-сервера, установив для переменной среды `OPENCODE_DISABLE_LSP_DOWNLOAD` значение `true`.

* * *

## Как это работает

Когда opencode открывает файл, он:

  1. Проверяет расширение файла на всех включенных серверах LSP.
  2. Запускает соответствующий сервер LSP, если он еще не запущен.



* * *

## Настройка

Вы можете настроить серверы LSP через раздел `lsp` в конфигурации opencode.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "lsp": {}
    }
```

Каждый LSP-сервер поддерживает следующее:

Свойство| Тип| Описание  
---|---|---  
`disabled`| boolean| Установите для этого параметра значение `true`, чтобы отключить сервер LSP.  
`command`| string[]| Команда запуска LSP-сервера  
`extensions`| string[]| Расширения файлов, которые должен обрабатывать этот сервер LSP  
`env`| object| Переменные среды, которые нужно установить при запуске сервера  
`initialization`| object| Параметры инициализации для отправки на сервер LSP  
  
Давайте посмотрим на несколько примеров.

* * *

### Переменные среды

Используйте свойство `env` для установки переменных среды при запуске сервера LSP:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "lsp": {
        "rust": {
          "env": {
            "RUST_LOG": "debug"
          }
        }
      }
    }
```

* * *

### Параметры инициализации

Используйте свойство `initialization` для передачи параметров инициализации на LSP-сервер. Это настройки, специфичные для сервера, отправляемые во время запроса LSP `initialize`:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "lsp": {
        "typescript": {
          "initialization": {
            "preferences": {
              "importModuleSpecifierPreference": "relative"
            }
          }
        }
      }
    }
```

Заметка

Параметры инициализации зависят от сервера LSP. Проверьте документацию вашего LSP-сервера на наличие доступных опций.

* * *

### Отключение LSP-серверов

Чтобы отключить **все** LSP-серверы глобально, установите для `lsp` значение `false`:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "lsp": false
    }
```

Чтобы отключить **конкретный** LSP-сервер, установите для `disabled` значение `true`:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "lsp": {
        "typescript": {
          "disabled": true
        }
      }
    }
```

* * *

### Пользовательские LSP-серверы

Вы можете добавить собственные LSP-серверы, указав команду и расширения файлов:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "lsp": {
        "custom-lsp": {
          "command": ["custom-lsp-server", "--stdio"],
          "extensions": [".custom"]
        }
      }
    }
```

* * *

## Дополнительная информация

### PHP Intelephense

PHP Intelephense предлагает дополнительные функции через лицензионный ключ. Вы можете предоставить лицензионный ключ, поместив (только) ключ в текстовый файл по адресу:

  * В macOS/Linux: `$HOME/intelephense/license.txt`
  * В Windows: `%USERPROFILE%/intelephense/license.txt`



Файл должен содержать только лицензионный ключ без какого-либо дополнительного содержимого.

[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/lsp.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-26"></a>
---
url: https://opencode.ai/docs/ru/mcp-servers/
---

# MCP-серверы

Добавьте локальные и удаленные инструменты MCP.

Вы можете добавить внешние инструменты в opencode, используя _Model Context Protocol_ или MCP. opencode поддерживает как локальные, так и удаленные серверы.

После добавления инструменты MCP автоматически становятся доступными для LLM наряду со встроенными инструментами.

* * *

#### Предостережения

Когда вы используете сервер MCP, он добавляет контекст. Это может быстро сложиться, если у вас много инструментов. Поэтому мы рекомендуем быть осторожными с тем, какие серверы MCP вы используете.

Совет

Серверы MCP добавляются к вашему контексту, поэтому будьте осторожны с тем, какие из них вы включаете.

Некоторые серверы MCP, такие как сервер MCP GitHub, имеют тенденцию добавлять много токенов и могут легко превысить ограничение контекста.

* * *

## Включение

Вы можете определить серверы MCP в своем [opencode Config](https://opencode.ai/docs/config/) в разделе `mcp`. Добавьте каждому MCP уникальное имя. Вы можете обратиться к этому MCP по имени при запросе LLM.

opencode.jsonc
```
{
      "$schema": "https://opencode.ai/config.json",
      "mcp": {
        "name-of-mcp-server": {
          // ...
          "enabled": true,
        },
        "name-of-other-mcp-server": {
          // ...
        },
      },
    }
```

Вы также можете отключить сервер, установив для `enabled` значение `false`. Это полезно, если вы хотите временно отключить сервер, не удаляя его из конфигурации.

* * *

### Переопределение удаленных настроек по умолчанию

Организации могут предоставлять серверы MCP по умолчанию через свою конечную точку `.well-known/opencode`. Эти серверы могут быть отключены по умолчанию, что позволяет пользователям выбирать те, которые им нужны.

Чтобы включить определенный сервер из удаленной конфигурации вашей организации, добавьте его в локальную конфигурацию с помощью `enabled: true`:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "mcp": {
        "jira": {
          "type": "remote",
          "url": "https://jira.example.com/mcp",
          "enabled": true
        }
      }
    }
```

Значения вашей локальной конфигурации переопределяют удаленные значения по умолчанию. Дополнительную информацию см. в [приоритете конфигурации](/docs/config#precedence-order).

* * *

## Локальные

Добавьте локальные серверы MCP с помощью `type` в `"local"` внутри объекта MCP.

opencode.jsonc
```
{
      "$schema": "https://opencode.ai/config.json",
      "mcp": {
        "my-local-mcp-server": {
          "type": "local",
          // Or ["bun", "x", "my-mcp-command"]
          "command": ["npx", "-y", "my-mcp-command"],
          "enabled": true,
          "environment": {
            "MY_ENV_VAR": "my_env_var_value",
          },
        },
      },
    }
```

Эта команда запускает локальный сервер MCP. Вы также можете передать список переменных среды.

Например, вот как можно добавить тестовый сервер [`@modelcontextprotocol/server-everything`](https://www.npmjs.com/package/@modelcontextprotocol/server-everything) MCP.

opencode.jsonc
```
{
      "$schema": "https://opencode.ai/config.json",
      "mcp": {
        "mcp_everything": {
          "type": "local",
          "command": ["npx", "-y", "@modelcontextprotocol/server-everything"],
        },
      },
    }
```

И чтобы использовать его, добавьте `use the mcp_everything tool` в свои подсказки.
```
use the mcp_everything tool to add the number 3 and 4
```

* * *

#### Параметры

Вот все варианты настройки локального сервера MCP.

Вариант| Тип| Обязательный| Описание  
---|---|---|---  
`type`| Строка| Да| Тип подключения к серверу MCP должен быть `"local"`.  
`command`| Массив| Да| Команда и аргументы для запуска сервера MCP.  
`environment`| Объект| | Переменные среды, которые необходимо установить при запуске сервера.  
`enabled`| логическое значение| | Включите или отключите сервер MCP при запуске.  
`timeout`| Число| | Тайм-аут в мс для получения инструментов с сервера MCP. По умолчанию 5000 (5 секунд).  
  
* * *

