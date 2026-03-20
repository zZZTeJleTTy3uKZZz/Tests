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
