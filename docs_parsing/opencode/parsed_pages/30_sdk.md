<a id="page-30"></a>
---
url: https://opencode.ai/docs/ru/sdk/
---

# SDK

Типобезопасный JS-клиент для сервера opencode.

SDK JS/TS с открытым кодом предоставляет типобезопасный клиент для взаимодействия с сервером. Используйте его для создания интеграции и программного управления открытым кодом.

[Узнайте больше](/docs/server) о том, как работает сервер. Примеры можно найти в [projects](/docs/ecosystem#projects), созданном сообществом.

* * *

## Установить

Установите SDK из npm:

Окно терминала
```
npm install @opencode-ai/sdk
```

* * *

## Создать клиента

Создайте экземпляр opencode:
```
import { createOpencode } from "@opencode-ai/sdk"
    
    
    const { client } = await createOpencode()
```

Это запускает и сервер, и клиент.

#### Параметры

Вариант| Тип| Описание| По умолчанию  
---|---|---|---  
`hostname`| `string`| Server hostname| `127.0.0.1`  
`port`| `number`| Server port| `4096`  
`signal`| `AbortSignal`| Abort signal for cancellation| `undefined`  
`timeout`| `number`| Timeout in ms for server start| `5000`  
`config`| `Config`| Configuration object| `{}`  
  
* * *

## Конфигурация

Вы можете передать объект конфигурации для настройки поведения. Экземпляр по-прежнему получает ваш `opencode.json`, но вы можете переопределить или добавить встроенную конфигурацию:
```
import { createOpencode } from "@opencode-ai/sdk"
    
    
    const opencode = await createOpencode({
      hostname: "127.0.0.1",
      port: 4096,
      config: {
        model: "anthropic/claude-3-5-sonnet-20241022",
      },
    })
    
    
    console.log(`Server running at ${opencode.server.url}`)
    
    
    opencode.server.close()
```

## Только клиент

Если у вас уже есть работающий экземпляр opencode, вы можете создать экземпляр клиента для подключения к нему:
```
import { createOpencodeClient } from "@opencode-ai/sdk"
    
    
    const client = createOpencodeClient({
      baseUrl: "http://localhost:4096",
    })
```

#### Параметры

Вариант| Тип| Описание| По умолчанию  
---|---|---|---  
`baseUrl`| `string`| URL of the server| `http://localhost:4096`  
`fetch`| `function`| Custom fetch implementation| `globalThis.fetch`  
`parseAs`| `string`| Response parsing method| `auto`  
`responseStyle`| `string`| Return style: `data` or `fields`| `fields`  
`throwOnError`| `boolean`| Throw errors instead of return| `false`  
  
* * *

## Типы

SDK включает определения TypeScript для всех типов API. Импортируйте их напрямую:
```
import type { Session, Message, Part } from "@opencode-ai/sdk"
```

Все типы генерируются на основе спецификации OpenAPI сервера и доступны в файле [types](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts).

* * *

## Ошибки

SDK может выдавать ошибки, которые вы можете отловить и обработать:
```
try {
      await client.session.get({ path: { id: "invalid-id" } })
    } catch (error) {
      console.error("Failed to get session:", (error as Error).message)
    }
```

* * *

## API

SDK предоставляет все серверные API через типобезопасный клиент.

* * *

### Глобальный

Метод| Описание| Ответ  
---|---|---  
`global.health()`| Check server health and version| `{ healthy: true, version: string }`  
  
* * *

#### Примеры
```
const health = await client.global.health()
    console.log(health.data.version)
```

* * *

### Приложение

Метод| Описание| Ответ  
---|---|---  
`app.log()`| Write a log entry| `boolean`  
`app.agents()`| List all available agents| [`Agent[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
  
* * *

#### Примеры
```
// Write a log entry
    await client.app.log({
      body: {
        service: "my-app",
        level: "info",
        message: "Operation completed",
      },
    })
    
    
    // List available agents
    const agents = await client.app.agents()
```

* * *

### Проект

Метод| Описание| Ответ  
---|---|---  
`project.list()`| List all projects| [`Project[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`project.current()`| Get current project| [`Project`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
  
* * *

#### Примеры
```
// List all projects
    const projects = await client.project.list()
    
    
    // Get current project
    const currentProject = await client.project.current()
```

* * *

### Путь

Метод| Описание| Ответ  
---|---|---  
`path.get()`| Get current path| [`Path`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
  
* * *

#### Примеры
```
// Get current path information
    const pathInfo = await client.path.get()
```

* * *

### Конфигурация

Метод| Описание| Ответ  
---|---|---  
`config.get()`| Get config info| [`Config`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`config.providers()`| List providers and default models| `{ providers: `[`Provider[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`, default: { [key: string]: string } }`  
  
* * *

#### Примеры
```
const config = await client.config.get()
    
    
    const { providers, default: defaults } = await client.config.providers()
```

* * *

### Сессии

Метод| Описание| Примечания  
---|---|---  
`session.list()`| List sessions| Returns [`Session[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`session.get({ path })`| Get session| Returns [`Session`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`session.children({ path })`| List child sessions| Returns [`Session[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`session.create({ body })`| Create session| Returns [`Session`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`session.delete({ path })`| Delete session| Returns `boolean`  
`session.update({ path, body })`| Update session properties| Returns [`Session`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`session.init({ path, body })`| Analyze app and create `AGENTS.md`| Returns `boolean`  
`session.abort({ path })`| Abort a running session| Returns `boolean`  
`session.share({ path })`| Share session| Returns [`Session`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`session.unshare({ path })`| Unshare session| Returns [`Session`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`session.summarize({ path, body })`| Summarize session| Returns `boolean`  
`session.messages({ path })`| List messages in a session| Returns `{ info: `[`Message`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`, parts: `[`Part[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`}[]`  
`session.message({ path })`| Get message details| Returns `{ info: `[`Message`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`, parts: `[`Part[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`}`  
`session.prompt({ path, body })`| Send prompt message| `body.noReply: true` returns UserMessage (context only). Default returns [`AssistantMessage`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts) with AI response  
`session.command({ path, body })`| Send command to session| Returns `{ info: `[`AssistantMessage`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`, parts: `[`Part[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`}`  
`session.shell({ path, body })`| Run a shell command| Returns [`AssistantMessage`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`session.revert({ path, body })`| Revert a message| Returns [`Session`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`session.unrevert({ path })`| Restore reverted messages| Returns [`Session`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`postSessionByIdPermissionsByPermissionId({ path, body })`| Respond to a permission request| Returns `boolean`  
  
* * *

#### Примеры
```
// Create and manage sessions
    const session = await client.session.create({
      body: { title: "My session" },
    })
    
    
    const sessions = await client.session.list()
    
    
    // Send a prompt message
    const result = await client.session.prompt({
      path: { id: session.id },
      body: {
        model: { providerID: "anthropic", modelID: "claude-3-5-sonnet-20241022" },
        parts: [{ type: "text", text: "Hello!" }],
      },
    })
    
    
    // Inject context without triggering AI response (useful for plugins)
    await client.session.prompt({
      path: { id: session.id },
      body: {
        noReply: true,
        parts: [{ type: "text", text: "You are a helpful assistant." }],
      },
    })
```

* * *

### Файлы

Метод| Описание| Ответ  
---|---|---  
`find.text({ query })`| Search for text in files| Array of match objects with `path`, `lines`, `line_number`, `absolute_offset`, `submatches`  
`find.files({ query })`| Find files and directories by name| `string[]` (paths)  
`find.symbols({ query })`| Find workspace symbols| [`Symbol[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`file.read({ query })`| Read a file| `{ type: "raw" | "patch", content: string }`  
`file.status({ query? })`| Get status for tracked files| [`File[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
  
`find.files` поддерживает несколько дополнительных полей запроса:

  * `type`: `"file"` или `"directory"`
  * `directory`: переопределить корень проекта для поиска.
  * `limit`: максимальное количество результатов (1–200)



* * *

#### Примеры
```
// Search and read files
    const textResults = await client.find.text({
      query: { pattern: "function.*opencode" },
    })
    
    
    const files = await client.find.files({
      query: { query: "*.ts", type: "file" },
    })
    
    
    const directories = await client.find.files({
      query: { query: "packages", type: "directory", limit: 20 },
    })
    
    
    const content = await client.file.read({
      query: { path: "src/index.ts" },
    })
```

* * *

### TUI

Метод| Описание| Ответ  
---|---|---  
`tui.appendPrompt({ body })`| Append text to the prompt| `boolean`  
`tui.openHelp()`| Open the help dialog| `boolean`  
`tui.openSessions()`| Open the session selector| `boolean`  
`tui.openThemes()`| Open the theme selector| `boolean`  
`tui.openModels()`| Open the model selector| `boolean`  
`tui.submitPrompt()`| Submit the current prompt| `boolean`  
`tui.clearPrompt()`| Clear the prompt| `boolean`  
`tui.executeCommand({ body })`| Execute a command| `boolean`  
`tui.showToast({ body })`| Show toast notification| `boolean`  
  
* * *

#### Примеры
```
// Control TUI interface
    await client.tui.appendPrompt({
      body: { text: "Add this to prompt" },
    })
    
    
    await client.tui.showToast({
      body: { message: "Task completed", variant: "success" },
    })
```

* * *

### Аутентификация

Метод| Описание| Ответ  
---|---|---  
`auth.set({ ... })`| Set authentication credentials| `boolean`  
  
* * *

#### Примеры
```
await client.auth.set({
      path: { id: "anthropic" },
      body: { type: "api", key: "your-api-key" },
    })
```

* * *

### События

Метод| Описание| Ответ  
---|---|---  
`event.subscribe()`| Server-sent events stream| Server-sent events stream  
  
* * *

#### Примеры
```
// Listen to real-time events
    const events = await client.event.subscribe()
    for await (const event of events.stream) {
      console.log("Event:", event.type, event.properties)
    }
```

[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/sdk.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.
