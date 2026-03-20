## Удаленные

Добавьте удаленные серверы MCP, установив для `type` значение `"remote"`.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "mcp": {
        "my-remote-mcp": {
          "type": "remote",
          "url": "https://my-mcp-server.com",
          "enabled": true,
          "headers": {
            "Authorization": "Bearer MY_API_KEY"
          }
        }
      }
    }
```

`url` — это URL-адрес удаленного сервера MCP, а с помощью параметра `headers` вы можете передать список заголовков.

* * *

#### Параметры

Вариант| Тип| Обязательный| Описание  
---|---|---|---  
`type`| Строка| Да| Тип подключения к серверу MCP должен быть `"remote"`.  
`url`| Строка| Да| URL-адрес удаленного сервера MCP.  
`enabled`| логическое значение| | Включите или отключите сервер MCP при запуске.  
`headers`| Объект| | Заголовки для отправки с запросом.  
`oauth`| Объект| | Конфигурация аутентификации OAuth. См. раздел OAuth ниже.  
`timeout`| Число| | Тайм-аут в мс для получения инструментов с сервера MCP. По умолчанию 5000 (5 секунд).  
  
* * *

## OAuth

opencode автоматически обрабатывает аутентификацию OAuth для удаленных серверов MCP. Когда серверу требуется аутентификация, opencode:

  1. Обнаружьте ответ 401 и инициируйте поток OAuth.
  2. Используйте **Динамическую регистрацию клиента (RFC 7591)** , если это поддерживается сервером.
  3. Надежно храните токены для будущих запросов



* * *

### Автоматически

Для большинства серверов MCP с поддержкой OAuth не требуется никакой специальной настройки. Просто настройте удаленный сервер:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "mcp": {
        "my-oauth-server": {
          "type": "remote",
          "url": "https://mcp.example.com/mcp"
        }
      }
    }
```

Если сервер требует аутентификации, opencode предложит вам пройти аутентификацию при первой попытке его использования. Если нет, вы можете вручную запустить поток  с помощью `opencode mcp auth <server-name>`.

* * *

### Предварительная регистрация

Если у вас есть учетные данные клиента от поставщика сервера MCP, вы можете их настроить:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "mcp": {
        "my-oauth-server": {
          "type": "remote",
          "url": "https://mcp.example.com/mcp",
          "oauth": {
            "clientId": "{env:MY_MCP_CLIENT_ID}",
            "clientSecret": "{env:MY_MCP_CLIENT_SECRET}",
            "scope": "tools:read tools:execute"
          }
        }
      }
    }
```

* * *

### Аутентификация

Вы можете вручную активировать аутентификацию или управлять учетными данными.

Аутентификация с помощью определенного сервера MCP:

Окно терминала
```
opencode mcp auth my-oauth-server
```

Перечислите все серверы MCP и их статус аутентификации:

Окно терминала
```
opencode mcp list
```

Удалить сохраненные учетные данные:

Окно терминала
```
opencode mcp logout my-oauth-server
```

Команда `mcp auth` откроет ваш браузер для авторизации. После того как вы авторизуетесь, opencode надежно сохранит токены в `~/.local/share/opencode/mcp-auth.json`.

* * *

#### Отключение OAuth

Если вы хотите отключить автоматический OAuth для сервера (например, для серверов, которые вместо этого используют ключи API), установите для `oauth` значение `false`:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "mcp": {
        "my-api-key-server": {
          "type": "remote",
          "url": "https://mcp.example.com/mcp",
          "oauth": false,
          "headers": {
            "Authorization": "Bearer {env:MY_API_KEY}"
          }
        }
      }
    }
```

* * *

#### Параметры OAuth

Вариант| Тип| Описание  
---|---|---  
`oauth`| Object | false| Объект конфигурации OAuth или `false`, чтобы отключить автообнаружение OAuth.  
`clientId`| String| OAuth client ID. Если не указан, будет выполнена динамическая регистрация клиента.  
`clientSecret`| String| OAuth client secret, если этого требует сервер авторизации.  
`scope`| String| OAuth scopes для запроса во время авторизации.  
  
#### Отладка

Если удаленный сервер MCP не может аутентифицироваться, вы можете диагностировать проблемы с помощью:

Окно терминала
```
# View auth status for all OAuth-capable servers
    opencode mcp auth list
    
    
    # Debug connection and OAuth flow for a specific server
    opencode mcp debug my-oauth-server
```

Команда `mcp debug` показывает текущий статус аутентификации, проверяет соединение HTTP и пытается выполнить поток обнаружения OAuth.

* * *

## Управление

Ваши MCP доступны в виде инструментов opencode наряду со встроенными инструментами. Таким образом, вы можете управлять ими через конфигурацию opencode, как и любым другим инструментом.

* * *

### Глобально

Это означает, что вы можете включать или отключать их глобально.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "mcp": {
        "my-mcp-foo": {
          "type": "local",
          "command": ["bun", "x", "my-mcp-command-foo"]
        },
        "my-mcp-bar": {
          "type": "local",
          "command": ["bun", "x", "my-mcp-command-bar"]
        }
      },
      "tools": {
        "my-mcp-foo": false
      }
    }
```

Мы также можем использовать шаблон glob, чтобы отключить все соответствующие MCP.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "mcp": {
        "my-mcp-foo": {
          "type": "local",
          "command": ["bun", "x", "my-mcp-command-foo"]
        },
        "my-mcp-bar": {
          "type": "local",
          "command": ["bun", "x", "my-mcp-command-bar"]
        }
      },
      "tools": {
        "my-mcp*": false
      }
    }
```

Здесь мы используем шаблон `my-mcp*` для отключения всех MCP.

* * *

### Для каждого агента

Если у вас большое количество серверов MCP, вы можете включить их только для каждого агента и отключить глобально. Для этого:

  1. Отключите его как инструмент глобально.
  2. В вашей [конфигурации агента](/docs/agents#tools) включите сервер MCP в качестве инструмента.



opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "mcp": {
        "my-mcp": {
          "type": "local",
          "command": ["bun", "x", "my-mcp-command"],
          "enabled": true
        }
      },
      "tools": {
        "my-mcp*": false
      },
      "agent": {
        "my-agent": {
          "tools": {
            "my-mcp*": true
          }
        }
      }
    }
```

* * *

#### Glob-шаблоны

Шаблон glob использует простые шаблоны подстановки регулярных выражений:

  * `*` соответствует нулю или более любого символа (например, `"my-mcp*"` соответствует `my-mcp_search`, `my-mcp_list` и т. д.).
  * `?` соответствует ровно одному символу.
  * Все остальные символы совпадают буквально



Заметка

Инструменты сервера MCP регистрируются с именем сервера в качестве префикса, поэтому, чтобы отключить все инструменты для сервера, просто используйте:
```
"mymcpservername_*": false
```

* * *

## Примеры

Ниже приведены примеры некоторых распространенных серверов MCP. Вы можете отправить PR, если хотите документировать другие серверы.

* * *

### Sentry

Добавьте [сервер Sentry MCP](https://mcp.sentry.dev) для взаимодействия с вашими проектами и проблемами Sentry.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "mcp": {
        "sentry": {
          "type": "remote",
          "url": "https://mcp.sentry.dev/mcp",
          "oauth": {}
        }
      }
    }
```

После добавления конфигурации пройдите аутентификацию с помощью Sentry:

Окно терминала
```
opencode mcp auth sentry
```

Откроется окно браузера для завершения процесса OAuth и подключения opencode к вашей учетной записи Sentry.

После аутентификации вы можете использовать инструменты Sentry в своих подсказках для запроса данных о проблемах, проектах и ​​ошибках.
```
Show me the latest unresolved issues in my project. use sentry
```

* * *

### Context7

Добавьте [сервер Context7 MCP](https://github.com/upstash/context7) для поиска в документах.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "mcp": {
        "context7": {
          "type": "remote",
          "url": "https://mcp.context7.com/mcp"
        }
      }
    }
```

Если вы зарегистрировали бесплатную учетную запись, вы можете использовать свой ключ API и получить более высокие ограничения скорости.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "mcp": {
        "context7": {
          "type": "remote",
          "url": "https://mcp.context7.com/mcp",
          "headers": {
            "CONTEXT7_API_KEY": "{env:CONTEXT7_API_KEY}"
          }
        }
      }
    }
```

Здесь мы предполагаем, что у вас установлена ​​переменная среды `CONTEXT7_API_KEY`.

Добавьте `use context7` в запросы на использование сервера Context7 MCP.
```
Configure a Cloudflare Worker script to cache JSON API responses for five minutes. use context7
```

Альтернативно вы можете добавить что-то подобное в свой файл [AGENTS.md](/docs/rules/).

AGENTS.md
```
When you need to search docs, use `context7` tools.
```

* * *

### Grep by Vercel

Добавьте сервер MCP [Grep от Vercel](https://grep.app) для поиска по фрагментам кода на GitHub.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "mcp": {
        "gh_grep": {
          "type": "remote",
          "url": "https://mcp.grep.app"
        }
      }
    }
```

Поскольку мы назвали наш сервер MCP `gh_grep`, вы можете добавить `use the gh_grep tool` в свои запросы, чтобы агент мог его использовать.
```
What's the right way to set a custom domain in an SST Astro component? use the gh_grep tool
```

Альтернативно вы можете добавить что-то подобное в свой файл [AGENTS.md](/docs/rules/).

AGENTS.md
```
If you are unsure how to do something, use `gh_grep` to search code examples from GitHub.
```

[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/mcp-servers.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-27"></a>
---
url: https://opencode.ai/docs/ru/acp/
---

# Поддержка ACP

Используйте opencode в любом ACP-совместимом редакторе.

opencode поддерживает [Agent Client Protocol](https://agentclientprotocol.com) (ACP), что позволяет использовать его непосредственно в совместимых редакторах и IDE.

Совет

Список редакторов и инструментов, поддерживающих ACP, можно найти в [отчете о ходе работы ACP](https://zed.dev/blog/acp-progress-report#available-now).

ACP — это открытый протокол, который стандартизирует взаимодействие между редакторами кода и ИИ-агентами.

* * *

## Настройка

Чтобы использовать opencode через ACP, настройте свой редактор для запуска команды `opencode acp`.

Команда запускает opencode как ACP-совместимый подпроцесс, который взаимодействует с вашим редактором через JSON-RPC через stdio.

Ниже приведены примеры популярных редакторов, поддерживающих ACP.

* * *

### Zed

Добавьте в конфигурацию [Zed](https://zed.dev) (`~/.config/zed/settings.json`):

~/.config/zed/settings.json
```
{
      "agent_servers": {
        "OpenCode": {
          "command": "opencode",
          "args": ["acp"]
        }
      }
    }
```

Чтобы открыть его, используйте действие `agent: new thread` в **Палитре команд**.

Вы также можете привязать сочетание клавиш, отредактировав свой `keymap.json`:

keymap.json
```
[
      {
        "bindings": {
          "cmd-alt-o": [
            "agent::NewExternalAgentThread",
            {
              "agent": {
                "custom": {
                  "name": "OpenCode",
                  "command": {
                    "command": "opencode",
                    "args": ["acp"]
                  }
                }
              }
            }
          ]
        }
      }
    ]
```

* * *

### IDE JetBrains

Добавьте в свою [JetBrains IDE](https://www.jetbrains.com/) acp.json в соответствии с [документацией](https://www.jetbrains.com/help/ai-assistant/acp.html):

acp.json
```
{
      "agent_servers": {
        "OpenCode": {
          "command": "/absolute/path/bin/opencode",
          "args": ["acp"]
        }
      }
    }
```

Чтобы открыть его, используйте новый агент opencode в селекторе агентов AI Chat.

* * *

### Avante.nvim

Добавьте в свою конфигурацию [Avante.nvim](https://github.com/yetone/avante.nvim):
```
{
      acp_providers = {
        ["opencode"] = {
          command = "opencode",
          args = { "acp" }
        }
      }
    }
```

Если вам нужно передать переменные среды:
```
{
      acp_providers = {
        ["opencode"] = {
          command = "opencode",
          args = { "acp" },
          env = {
            OPENCODE_API_KEY = os.getenv("OPENCODE_API_KEY")
          }
        }
      }
    }
```

* * *

### CodeCompanion.nvim

Чтобы использовать opencode в качестве агента ACP в [CodeCompanion.nvim](https://github.com/olimorris/codecompanion.nvim), добавьте в конфигурацию Neovim следующее:
```
require("codecompanion").setup({
      interactions = {
        chat = {
          adapter = {
            name = "opencode",
            model = "claude-sonnet-4",
          },
        },
      },
    })
```

Эта конфигурация настраивает CodeCompanion для использования opencode в качестве агента ACP для чата.

Если вам нужно передать переменные среды (например, `OPENCODE_API_KEY`), обратитесь к разделу [Настройка адаптеров: переменные среды](https://codecompanion.olimorris.dev/getting-started#setting-an-api-key) в документации CodeCompanion.nvim для получения полной информации.

## Поддержка

opencode через ACP работает так же, как и в терминале. Поддерживаются все функции:

Заметка

Некоторые встроенные команды слэша, такие как `/undo` и `/redo`, в настоящее время не поддерживаются.

  * Встроенные инструменты (файловые операции, команды терминала и т. д.)
  * Пользовательские инструменты и команды слэша
  * Серверы MCP, настроенные в вашей конфигурации opencode
  * Правила для конкретного проекта из `AGENTS.md`
  * Пользовательские форматтеры и линтеры
  * Агенты и система разрешений



[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/acp.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-28"></a>
---
url: https://opencode.ai/docs/ru/skills/
---

# Навыки агента

Определите повторно используемое поведение с помощью определений SKILL.md

Навыки агента позволяют opencode обнаруживать многократно используемые инструкции из вашего репозитория или домашнего каталога. Навыки загружаются по требованию с помощью встроенного инструмента `skill`: агенты видят доступные навыки и при необходимости могут загрузить весь контент.

* * *

## Разместить файлы

Создайте одну папку для каждого имени навыка и поместите в нее `SKILL.md`. opencode выполняет поиск в следующих местах:

  * Конфигурация проекта: `.opencode/skills/<name>/SKILL.md`
  * Глобальная конфигурация: `~/.config/opencode/skills/<name>/SKILL.md`.
  * Совместимость с Project Claude: `.claude/skills/<name>/SKILL.md`
  * Глобальная совместимость с Claude: `~/.claude/skills/<name>/SKILL.md`
  * Совместимость с агентом проекта: `.agents/skills/<name>/SKILL.md`
  * Совместимость с глобальным агентом: `~/.agents/skills/<name>/SKILL.md`



* * *

## Понимание обнаружения

Для локальных путей проекта opencode переходит из вашего текущего рабочего каталога, пока не достигнет рабочего дерева git. Он загружает все соответствующие `skills/*/SKILL.md` в `.opencode/` и все соответствующие `.claude/skills/*/SKILL.md` или `.agents/skills/*/SKILL.md` по пути.

Глобальные определения также загружаются из `~/.config/opencode/skills/*/SKILL.md`, `~/.claude/skills/*/SKILL.md` и `~/.agents/skills/*/SKILL.md`.

* * *

## Напишите заголовок

Каждый `SKILL.md` должен начинаться с заголовка YAML. Распознаются только эти поля:

  * `name` (required)
  * `description` (required)
  * `license` (необязательно)
  * `compatibility` (необязательно)
  * `metadata` (необязательно, преобразование строк в строки)



Неизвестные поля заголовка игнорируются.

* * *

## Проверка имен

`name` должен:

  * Длина от 1 до 64 символов.
  * Используйте строчные буквы и цифры с одинарным дефисом.
  * Не начинаться и не заканчиваться на `-`.
  * Не содержать последовательных `--`
  * Сопоставьте имя каталога, содержащее `SKILL.md`.



Эквивалентное регулярное выражение:
```
^[a-z0-9]+(-[a-z0-9]+)*$
```

* * *

## Соблюдайте правила длины

`description` должно содержать от 1 до 1024 символов. Держите его достаточно конкретным, чтобы агент мог сделать правильный выбор.

* * *

## Используйте пример

Создайте `.opencode/skills/git-release/SKILL.md` следующим образом:
```
---
    name: git-release
    description: Create consistent releases and changelogs
    license: MIT
    compatibility: opencode
    metadata:
      audience: maintainers
      workflow: github
    ---
    
    
    ## What I do
    
    
    - Draft release notes from merged PRs
    - Propose a version bump
    - Provide a copy-pasteable `gh release create` command
    
    
    ## When to use me
    
    
    Use this when you are preparing a tagged release.
    Ask clarifying questions if the target versioning scheme is unclear.
```

* * *

## Распознавание описания инструмента

opencode перечисляет доступные навыки в описании инструмента `skill`. Каждая запись включает название и описание навыка:
```
<available_skills>
      <skill>
        <name>git-release</name>
        <description>Create consistent releases and changelogs</description>
      </skill>
    </available_skills>
```

Агент загружает навык, вызывая инструмент:
```
skill({ name: "git-release" })
```

* * *

## Настройка разрешений

Контролируйте, к каким навыкам агенты могут получить доступ, используя разрешения на основе шаблонов в `opencode.json`:
```
{
      "permission": {
        "skill": {
          "*": "allow",
          "pr-review": "allow",
          "internal-*": "deny",
          "experimental-*": "ask"
        }
      }
    }
```

Разрешение| Поведение  
---|---  
`allow`| Skill loads immediately  
`deny`| Skill hidden from agent, access rejected  
`ask`| User prompted for approval before loading  
  
Шаблоны поддерживают подстановочные знаки: `internal-*` соответствует `internal-docs`, `internal-tools` и т. д.

* * *

## Переопределить для каждого агента

Предоставьте конкретным агентам разрешения, отличные от глобальных настроек по умолчанию.

**Для пользовательских агентов** (в заголовке агента):
```
---
    permission:
      skill:
        "documents-*": "allow"
    ---
```

**Для встроенных агентов** (в формате `opencode.json`):
```
{
      "agent": {
        "plan": {
          "permission": {
            "skill": {
              "internal-*": "allow"
            }
          }
        }
      }
    }
```

* * *

## Отключить инструмент навыков

Полностью отключить навыки для агентов, которым не следует их использовать:

**Для индивидуальных агентов** :
```
---
    tools:
      skill: false
    ---
```

**Для встроенных агентов** :
```
{
      "agent": {
        "plan": {
          "tools": {
            "skill": false
          }
        }
      }
    }
```

Если этот параметр отключен, раздел `<available_skills>` полностью опускается.

* * *

## Устранение неполадок с загрузкой

Если навык не отображается:

  1. Убедитесь, что `SKILL.md` написано заглавными буквами.
  2. Убедитесь, что заголовок включает `name` и `description`.
  3. Убедитесь, что названия навыков уникальны во всех локациях.
  4. Проверьте разрешения — навыки с `deny` скрыты от агентов.



[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/skills.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-29"></a>
---
url: https://opencode.ai/docs/ru/custom-tools/
---

# Пользовательские инструменты

Создавайте инструменты, которые LLM может вызывать в opencode.

Пользовательские инструменты — это создаваемые вами функции, которые LLM может вызывать во время разговоров. Они работают вместе со [встроенными инструментами ](/docs/tools) opencode, такими как `read`, `write` и `bash`.

* * *

## Создание инструмента

Инструменты определяются как файлы **TypeScript** или **JavaScript**. Однако определение инструмента может вызывать сценарии, написанные на **любом языке** — TypeScript или JavaScript используются только для самого определения инструмента.

* * *

### Расположение

Их можно определить:

  * Локально, поместив их в каталог `.opencode/tools/` вашего проекта.
  * Или глобально, поместив их в `~/.config/opencode/tools/`.



* * *

### Структура

Самый простой способ создания инструментов — использовать помощник `tool()`, который обеспечивает безопасность типов и проверку.

.opencode/tools/database.ts
```
import { tool } from "@opencode-ai/plugin"
    
    
    export default tool({
      description: "Query the project database",
      args: {
        query: tool.schema.string().describe("SQL query to execute"),
      },
      async execute(args) {
        // Your database logic here
        return `Executed query: ${args.query}`
      },
    })
```

**имя файла** становится **именем инструмента**. Вышеупомянутое создает инструмент `database`.

* * *

#### Несколько инструментов в файле

Вы также можете экспортировать несколько инструментов из одного файла. Каждый экспорт становится **отдельным инструментом** с именем **`<filename>_<exportname>`**:

.opencode/tools/math.ts
```
import { tool } from "@opencode-ai/plugin"
    
    
    export const add = tool({
      description: "Add two numbers",
      args: {
        a: tool.schema.number().describe("First number"),
        b: tool.schema.number().describe("Second number"),
      },
      async execute(args) {
        return args.a + args.b
      },
    })
    
    
    export const multiply = tool({
      description: "Multiply two numbers",
      args: {
        a: tool.schema.number().describe("First number"),
        b: tool.schema.number().describe("Second number"),
      },
      async execute(args) {
        return args.a * args.b
      },
    })
```

При этом создаются два инструмента: `math_add` и `math_multiply`.

* * *

### Аргументы

Вы можете использовать `tool.schema`, то есть просто [Zod](https://zod.dev), для определения типов аргументов.
```
args: {
      query: tool.schema.string().describe("SQL query to execute")
    }
```

Вы также можете импортировать [Zod](https://zod.dev) напрямую и вернуть простой объект:
```
import { z } from "zod"
    
    
    export default {
      description: "Tool description",
      args: {
        param: z.string().describe("Parameter description"),
      },
      async execute(args, context) {
        // Tool implementation
        return "result"
      },
    }
```

* * *

### Контекст

Инструменты получают контекст текущего сеанса:

.opencode/tools/project.ts
```
import { tool } from "@opencode-ai/plugin"
    
    
    export default tool({
      description: "Get project information",
      args: {},
      async execute(args, context) {
        // Access context information
        const { agent, sessionID, messageID, directory, worktree } = context
        return `Agent: ${agent}, Session: ${sessionID}, Message: ${messageID}, Directory: ${directory}, Worktree: ${worktree}`
      },
    })
```

Используйте `context.directory` для рабочего каталога сеанса. Используйте `context.worktree` для корня рабочего дерева git.

* * *

## Примеры

### Инструмент на Python

Вы можете писать свои инструменты на любом языке, который захотите. Вот пример сложения двух чисел с использованием Python.

Сначала создайте инструмент как скрипт Python:

.opencode/tools/add.py
```
import sys
    
    
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(a + b)
```

Затем создайте определение инструмента, которое его вызывает:

.opencode/tools/python-add.ts
```
import { tool } from "@opencode-ai/plugin"
    import path from "path"
    
    
    export default tool({
      description: "Add two numbers using Python",
      args: {
        a: tool.schema.number().describe("First number"),
        b: tool.schema.number().describe("Second number"),
      },
      async execute(args, context) {
        const script = path.join(context.worktree, ".opencode/tools/add.py")
        const result = await Bun.$`python3 ${script} ${args.a} ${args.b}`.text()
        return result.trim()
      },
    })
```

Здесь мы используем утилиту [`Bun.$`](https://bun.com/docs/runtime/shell) для запуска скрипта Python.

[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/custom-tools.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

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


---

<a id="page-31"></a>
---
url: https://opencode.ai/docs/ru/server/
---

# Сервер

Взаимодействуйте с сервером opencode через HTTP.

Команда `opencode serve` запускает автономный HTTP-сервер, который предоставляет конечную точку OpenAPI, которую может использовать клиент с открытым кодом.

* * *

### Использование

Окно терминала
```
opencode serve [--port <number>] [--hostname <string>] [--cors <origin>]
```

#### Параметры

Флаг| Описание| По умолчанию  
---|---|---  
`--port`| Port to listen on| `4096`  
`--hostname`| Hostname to listen on| `127.0.0.1`  
`--mdns`| Enable mDNS discovery| `false`  
`--mdns-domain`| Custom domain name for mDNS service| `opencode.local`  
`--cors`| Additional browser origins to allow| `[]`  
  
`--cors` можно передать несколько раз:

Окно терминала
```
opencode serve --cors http://localhost:5173 --cors https://app.example.com
```

* * *

### Аутентификация

Установите `OPENCODE_SERVER_PASSWORD`, чтобы защитить сервер с помощью базовой аутентификации HTTP. Имя пользователя по умолчанию — `opencode` или установите `OPENCODE_SERVER_USERNAME`, чтобы переопределить его. Это относится как к `opencode serve`, так и к `opencode web`.

Окно терминала
```
OPENCODE_SERVER_PASSWORD=your-password opencode serve
```

* * *

### Как это работает

Когда вы запускаете `opencode`, он запускает TUI и сервер. Где находится TUI клиент, который общается с сервером. Сервер предоставляет спецификацию OpenAPI 3.1. конечная точка. Эта конечная точка также используется для создания файла [SDK](/docs/sdk).

Совет

Используйте сервер opencode для программного взаимодействия с открытым кодом.

Эта архитектура позволяет открытому коду поддерживать несколько клиентов и позволяет программно взаимодействовать с открытым кодом.

Вы можете запустить `opencode serve`, чтобы запустить автономный сервер. Если у вас есть TUI с открытым кодом запущен, `opencode serve` запустит новый сервер.

* * *

#### Подключиться к существующему серверу

Когда вы запускаете TUI, он случайным образом назначает порт и имя хоста. Вместо этого вы можете передать `--hostname` и `--port` [flags](/docs/cli). Затем используйте это для подключения к его серверу.

Конечную точку `/tui` можно использовать для управления TUI через сервер. Например, вы можете предварительно заполнить или запустить подсказку. Эта настройка используется плагинами opencode [IDE](/docs/ide).

* * *

## Спецификация

Сервер публикует спецификацию OpenAPI 3.1, которую можно просмотреть по адресу:
```
http://<hostname>:<port>/doc
```

For example, `http://localhost:4096/doc`. Use the spec to generate clients or inspect request and response types. Or view it in a Swagger explorer.

* * *

## API

Сервер opencode предоставляет следующие API.

* * *

### Глобальный

Метод| Путь| Описание| Ответ  
---|---|---|---  
`GET`| `/global/health`| Get server health and version| `{ healthy: true, version: string }`  
`GET`| `/global/event`| Get global events (SSE stream)| Event stream  
  
* * *

### Проект

Метод| Путь| Описание| Ответ  
---|---|---|---  
`GET`| `/project`| List all projects| [`Project[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`GET`| `/project/current`| Get the current project| [`Project`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
  
* * *

### Путь и система контроля версий

Метод| Путь| Описание| Ответ  
---|---|---|---  
`GET`| `/path`| Get the current path| [`Path`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`GET`| `/vcs`| Get VCS info for the current project| [`VcsInfo`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
  
* * *

### Экземпляр

Метод| Путь| Описание| Ответ  
---|---|---|---  
`POST`| `/instance/dispose`| Dispose the current instance| `boolean`  
  
* * *

### Конфигурация

Метод| Путь| Описание| Ответ  
---|---|---|---  
`GET`| `/config`| Get config info| [`Config`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`PATCH`| `/config`| Update config| [`Config`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`GET`| `/config/providers`| List providers and default models| `{ providers: `[Provider[]](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`, default: { [key: string]: string } }`  
  
* * *

### Поставщик

Метод| Путь| Описание| Ответ  
---|---|---|---  
`GET`| `/provider`| List all providers| `{ all: `[Provider[]](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`, default: {...}, connected: string[] }`  
`GET`| `/provider/auth`| Get provider authentication methods| `{ [providerID: string]: `[ProviderAuthMethod[]](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)` }`  
`POST`| `/provider/{id}/oauth/authorize`| Authorize a provider using OAuth| [`ProviderAuthAuthorization`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`POST`| `/provider/{id}/oauth/callback`| Handle OAuth callback for a provider| `boolean`  
  
* * *

### Сессии

Метод| Путь| Описание| Примечания  
---|---|---|---  
`GET`| `/session`| List all sessions| Returns [`Session[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`POST`| `/session`| Create a new session| body: `{ parentID?, title? }`, returns [`Session`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`GET`| `/session/status`| Get session status for all sessions| Returns `{ [sessionID: string]: `[SessionStatus](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)` }`  
`GET`| `/session/:id`| Get session details| Returns [`Session`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`DELETE`| `/session/:id`| Delete a session and all its data| Returns `boolean`  
`PATCH`| `/session/:id`| Update session properties| body: `{ title? }`, returns [`Session`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`GET`| `/session/:id/children`| Get a session’s child sessions| Returns [`Session[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`GET`| `/session/:id/todo`| Get the todo list for a session| Returns [`Todo[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`POST`| `/session/:id/init`| Analyze app and create `AGENTS.md`| body: `{ messageID, providerID, modelID }`, returns `boolean`  
`POST`| `/session/:id/fork`| Fork an existing session at a message| body: `{ messageID? }`, returns [`Session`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`POST`| `/session/:id/abort`| Abort a running session| Returns `boolean`  
`POST`| `/session/:id/share`| Share a session| Returns [`Session`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`DELETE`| `/session/:id/share`| Unshare a session| Returns [`Session`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`GET`| `/session/:id/diff`| Get the diff for this session| query: `messageID?`, returns [`FileDiff[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`POST`| `/session/:id/summarize`| Summarize the session| body: `{ providerID, modelID }`, returns `boolean`  
`POST`| `/session/:id/revert`| Revert a message| body: `{ messageID, partID? }`, returns `boolean`  
`POST`| `/session/:id/unrevert`| Restore all reverted messages| Returns `boolean`  
`POST`| `/session/:id/permissions/:permissionID`| Respond to a permission request| body: `{ response, remember? }`, returns `boolean`  
  
* * *

### Сообщения

Метод| Путь| Описание| Примечания  
---|---|---|---  
`GET`| `/session/:id/message`| List messages in a session| query: `limit?`, returns `{ info: `[Message](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`, parts: `[Part[]](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`}[]`  
`POST`| `/session/:id/message`| Send a message and wait for response| body: `{ messageID?, model?, agent?, noReply?, system?, tools?, parts }`, returns `{ info: `[Message](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`, parts: `[Part[]](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`}`  
`GET`| `/session/:id/message/:messageID`| Get message details| Returns `{ info: `[Message](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`, parts: `[Part[]](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`}`  
`POST`| `/session/:id/prompt_async`| Send a message asynchronously (no wait)| body: same as `/session/:id/message`, returns `204 No Content`  
`POST`| `/session/:id/command`| Execute a slash command| body: `{ messageID?, agent?, model?, command, arguments }`, returns `{ info: `[Message](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`, parts: `[Part[]](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`}`  
`POST`| `/session/:id/shell`| Run a shell command| body: `{ agent, model?, command }`, returns `{ info: `[Message](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`, parts: `[Part[]](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)`}`  
  
* * *

### Команды

Метод| Путь| Описание| Ответ  
---|---|---|---  
`GET`| `/command`| List all commands| [`Command[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
  
* * *

### Файлы

Метод| Путь| Описание| Ответ  
---|---|---|---  
`GET`| `/find?pattern=<pat>`| Search for text in files| Array of match objects with `path`, `lines`, `line_number`, `absolute_offset`, `submatches`  
`GET`| `/find/file?query=<q>`| Find files and directories by name| `string[]` (paths)  
`GET`| `/find/symbol?query=<q>`| Find workspace symbols| [`Symbol[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`GET`| `/file?path=<path>`| List files and directories| [`FileNode[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`GET`| `/file/content?path=<p>`| Read a file| [`FileContent`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`GET`| `/file/status`| Get status for tracked files| [`File[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
  
#### `/find/file` параметры запроса

  * `query` (обязательно) — строка поиска (нечеткое совпадение)
  * `type` (необязательно) — ограничить результаты `"file"` или `"directory"`.
  * `directory` (необязательно) — переопределить корень проекта для поиска.
  * `limit` (необязательно) — максимальное количество результатов (1–200)
  * `dirs` (необязательно) — устаревший флаг (`"false"` возвращает только файлы)



* * *

### Инструменты (Экспериментальные)

Метод| Путь| Описание| Ответ  
---|---|---|---  
`GET`| `/experimental/tool/ids`| List all tool IDs| [`ToolIDs`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`GET`| `/experimental/tool?provider=<p>&model=<m>`| List tools with JSON schemas for a model| [`ToolList`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
  
* * *

### LSP, форматтеры и MCP

Метод| Путь| Описание| Ответ  
---|---|---|---  
`GET`| `/lsp`| Get LSP server status| [`LSPStatus[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`GET`| `/formatter`| Get formatter status| [`FormatterStatus[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
`GET`| `/mcp`| Get MCP server status| `{ [name: string]: `[MCPStatus](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)` }`  
`POST`| `/mcp`| Add MCP server dynamically| body: `{ name, config }`, returns MCP status object  
  
* * *

### Агенты

Метод| Путь| Описание| Ответ  
---|---|---|---  
`GET`| `/agent`| List all available agents| [`Agent[]`](https://github.com/anomalyco/opencode/blob/dev/packages/sdk/js/src/gen/types.gen.ts)  
  
* * *

### Ведение журнала

Метод| Путь| Описание| Ответ  
---|---|---|---  
`POST`| `/log`| Write log entry. Body: `{ service, level, message, extra? }`| `boolean`  
  
* * *

### TUI

Метод| Путь| Описание| Ответ  
---|---|---|---  
`POST`| `/tui/append-prompt`| Append text to the prompt| `boolean`  
`POST`| `/tui/open-help`| Open the help dialog| `boolean`  
`POST`| `/tui/open-sessions`| Open the session selector| `boolean`  
`POST`| `/tui/open-themes`| Open the theme selector| `boolean`  
`POST`| `/tui/open-models`| Open the model selector| `boolean`  
`POST`| `/tui/submit-prompt`| Submit the current prompt| `boolean`  
`POST`| `/tui/clear-prompt`| Clear the prompt| `boolean`  
`POST`| `/tui/execute-command`| Execute a command (`{ command }`)| `boolean`  
`POST`| `/tui/show-toast`| Show toast (`{ title?, message, variant }`)| `boolean`  
`GET`| `/tui/control/next`| Wait for the next control request| Control request object  
`POST`| `/tui/control/response`| Respond to a control request (`{ body }`)| `boolean`  
  
* * *

### Авторизация

Метод| Путь| Описание| Ответ  
---|---|---|---  
`PUT`| `/auth/:id`| Set authentication credentials. Body must match provider schema| `boolean`  
  
* * *

### События

Метод| Путь| Описание| Ответ  
---|---|---|---  
`GET`| `/event`| Server-sent events stream. First event is `server.connected`, then bus events| Server-sent events stream  
  
* * *

### Документы

Метод| Путь| Описание| Ответ  
---|---|---|---  
`GET`| `/doc`| OpenAPI 3.1 specification| HTML page with OpenAPI spec  
  
[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/server.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-32"></a>
---
url: https://opencode.ai/docs/ru/plugins/
---

# Плагины

Напишите свои собственные плагины для расширения opencode.

Плагины позволяют расширять opencode, подключаясь к различным событиям и настраивая поведение. Вы можете создавать плагины для добавления новых функций, интеграции с внешними сервисами или изменения поведения opencode по умолчанию.

Для примера ознакомьтесь с [plugins](/docs/ecosystem#plugins), созданными сообществом.

* * *

## Используйте плагин

Есть два способа загрузки плагинов.

* * *

### Из локальных файлов

Поместите файлы JavaScript или TypeScript в каталог плагина.

  * `.opencode/plugins/` – плагины уровня проекта.
  * `~/.config/opencode/plugins/` — глобальные плагины



Файлы в этих каталогах автоматически загружаются при запуске.

* * *

### Из npm

Укажите пакеты npm в файле конфигурации.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "plugin": ["opencode-helicone-session", "opencode-wakatime", "@my-org/custom-plugin"]
    }
```

Поддерживаются как обычные, так и ограниченные пакеты npm.

Просмотрите доступные плагины в папке [ecosystem](/docs/ecosystem#plugins).

* * *

### Как устанавливаются плагины

**Плагины npm** устанавливаются автоматически с помощью Bun при запуске. Пакеты и их зависимости кэшируются в `~/.cache/opencode/node_modules/`.

**Локальные плагины** загружаются непосредственно из каталога плагинов. Чтобы использовать внешние пакеты, вы должны создать `package.json` в своем каталоге конфигурации (см. Зависимости) или опубликовать плагин в npm и [добавить его в свой config](/docs/config#plugins).

* * *

### Порядок загрузки

Плагины загружаются из всех источников, и все хуки запускаются последовательно. Порядок загрузки следующий:

  1. Глобальная конфигурация (`~/.config/opencode/opencode.json`)
  2. Конфигурация проекта (`opencode.json`)
  3. Глобальный каталог плагинов (`~/.config/opencode/plugins/`)
  4. Каталог плагинов проекта (`.opencode/plugins/`)



Дубликаты пакетов npm с тем же именем и версией загружаются один раз. Однако локальный плагин и плагин npm со схожими именами загружаются отдельно.

* * *

## Создать плагин

Плагин — это **модуль JavaScript/TypeScript** , который экспортирует один или несколько плагинов. функции. Каждая функция получает объект контекста и возвращает объект перехватчика.

* * *

### Зависимости

Локальные плагины и специальные инструменты могут использовать внешние пакеты npm. Добавьте `package.json` в каталог конфигурации с необходимыми вам зависимостями.

.opencode/package.json
```
{
      "dependencies": {
        "shescape": "^2.1.0"
      }
    }
```

opencode запускает `bun install` при запуске для их установки. Затем ваши плагины и инструменты смогут импортировать их.

.opencode/plugins/my-plugin.ts
```
import { escape } from "shescape"
    
    
    export const MyPlugin = async (ctx) => {
      return {
        "tool.execute.before": async (input, output) => {
          if (input.tool === "bash") {
            output.args.command = escape(output.args.command)
          }
        },
      }
    }
```

* * *

### Базовая структура

.opencode/plugins/example.js
```
export const MyPlugin = async ({ project, client, $, directory, worktree }) => {
      console.log("Plugin initialized!")
    
    
      return {
        // Hook implementations go here
      }
    }
```

Функция плагина получает:

  * `project`: Текущая информация о проекте.
  * `directory`: текущий рабочий каталог.
  * `worktree`: путь к рабочему дереву git.
  * `client`: клиент SDK с открытым кодом для взаимодействия с ИИ.
  * `$`: [Bun shell API](https://bun.com/docs/runtime/shell) для выполнения команд.



* * *

### Поддержка TypeScript

Для плагинов TypeScript вы можете импортировать типы из пакета плагина:

my-plugin.ts
```
import type { Plugin } from "@opencode-ai/plugin"
    
    
    export const MyPlugin: Plugin = async ({ project, client, $, directory, worktree }) => {
      return {
        // Type-safe hook implementations
      }
    }
```

* * *

### События

Плагины могут подписываться на события, как показано ниже в разделе «Примеры». Вот список различных доступных событий.

#### Командные события

  * `command.executed`



#### События файла

  * `file.edited`
  * `file.watcher.updated`



#### События установки

  * `installation.updated`



#### События LSP

  * `lsp.client.diagnostics`
  * `lsp.updated`



#### События сообщений

  * `message.part.removed`
  * `message.part.updated`
  * `message.removed`
  * `message.updated`



#### События разрешения

  * `permission.asked`
  * `permission.replied`



#### События сервера

  * `server.connected`



#### События сессии

  * `session.created`
  * `session.compacted`
  * `session.deleted`
  * `session.diff`
  * `session.error`
  * `session.idle`
  * `session.status`
  * `session.updated`



#### События

  * `todo.updated`



#### События shell

  * `shell.env`



#### События инструмента

  * `tool.execute.after`
  * `tool.execute.before`



#### Мероприятия TUI

  * `tui.prompt.append`
  * `tui.command.execute`
  * `tui.toast.show`



* * *

## Примеры

Вот несколько примеров плагинов, которые вы можете использовать для расширения opencode.

* * *

### Отправлять уведомления

Отправляйте уведомления при возникновении определенных событий:

.opencode/plugins/notification.js
```
export const NotificationPlugin = async ({ project, client, $, directory, worktree }) => {
      return {
        event: async ({ event }) => {
          // Send notification on session completion
          if (event.type === "session.idle") {
            await $`osascript -e 'display notification "Session completed!" with title "opencode"'`
          }
        },
      }
    }
```

Мы используем `osascript` для запуска AppleScript на macOS. Здесь мы используем его для отправки уведомлений.

Заметка

Если вы используете настольное приложение opencode, оно может автоматически отправлять системные уведомления, когда ответ готов или когда возникает ошибка сеанса.

* * *

### Защита .env

Запретите открытому коду читать файлы `.env`:

.opencode/plugins/env-protection.js
```
export const EnvProtection = async ({ project, client, $, directory, worktree }) => {
      return {
        "tool.execute.before": async (input, output) => {
          if (input.tool === "read" && output.args.filePath.includes(".env")) {
            throw new Error("Do not read .env files")
          }
        },
      }
    }
```

* * *

### Внедрение переменных среды

Внедряйте переменные среды во все shell-процессы выполнения (инструменты искусственного интеллекта и пользовательские terminal):

.opencode/plugins/inject-env.js
```
export const InjectEnvPlugin = async () => {
      return {
        "shell.env": async (input, output) => {
          output.env.MY_API_KEY = "secret"
          output.env.PROJECT_ROOT = input.cwd
        },
      }
    }
```

* * *

### Пользовательские инструменты

Плагины также могут добавлять в opencode собственные инструменты:

.opencode/plugins/custom-tools.ts
```
import { type Plugin, tool } from "@opencode-ai/plugin"
    
    
    export const CustomToolsPlugin: Plugin = async (ctx) => {
      return {
        tool: {
          mytool: tool({
            description: "This is a custom tool",
            args: {
              foo: tool.schema.string(),
            },
            async execute(args, context) {
              const { directory, worktree } = context
              return `Hello ${args.foo} from ${directory} (worktree: ${worktree})`
            },
          }),
        },
      }
    }
```

Помощник `tool` создает собственный инструмент, который может вызывать opencode. Он принимает функцию схемы Zod и возвращает определение инструмента:

  * `description`: Что делает инструмент
  * `args`: схема Zod для аргументов инструмента.
  * `execute`: функция, которая запускается при вызове инструмента.



Ваши пользовательские инструменты будут доступны для открытия кода наряду со встроенными инструментами.

* * *

### Ведение журнала

Используйте `client.app.log()` вместо `console.log` для структурированного ведения журнала:

.opencode/plugins/my-plugin.ts
```
export const MyPlugin = async ({ client }) => {
      await client.app.log({
        body: {
          service: "my-plugin",
          level: "info",
          message: "Plugin initialized",
          extra: { foo: "bar" },
        },
      })
    }
```

Уровни: `debug`, `info`, `warn`, `error`. Подробности см. в документации SDK](<https://opencode.ai/docs/sdk>).

* * *

### Хуки сжатия

Настройте контекст, включаемый при сжатии сеанса:

.opencode/plugins/compaction.ts
```
import type { Plugin } from "@opencode-ai/plugin"
    
    
    export const CompactionPlugin: Plugin = async (ctx) => {
      return {
        "experimental.session.compacting": async (input, output) => {
          // Inject additional context into the compaction prompt
          output.context.push(`
    ## Custom Context
    
    
    Include any state that should persist across compaction:
    - Current task status
    - Important decisions made
    - Files being actively worked on
    `)
        },
      }
    }
```

Хук `experimental.session.compacting` срабатывает до того, как LLM сгенерирует сводку для продолжения. Используйте его для внедрения контекста, специфичного для домена, который будет пропущен при запросе на сжатие по умолчанию.

Вы также можете полностью заменить запрос на уплотнение, установив `output.prompt`:

.opencode/plugins/custom-compaction.ts
```
import type { Plugin } from "@opencode-ai/plugin"
    
    
    export const CustomCompactionPlugin: Plugin = async (ctx) => {
      return {
        "experimental.session.compacting": async (input, output) => {
          // Replace the entire compaction prompt
          output.prompt = `
    You are generating a continuation prompt for a multi-agent swarm session.
    
    
    Summarize:
    1. The current task and its status
    2. Which files are being modified and by whom
    3. Any blockers or dependencies between agents
    4. The next steps to complete the work
    
    
    Format as a structured prompt that a new agent can use to resume work.
    `
        },
      }
    }
```

Если установлен `output.prompt`, он полностью заменяет приглашение на сжатие по умолчанию. Массив `output.context` в этом случае игнорируется.

[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/plugins.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-33"></a>
---
url: https://opencode.ai/docs/ru/ecosystem/
---

# Экосистема

Проекты и интеграции, созданные с помощью opencode.

Коллекция проектов сообщества, построенных на opencode.

Заметка

Хотите добавить свой проект, связанный с opencode, в этот список? Разместите PR.

Вы также можете посетить [awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) и [opencode.cafe](https://opencode.cafe) — хаб, объединяющий экосистему и сообщество.

* * *

## Плагины

Имя| Описание  
---|---  
[opencode-daytona](https://github.com/jamesmurdza/daytona/blob/main/guides/typescript/opencode/README.md)| Автоматически запускайте сеансы opencode в изолированных песочницах Daytona с синхронизацией git и предварительным просмотром в реальном времени.  
[opencode-helicone-session](https://github.com/H2Shami/opencode-helicone-session)| Автоматически внедрять заголовки сеансов Helicone для группировки запросов.  
[opencode-type-inject](https://github.com/nick-vi/opencode-type-inject)| Автоматическое внедрение типов TypeScript/Svelte в файлы, считываемые с помощью инструментов поиска.  
[opencode-openai-codex-auth](https://github.com/numman-ali/opencode-openai-codex-auth)| Используйте подписку ChatGPT Plus/Pro вместо кредитов API.  
[opencode-gemini-auth](https://github.com/jenslys/opencode-gemini-auth)| Используйте существующий план Gemini вместо выставления счетов через API.  
[opencode-antigravity-auth](https://github.com/NoeFabris/opencode-antigravity-auth)| Используйте бесплатные модели Antigravity вместо выставления счетов через API.  
[opencode-devcontainers](https://github.com/athal7/opencode-devcontainers)| Многоветвевая изоляция контейнеров разработки с мелкими клонами и автоматическим назначением портов.  
[opencode-google-antigravity-auth](https://github.com/shekohex/opencode-google-antigravity-auth)| Плагин Google Antigravity OAuth с поддержкой поиска Google и более надежной обработкой API.  
[opencode-dynamic-context-pruning](https://github.com/Tarquinen/opencode-dynamic-context-pruning)| Оптимизируйте использование токенов за счет сокращения выходных данных устаревших инструментов.  
[opencode-websearch-cited](https://github.com/ghoulr/opencode-websearch-cited.git)| Добавьте встроенную поддержку веб-поиска для поддерживаемых поставщиков в стиле Google.  
[opencode-pty](https://github.com/shekohex/opencode-pty.git)| Позволяет агентам ИИ запускать фоновые процессы в PTY и отправлять им интерактивные данные.  
[opencode-shell-strategy](https://github.com/JRedeker/opencode-shell-strategy)| Инструкции для неинтерактивных shell-команд — предотвращают зависания из-за операций, зависящих от TTY.  
[opencode-wakatime](https://github.com/angristan/opencode-wakatime)| Отслеживайте использование opencode с помощью Wakatime  
[opencode-md-table-formatter](https://github.com/franlol/opencode-md-table-formatter/tree/main)| Очистка таблиц Markdown, созданных LLM  
[opencode-morph-fast-apply](https://github.com/JRedeker/opencode-morph-fast-apply)| Редактирование кода в 10 раз быстрее с помощью API Morph Fast Apply и маркеров отложенного редактирования.  
[oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)| Фоновые агенты, встроенные инструменты LSP/AST/MCP, курируемые агенты, совместимость с Claude Code  
[opencode-notificator](https://github.com/panta82/opencode-notificator)| Уведомления на рабочем столе и звуковые оповещения для сеансов opencode  
[opencode-notifier](https://github.com/mohak34/opencode-notifier)| Уведомления на рабочем столе и звуковые оповещения о разрешениях, завершении и событиях ошибок.  
[opencode-zellij-namer](https://github.com/24601/opencode-zellij-namer)| Автоматическое именование сеансов Zellij на основе искусственного интеллекта на основе контекста opencode.  
[opencode-skillful](https://github.com/zenobi-us/opencode-skillful)| Разрешить агентам opencode отложенную загрузку подсказок по требованию с обнаружением и внедрением навыков.  
[opencode-supermemory](https://github.com/supermemoryai/opencode-supermemory)| Постоянная память между сеансами с использованием Supermemory  
[@plannotator/opencode](https://github.com/backnotprop/plannotator/tree/main/apps/opencode-plugin)| Интерактивный обзор плана с визуальными аннотациями и возможностью совместного использования в частном или автономном режиме.  
[@openspoon/subtask2](https://github.com/spoons-and-mirrors/subtask2)| Расширьте opencode/команды до мощной системы оркестровки с детальным управлением потоком данных.  
[opencode-scheduler](https://github.com/different-ai/opencode-scheduler)| Планируйте повторяющиеся задания с помощью launchd (Mac) или systemd (Linux) с синтаксисом cron.  
[micode](https://github.com/vtemian/micode)| Структурированный мозговой штурм → План → Реализация рабочего процесса с непрерывностью сеанса  
[octto](https://github.com/vtemian/octto)| Интерактивный пользовательский интерфейс браузера для мозгового штурма с помощью искусственного интеллекта с формами из нескольких вопросов  
[opencode-background-agents](https://github.com/kdcokenny/opencode-background-agents)| Фоновые агенты в стиле Claude Code с асинхронным делегированием и сохранением контекста.  
[opencode-notify](https://github.com/kdcokenny/opencode-notify)| Встроенные уведомления ОС для opencode — узнайте, когда задачи завершены  
[opencode-workspace](https://github.com/kdcokenny/opencode-workspace)| Комплексный пакет многоагентной оркестровки — 16 компонентов, одна установка  
[opencode-worktree](https://github.com/kdcokenny/opencode-worktree)| Рабочие деревья git с нулевым трением для opencode  
  
* * *

## Проекты

Имя| Описание  
---|---  
[opencode.nvim](https://github.com/NickvanDyke/opencode.nvim)| Плагин Neovim для подсказок с поддержкой редактора, созданный на основе API  
[portal](https://github.com/hosenur/portal)| Мобильный веб-интерфейс для opencode через Tailscale/VPN  
[opencode plugin template](https://github.com/zenobi-us/opencode-plugin-template/)| Шаблон для создания плагинов opencode  
[opencode.nvim](https://github.com/sudo-tee/opencode.nvim)| Интерфейс Neovim для opencode — агент кодирования искусственного интеллекта на базе terminal  
[ai-sdk-provider-opencode-sdk](https://github.com/ben-vargas/ai-sdk-provider-opencode-sdk)| Поставщик Vercel AI SDK для использования opencode через @opencode-ai/sdk  
[OpenChamber](https://github.com/btriapitsyn/openchamber)| Веб-приложение или настольное приложение и расширение VS Code для opencode  
[OpenCode-Obsidian](https://github.com/mtymek/opencode-obsidian)| Плагин Obsidian, встраивающий opencode в пользовательский интерфейс Obsidian.  
[OpenWork](https://github.com/different-ai/openwork)| Альтернатива Claude Cowork с открытым исходным кодом на базе opencode.  
[ocx](https://github.com/kdcokenny/ocx)| Менеджер расширений opencode с переносимыми изолированными профилями.  
[CodeNomad](https://github.com/NeuralNomadsAI/CodeNomad)| Настольное, веб-, мобильное и удаленное клиентское приложение для opencode  
  
* * *

## Агенты

Имя| Описание  
---|---  
[Agentic](https://github.com/Cluster444/agentic)| Модульные ИИ-агенты и команды для структурированной разработки  
[opencode-agents](https://github.com/darrenhinde/opencode-agents)| Конфигурации, подсказки, агенты и плагины для улучшения рабочих процессов.  
  
[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/ecosystem.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

