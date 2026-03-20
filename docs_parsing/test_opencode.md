# Полная документация OpenCode

## Оглавление

- [Введение](#page-1)
- [Конфигурация](#page-2)
- [Провайдеры](#page-3)
- [Сеть](#page-4)
- [Корпоративное использование](#page-5)
- [Поиск неисправностей](#page-6)
- [Windows](#page-7)
- **Использование**
  - [TUI](#page-8)
  - [CLI](#page-9)
  - [Интернет](#page-10)
  - [IDE](#page-11)
  - [Zen](#page-12)
  - [Делиться](#page-13)
  - [GitHub](#page-14)
  - [GitLab](#page-15)
- **Настройка**
  - [Инструменты](#page-16)
  - [Правила](#page-17)
  - [Агенты](#page-18)
  - [Модели](#page-19)
  - [Темы](#page-20)
  - [Сочетания клавиш](#page-21)
  - [Команды](#page-22)
  - [Форматтеры](#page-23)
  - [Разрешения](#page-24)
  - [LSP-серверы](#page-25)
  - [MCP-серверы](#page-26)
  - [Поддержка ACP](#page-27)
  - [Навыки агента](#page-28)
  - [Пользовательские инструменты](#page-29)
- **Разработка**
  - [SDK](#page-30)
  - [Сервер](#page-31)
  - [Плагины](#page-32)
  - [Экосистема](#page-33)

---

<a id="page-1"></a>
---
url: https://opencode.ai/docs/ru/
---

# Введение

Начните работу с opencode.

[**opencode**](/) — это агент кодирования искусственного интеллекта с открытым исходным кодом. Он доступен в виде интерфейса на базе терминала, настольного приложения или расширения IDE.

![opencode TUI с темой opencode](https://opencode.ai/docs/_astro/screenshot.CQjBbRyJ_1dLadc.webp)

Давайте начнем.

* * *

#### Системные требования

Чтобы использовать opencode в вашем терминале, вам понадобится:

  1. Современный эмулятор терминала, например:

     * [WezTerm](https://wezterm.org), кроссплатформенный
     * [Alacritty](https://alacritty.org), кроссплатформенный
     * [Ghostty](https://ghostty.org), Linux и macOS
     * [Kitty](https://sw.kovidgoyal.net/kitty/), Linux и macOS
  2. Ключи API для поставщиков LLM, которых вы хотите использовать.




* * *

## Установка

Самый простой способ установить opencode — через сценарий установки.

Окно терминала
```
curl -fsSL https://opencode.ai/install | bash
```

Вы также можете установить его с помощью следующих команд:

  * **Использование Node.js**

    * npm 
    * Bun 
    * pnpm 
    * Yarn 

Окно терминала
```
npm install -g opencode-ai
```

Окно терминала
```
bun install -g opencode-ai
```

Окно терминала
```
pnpm install -g opencode-ai
```

Окно терминала
```
yarn global add opencode-ai
```

  * **Использование Homebrew в macOS и Linux**

Окно терминала
```
brew install anomalyco/tap/opencode
```

> Мы рекомендуем использовать tap opencode для получения самых последних версий. Официальная формула `brew install opencode` поддерживается командой Homebrew и обновляется реже.

  * **Использование Paru в Arch Linux**

Окно терминала
```
sudo pacman -S opencode           # Arch Linux (Stable)
        paru -S opencode-bin              # Arch Linux (Latest from AUR)
```




#### Windows

Рекомендуется: используйте WSL

Для наилучшей работы в Windows мы рекомендуем использовать [Подсистема Windows для Linux (WSL)](/docs/windows-wsl). Он обеспечивает лучшую производительность и полную совместимость с функциями opencode.

  * **Используя Chocolatey**

Окно терминала
```
choco install opencode
```

  * **Использование Scoop**

Окно терминала
```
scoop install opencode
```

  * **Использование NPM**

Окно терминала
```
npm install -g opencode-ai
```

  * **Использование Mise**

Окно терминала
```
mise use -g github:anomalyco/opencode
```

  * **Использование Docker**

Окно терминала
```
docker run -it --rm ghcr.io/anomalyco/opencode
```




В настоящее время добавляется поддержка установки opencode в Windows с помощью Bun.

Вы также можете получить двоичный файл из файла [Releases](https://github.com/anomalyco/opencode/releases).

* * *

## Настроить

С opencode вы можете использовать любого поставщика LLM, настроив его ключи API.

Если вы новичок в использовании поставщиков LLM, мы рекомендуем использовать [OpenCode Zen](/docs/zen). Это тщательно подобранный список моделей, протестированных и проверенных opencode. команда.

  1. Запустите команду `/connect` в TUI, выберите opencode и перейдите по адресу [opencode.ai/auth](https://opencode.ai/auth).
```
/connect
```

  2. Войдите в систему, добавьте свои платежные данные и скопируйте ключ API.

  3. Вставьте свой ключ API.
```
┌ API key
         │
         │
         └ enter
```




Альтернативно вы можете выбрать одного из других поставщиков. [Подробнее](/docs/providers#directory).

* * *

## Инициализация

Теперь, когда вы настроили поставщика, вы можете перейти к проекту, который над которым вы хотите работать.

Окно терминала
```
cd /path/to/project
```

И запустите opencode.

Окно терминала
```
opencode
```

Затем инициализируйте opencode для проекта, выполнив следующую команду.
```
/init
```

Это позволит opencode проанализировать ваш проект и создать файл `AGENTS.md` в корень проекта.

Совет

Вам следует зафиксировать файл `AGENTS.md` вашего проекта в Git.

Это помогает opencode понять структуру проекта и шаблоны кодирования. использовал.

* * *

## Использование

Теперь вы готовы использовать opencode для работы над своим проектом. Не стесняйтесь спрашивать о чем угодно!

Если вы новичок в использовании агента кодирования ИИ, вот несколько примеров, которые могут вам помочь. помощь.

* * *

### Задавайте вопросы

Вы можете попросить opencode объяснить вам кодовую базу.

Совет

Используйте ключ `@` для нечеткого поиска файлов в проекте.
```
How is authentication handled in @packages/functions/src/api/index.ts
```

Это полезно, если есть часть кодовой базы, над которой вы не работали.

* * *

### Добавление функций

Вы можете попросить opencode добавить новые функции в ваш проект. Хотя мы сначала рекомендуем попросить его создать план.

  1. **Составьте план**

opencode имеет _режим планирования_ , который отключает возможность вносить изменения и вместо этого предложите _как_ реализовать эту функцию.

Переключитесь на него с помощью клавиши **Tab**. Вы увидите индикатор этого в правом нижнем углу.
```
<TAB>
```

Теперь давайте опишем, что мы хотим от него.
```
When a user deletes a note, we'd like to flag it as deleted in the database.
         Then create a screen that shows all the recently deleted notes.
         From this screen, the user can undelete a note or permanently delete it.
```

Вы хотите предоставить opencode достаточно подробностей, чтобы понять, чего вы хотите. Это помогает поговорить с ним так, как будто вы разговариваете с младшим разработчиком в своей команде.

Совет

Дайте opencode много контекста и примеров, чтобы помочь ему понять, что вы хотеть.

  2. **Итерация плана**

Как только он предоставит вам план, вы можете оставить ему отзыв или добавить более подробную информацию.
```
We'd like to design this new screen using a design I've used before.
         [Image #1] Take a look at this image and use it as a reference.
```

Совет

Перетащите изображения в терминал, чтобы добавить их в подсказку.

opencode может сканировать любые изображения, которые вы ему предоставляете, и добавлять их в командную строку. Ты можешь сделайте это, перетащив изображение в терминал.

  3. **Создайте функцию**

Как только вы почувствуете себя комфортно с планом, вернитесь в _режим сборки_ , снова нажав клавишу **Tab**.
```
<TAB>
```

И попросить его внести изменения.
```
Sounds good! Go ahead and make the changes.
```




* * *

### Внесение изменений

Для более простых изменений вы можете попросить opencode создать его напрямую. без необходимости предварительного рассмотрения плана.
```
We need to add authentication to the /settings route. Take a look at how this is
    handled in the /notes route in @packages/functions/src/notes.ts and implement
    the same logic in @packages/functions/src/settings.ts
```

Вы хотите убедиться, что вы предоставляете достаточно деталей, чтобы opencode сделал правильный выбор. изменения.

* * *

### Отмена изменений

Допустим, вы просите opencode внести некоторые изменения.
```
Can you refactor the function in @packages/functions/src/api/index.ts?
```

Но ты понимаешь, что это не то, чего ты хотел. Вы **можете отменить** изменения с помощью команды `/undo`.
```
/undo
```

opencode теперь отменит внесенные вами изменения и покажет исходное сообщение. снова.
```
Can you refactor the function in @packages/functions/src/api/index.ts?
```

Отсюда вы можете настроить подсказку и попросить opencode повторить попытку.

Совет

Вы можете запустить `/undo` несколько раз, чтобы отменить несколько изменений.

Или вы **можете повторить** изменения с помощью команды `/redo`.
```
/redo
```

* * *

## Общий доступ

Разговоры, которые вы ведете с opencode, можно [поделиться с вашим команда](/docs/share).
```
/share
```

Это создаст ссылку на текущий разговор и скопирует ее в буфер обмена.

Заметка

По умолчанию общий доступ к беседам не предоставляется.

Вот [пример диалога](https://opencode.ai/s/4XP1fce5) с opencode.

* * *

## Настроить

И все! Теперь вы профессионал в использовании opencode.

Чтобы создать свою собственную, мы рекомендуем [выбрать тему](/docs/themes), [настроить привязки клавиш](/docs/keybinds), [настроить средства форматирования кода](/docs/formatters), [создать собственные команды](/docs/commands) или поиграться с файлом [opencode config](/docs/config).

[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/index.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-2"></a>
---
url: https://opencode.ai/docs/ru/config/
---

# Конфигурация

Использование конфигурации opencode JSON.

Вы можете настроить opencode, используя файл конфигурации JSON.

* * *

## Формат

opencode поддерживает форматы **JSON** и **JSONC** (JSON с комментариями).

opencode.jsonc
```
{
      "$schema": "https://opencode.ai/config.json",
      // Theme configuration
      "theme": "opencode",
      "model": "anthropic/claude-sonnet-4-5",
      "autoupdate": true,
    }
```

* * *

## Расположение

Вы можете разместить свою конфигурацию в нескольких разных местах, и у них есть разный порядок старшинства.

Заметка

Файлы конфигурации **объединяются** , а не заменяются.

Файлы конфигурации объединяются, а не заменяются. Настройки из следующих мест конфигурации объединяются. Более поздние конфигурации переопределяют предыдущие только в случае конфликта ключей. Неконфликтные настройки из всех конфигов сохраняются.

Например, если ваша глобальная конфигурация устанавливает `theme: "opencode"` и `autoupdate: true`, а конфигурация вашего проекта устанавливает `model: "anthropic/claude-sonnet-4-5"`, окончательная конфигурация будет включать все три параметра.

* * *

### Порядок приоритета

Источники конфигурации загружаются в следующем порядке (более поздние источники переопределяют более ранние):

  1. **Удаленная конфигурация** (от `.well-known/opencode`) – организационные настройки по умолчанию.
  2. **Глобальная конфигурация** (`~/.config/opencode/opencode.json`) — настройки пользователя.
  3. **Пользовательская конфигурация** (`OPENCODE_CONFIG` env var) – пользовательские переопределения
  4. **Конфигурация проекта** (`opencode.json` в проекте) — настройки, специфичные для проекта.
  5. **Каталоги`.opencode`** — агенты, команды, плагины
  6. **Встроенная конфигурация** (`OPENCODE_CONFIG_CONTENT` env var) – переопределяет время выполнения



Это означает, что конфигурации проекта могут переопределять глобальные настройки по умолчанию, а глобальные конфигурации могут переопределять настройки по умолчанию для удаленной организации.

Заметка

В каталогах `.opencode` и `~/.config/opencode` для подкаталогов используются **множественные имена** : `agents/`, `commands/`, `modes/`, `plugins/`, `skills/`, `tools/` и `themes/`. Единственные имена (например, `agent/`) также поддерживаются для обратной совместимости.

* * *

### Удаленная

Организации могут предоставить конфигурацию по умолчанию через конечную точку `.well-known/opencode`. Он извлекается автоматически при аутентификации у провайдера, который его поддерживает.

Удаленная конфигурация загружается первой и служит базовым слоем. Все остальные источники конфигурации (глобальные, проектные) могут переопределить эти значения по умолчанию.

Например, если ваша организация предоставляет серверы MCP, которые по умолчанию отключены:

Remote config from .well-known/opencode
```
{
      "mcp": {
        "jira": {
          "type": "remote",
          "url": "https://jira.example.com/mcp",
          "enabled": false
        }
      }
    }
```

Вы можете включить определенные серверы в локальной конфигурации:

opencode.json
```
{
      "mcp": {
        "jira": {
          "type": "remote",
          "url": "https://jira.example.com/mcp",
          "enabled": true
        }
      }
    }
```

* * *

### Глобальная

Поместите глобальную конфигурацию opencode в `~/.config/opencode/opencode.json`. Используйте глобальную конфигурацию для общепользовательских настроек, таких как темы, поставщики или привязки клавиш.

Глобальная конфигурация переопределяет настройки по умолчанию для удаленной организации.

* * *

### Проектная

Добавьте `opencode.json` в корень вашего проекта. Конфигурация проекта имеет наивысший приоритет среди стандартных файлов конфигурации — она переопределяет как глобальные, так и удаленные конфигурации.

Совет

Поместите конфигурацию конкретного проекта в корень вашего проекта.

Когда opencode запускается, он ищет файл конфигурации в текущем каталоге или переходит к ближайшему каталогу Git.

Его также можно безопасно зарегистрировать в Git, и он использует ту же схему, что и глобальная.

* * *

### Пользовательский путь

Укажите собственный путь к файлу конфигурации, используя переменную среды `OPENCODE_CONFIG`.

Окно терминала
```
export OPENCODE_CONFIG=/path/to/my/custom-config.json
    opencode run "Hello world"
```

Пользовательская конфигурация загружается между глобальными и проектными конфигурациями в порядке приоритета.

* * *

### Пользовательский каталог

Укажите пользовательский каталог конфигурации, используя переменную среды `OPENCODE_CONFIG_DIR`. В этом каталоге будет выполняться поиск агентов, команд, режимов и плагинов (аналогично стандартному каталогу `.opencode`), и он должен иметь ту же структуру.

Окно терминала
```
export OPENCODE_CONFIG_DIR=/path/to/my/config-directory
    opencode run "Hello world"
```

Пользовательский каталог загружается после каталогов global config и `.opencode`, поэтому он **может переопределить** их настройки.

* * *

## Схема

Файл конфигурации имеет схему, определенную в [**`opencode.ai/config.json`**](https://opencode.ai/config.json).

Ваш редактор должен иметь возможность проверять и автозаполнять данные на основе схемы.

* * *

### TUI

Вы можете настроить параметры TUI с помощью опции `tui`.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "tui": {
        "scroll_speed": 3,
        "scroll_acceleration": {
          "enabled": true
        },
        "diff_style": "auto"
      }
    }
```

Доступные варианты:

  * `scroll_acceleration.enabled` — включить ускорение прокрутки в стиле MacOS. **Имеет приоритет над`scroll_speed`.**
  * `scroll_speed` — пользовательский множитель скорости прокрутки (по умолчанию: `3`, минимум: `1`). Игнорируется, если `scroll_acceleration.enabled` равен `true`.
  * `diff_style` — управление рендерингом различий. `"auto"` адаптируется к ширине terminal, `"stacked"` всегда отображает один столбец.



[Подробнее об использовании TUI можно узнать здесь](/docs/tui).

* * *

### Сервер

Вы можете настроить параметры сервера для команд `opencode serve` и `opencode web` с помощью опции `server`.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "server": {
        "port": 4096,
        "hostname": "0.0.0.0",
        "mdns": true,
        "mdnsDomain": "myproject.local",
        "cors": ["http://localhost:5173"]
      }
    }
```

Доступные варианты:

  * `port` — порт для прослушивания.
  * `hostname` — имя хоста для прослушивания. Если `mdns` включен и имя хоста не задано, по умолчанию используется `0.0.0.0`.
  * `mdns` — включить обнаружение службы mDNS. Это позволит другим устройствам в сети обнаружить ваш сервер opencode.
  * `mdnsDomain` — собственное доменное имя для службы mDNS. По умолчанию `opencode.local`. Полезно для запуска нескольких экземпляров в одной сети.
  * `cors` — дополнительные источники, позволяющие использовать CORS при использовании HTTP-сервера из браузерного клиента. Значения должны быть полными источниками (схема + хост + дополнительный порт), например `https://app.example.com`.



[Подробнее о сервере можно узнать здесь](/docs/server).

* * *

### Инструменты

Вы можете управлять инструментами, которые LLM может использовать, с помощью опции `tools`.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "tools": {
        "write": false,
        "bash": false
      }
    }
```

[Подробнее об инструментах можно узнать здесь](/docs/tools).

* * *

### models

Вы можете настроить поставщиков и модели, которые хотите использовать в своей конфигурации opencode, с помощью параметров `provider`, `model` и `small_model`.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "provider": {},
      "model": "anthropic/claude-sonnet-4-5",
      "small_model": "anthropic/claude-haiku-4-5"
    }
```

Опция `small_model` настраивает отдельную модель для облегченных задач, таких как создание заголовков. По умолчанию opencode пытается использовать более дешевую модель, если она доступна у вашего провайдера, в противном случае он возвращается к вашей основной модели.

Опции провайдера могут включать `timeout` и `setCacheKey`:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "provider": {
        "anthropic": {
          "options": {
            "timeout": 600000,
            "setCacheKey": true
          }
        }
      }
    }
```

  * `timeout` — таймаут запроса в миллисекундах (по умолчанию: 300000). Установите `false` для отключения.
  * `setCacheKey` — убедитесь, что ключ кэша всегда установлен для назначенного поставщика.



Вы также можете настроить [локальные модели](/docs/models#local). [Подробнее ](/docs/models).

* * *

#### Параметры, зависящие от поставщика

Некоторые поставщики поддерживают дополнительные параметры конфигурации помимо общих настроек `timeout` и `apiKey`.

##### Amazon

Amazon Bedrock поддерживает конфигурацию, специфичную для AWS:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "provider": {
        "amazon-bedrock": {
          "options": {
            "region": "us-east-1",
            "profile": "my-aws-profile",
            "endpoint": "https://bedrock-runtime.us-east-1.vpce-xxxxx.amazonaws.com"
          }
        }
      }
    }
```

  * `region` — регион AWS для Bedrock (по умолчанию переменная среды `AWS_REGION` или `us-east-1`)
  * `profile` — именованный профиль AWS из `~/.aws/credentials` (по умолчанию переменная окружения `AWS_PROFILE`)
  * `endpoint` — URL-адрес пользовательской конечной точки для конечных точек VPC. Это псевдоним общего параметра `baseURL`, использующий терминологию, специфичную для AWS. Если указаны оба параметра, `endpoint` имеет приоритет.



Заметка

Токены носителя (`AWS_BEARER_TOKEN_BEDROCK` или `/connect`) имеют приоритет над аутентификацией на основе профиля. Подробности см. в [приоритет аутентификации](/docs/providers#authentication-precedence).

[Подробнее о конфигурации Amazon Bedrock](/docs/providers#amazon-bedrock).

* * *

### theme

Вы можете настроить тему, которую хотите использовать, в конфигурации opencode с помощью опции `theme`.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "theme": ""
    }
```

[Подробнее здесь](/docs/themes).

* * *

### agent

Вы можете настроить специализированные агенты для конкретных задач с помощью опции `agent`.

opencode.jsonc
```
{
      "$schema": "https://opencode.ai/config.json",
      "agent": {
        "code-reviewer": {
          "description": "Reviews code for best practices and potential issues",
          "model": "anthropic/claude-sonnet-4-5",
          "prompt": "You are a code reviewer. Focus on security, performance, and maintainability.",
          "tools": {
            // Disable file modification tools for review-only agent
            "write": false,
            "edit": false,
          },
        },
      },
    }
```

Вы также можете определить агентов, используя файлы Markdown в `~/.config/opencode/agents/` или `.opencode/agents/`. [Подробнее здесь](/docs/agents).

* * *

### default_agent

Вы можете установить агента по умолчанию, используя опцию `default_agent`. Это определяет, какой агент используется, если ни один из них не указан явно.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "default_agent": "plan"
    }
```

Агент по умолчанию должен быть основным агентом (а не субагентом). Это может быть встроенный агент, например `"build"` или `"plan"`, или [пользовательский агент](/docs/agents), который вы определили. Если указанный агент не существует или является субагентом, opencode вернется к `"build"` с предупреждением.

Этот параметр применяется ко всем интерфейсам: TUI, CLI (`opencode run`), настольному приложению и действию GitHub.

* * *

### share

Функцию [share](/docs/share) можно настроить с помощью опции `share`.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "share": "manual"
    }
```

Принимает значения:

  * `"manual"` — разрешить общий доступ вручную с помощью команд (по умолчанию).
  * `"auto"` — автоматически делиться новыми беседами.
  * `"disabled"` — полностью отключить общий доступ



По умолчанию общий доступ установлен в ручной режим, в котором вам необходимо явно делиться разговорами с помощью команды `/share`.

* * *

### Команды

Вы можете настроить собственные команды для повторяющихся задач с помощью опции `command`.

opencode.jsonc
```
{
      "$schema": "https://opencode.ai/config.json",
      "command": {
        "test": {
          "template": "Run the full test suite with coverage report and show any failures.\nFocus on the failing tests and suggest fixes.",
          "description": "Run tests with coverage",
          "agent": "build",
          "model": "anthropic/claude-haiku-4-5",
        },
        "component": {
          "template": "Create a new React component named $ARGUMENTS with TypeScript support.\nInclude proper typing and basic structure.",
          "description": "Create a new component",
        },
      },
    }
```

Вы также можете определять команды, используя файлы Markdown в `~/.config/opencode/commands/` или `.opencode/commands/`. [Подробнее здесь](/docs/commands).

* * *

### Сочетания клавиш

Вы можете настроить привязки клавиш с помощью опции `keybinds`.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "keybinds": {}
    }
```

[Подробнее здесь](/docs/keybinds).

* * *

### Автообновление

opencode автоматически загрузит все новые обновления при запуске. Вы можете отключить это с помощью опции `autoupdate`.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "autoupdate": false
    }
```

Если вы не хотите получать обновления, но хотите получать уведомления о появлении новой версии, установите для `autoupdate` значение `"notify"`. Обратите внимание, что это работает только в том случае, если оно было установлено без использования менеджера пакетов, такого как Homebrew.

* * *

### Форматтеры

Вы можете настроить форматировщики кода с помощью опции `formatter`.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "formatter": {
        "prettier": {
          "disabled": true
        },
        "custom-prettier": {
          "command": ["npx", "prettier", "--write", "$FILE"],
          "environment": {
            "NODE_ENV": "development"
          },
          "extensions": [".js", ".ts", ".jsx", ".tsx"]
        }
      }
    }
```

[Подробнее о форматтерах можно узнать здесь](/docs/formatters).

* * *

### permission

По умолчанию opencode **разрешает все операции** , не требуя явного разрешения. Вы можете изменить это, используя опцию `permission`.

Например, чтобы гарантировать, что инструменты `edit` и `bash` требуют одобрения пользователя:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "permission": {
        "edit": "ask",
        "bash": "ask"
      }
    }
```

[Подробнее о разрешениях можно узнать здесь](/docs/permissions).

* * *

### compaction

Вы можете управлять поведением сжатия контекста с помощью опции `compaction`.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "compaction": {
        "auto": true,
        "prune": true
      }
    }
```

  * `auto` — автоматически сжимать сеанс при заполнении контекста (по умолчанию: `true`).
  * `prune` — удалить старые выходные данные инструмента для сохранения токенов (по умолчанию: `true`).



* * *

### watcher

Вы можете настроить шаблоны игнорирования средства отслеживания файлов с помощью опции `watcher`.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "watcher": {
        "ignore": ["node_modules/**", "dist/**", ".git/**"]
      }
    }
```

Шаблоны соответствуют синтаксису glob. Используйте это, чтобы исключить зашумленные каталоги из просмотра файлов.

* * *

### mcp

Вы можете настроить серверы MCP, которые хотите использовать, с помощью опции `mcp`.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "mcp": {}
    }
```

[Подробнее здесь](/docs/mcp-servers).

* * *

### Плагины

[Плагины](/docs/plugins) расширяют opencode с помощью пользовательских инструментов, перехватчиков и интеграций.

Поместите файлы плагина в `.opencode/plugins/` или `~/.config/opencode/plugins/`. Вы также можете загружать плагины из npm с помощью опции `plugin`.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "plugin": ["opencode-helicone-session", "@my-org/custom-plugin"]
    }
```

[Подробнее здесь](/docs/plugins).

* * *

### instructions

Вы можете настроить инструкции для используемой вами модели с помощью опции `instructions`.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "instructions": ["CONTRIBUTING.md", "docs/guidelines.md", ".cursor/rules/*.md"]
    }
```

Для этого требуется массив путей и шаблонов glob для файлов инструкций. [Подробнее о правилах читайте здесь](/docs/rules).

* * *

### disabled_providers

Вы можете отключить поставщиков, которые загружаются автоматически, с помощью опции `disabled_providers`. Это полезно, если вы хотите запретить загрузку определенных поставщиков, даже если их учетные данные доступны.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "disabled_providers": ["openai", "gemini"]
    }
```

Заметка

`disabled_providers` имеет приоритет над `enabled_providers`.

Опция `disabled_providers` принимает массив идентификаторов поставщиков. Когда провайдер отключен:

  * Он не будет загружен, даже если установлены переменные среды.
  * Он не будет загружен, даже если ключи API настроены с помощью команды `/connect`.
  * Модели поставщика не появятся в списке выбора моделей.



* * *

### enabled_providers

Вы можете указать белый список поставщиков с помощью опции `enabled_providers`. Если этот параметр установлен, будут включены только указанные поставщики, а все остальные будут игнорироваться.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "enabled_providers": ["anthropic", "openai"]
    }
```

Это полезно, если вы хотите ограничить opencode использованием только определенных поставщиков, а не отключать их по одному.

Заметка

`disabled_providers` имеет приоритет над `enabled_providers`.

Если поставщик указан как в `enabled_providers`, так и в `disabled_providers`, `disabled_providers` имеет приоритет для обратной совместимости.

* * *

### Экспериментальные возможности

Ключ `experimental` содержит параметры, находящиеся в активной разработке.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "experimental": {}
    }
```

Осторожно

Экспериментальные варианты не стабильны. Они могут быть изменены или удалены без предварительного уведомления.

* * *

## Переменные

Вы можете использовать подстановку переменных в файлах конфигурации для ссылки на переменные среды и содержимое файлов.

* * *

### Переменные окружения

Используйте `{env:VARIABLE_NAME}` для замены переменных среды:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "model": "{env:OPENCODE_MODEL}",
      "provider": {
        "anthropic": {
          "models": {},
          "options": {
            "apiKey": "{env:ANTHROPIC_API_KEY}"
          }
        }
      }
    }
```

Если переменная среды не установлена, она будет заменена пустой строкой.

* * *

### Файлы

Используйте `{file:path/to/file}` для замены содержимого файла:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "instructions": ["./custom-instructions.md"],
      "provider": {
        "openai": {
          "options": {
            "apiKey": "{file:~/.secrets/openai-key}"
          }
        }
      }
    }
```

Пути к файлам могут быть:

  * Относительно каталога файла конфигурации
  * Или абсолютные пути, начинающиеся с `/` или `~`.



Они полезны для:

  * Хранение конфиденциальных данных, таких как ключи API, в отдельных файлах.
  * Включая большие файлы инструкций, не загромождая вашу конфигурацию.
  * Совместное использование общих фрагментов конфигурации в нескольких файлах конфигурации.



[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/config.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-3"></a>
---
url: https://opencode.ai/docs/ru/providers/
---

# Провайдеры

Использование любого провайдера LLM в opencode.

opencode использует [AI SDK](https://ai-sdk.dev/) и [Models.dev](https://models.dev) для поддержки **более 75 поставщиков LLM** и поддерживает запуск локальных моделей.

Чтобы добавить провайдера, вам необходимо:

  1. Добавьте ключи API для провайдера с помощью команды `/connect`.
  2. Настройте провайдера в вашей конфигурации opencode.



* * *

### Учетные данные

Когда вы добавляете ключи API провайдера с помощью команды `/connect`, они сохраняются в `~/.local/share/opencode/auth.json`.

* * *

### Настройка

Вы можете настроить поставщиков через раздел `provider` в вашем opencode. конфиг.

* * *

#### Базовый URL

Вы можете настроить базовый URL-адрес для любого провайдера, установив параметр `baseURL`. Это полезно при использовании прокси-сервисов или пользовательских конечных точек.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "provider": {
        "anthropic": {
          "options": {
            "baseURL": "https://api.anthropic.com/v1"
          }
        }
      }
    }
```

* * *

## OpenCode Zen

OpenCode Zen — это список моделей, предоставленный командой opencode, которые были протестировано и проверено на хорошую работу с opencode. [Подробнее](/docs/zen).

Совет

Если вы новичок, мы рекомендуем начать с OpenCode Zen.

  1. Запустите команду `/connect` в TUI, выберите opencode и перейдите по адресу [opencode.ai/auth](https://opencode.ai/auth).
```
/connect
```

  2. Войдите в систему, добавьте свои платежные данные и скопируйте ключ API.

  3. Вставьте свой ключ API.
```
┌ API key
         │
         │
         └ enter
```

  4. Запустите `/models` в TUI, чтобы просмотреть список рекомендуемых нами моделей.
```
/models
```




Он работает как любой другой поставщик в opencode и его использование совершенно необязательно.

* * *

## Каталог

Рассмотрим некоторых провайдеров подробнее. Если вы хотите добавить провайдера в список, смело открывайте PR.

Заметка

Не видите здесь провайдера? Откройте PR.

* * *

### 302.AI

  1. Перейдите в консоль 302.AI](<https://302.ai/>), создайте учетную запись и сгенерируйте ключ API.

  2. Запустите команду `/connect` и найдите **302.AI**.
```
/connect
```

  3. Введите свой ключ API 302.AI.
```
┌ API key
         │
         │
         └ enter
```

  4. Запустите команду `/models`, чтобы выбрать модель.
```
/models
```




* * *

### Amazon Bedrock

Чтобы использовать Amazon Bedrock с opencode:

  1. Перейдите в **Каталог моделей** в консоли Amazon Bedrock и запросите доступ к нужным моделям.

Совет

Вам необходимо иметь доступ к нужной модели в Amazon Bedrock.

  2. **Настройте аутентификацию** одним из следующих способов:

#### Переменные среды (быстрый старт)

Установите одну из этих переменных среды при запуске opencode:

Окно терминала
```
# Option 1: Using AWS access keys
         AWS_ACCESS_KEY_ID=XXX AWS_SECRET_ACCESS_KEY=YYY opencode
         
         
         # Option 2: Using named AWS profile
         AWS_PROFILE=my-profile opencode
         
         
         # Option 3: Using Bedrock bearer token
         AWS_BEARER_TOKEN_BEDROCK=XXX opencode
```

Или добавьте их в свой профиль bash:

~/.bash_profile
```
export AWS_PROFILE=my-dev-profile
         export AWS_REGION=us-east-1
```

#### Файл конфигурации (рекомендуется)

Для конкретной или постоянной конфигурации проекта используйте `opencode.json`:

opencode.json
```
{
           "$schema": "https://opencode.ai/config.json",
           "provider": {
             "amazon-bedrock": {
               "options": {
                 "region": "us-east-1",
                 "profile": "my-aws-profile"
               }
             }
           }
         }
```

**Доступные варианты:**

     * `region` – регион AWS (например, `us-east-1`, `eu-west-1`).
     * `profile` – именованный профиль AWS из `~/.aws/credentials`.
     * `endpoint` — URL-адрес пользовательской конечной точки для конечных точек VPC (псевдоним для общей опции `baseURL`).

Совет

Параметры файла конфигурации имеют приоритет над переменными среды.

#### Дополнительно: конечные точки VPC

Если вы используете конечные точки VPC для Bedrock:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "provider": {
        "amazon-bedrock": {
          "options": {
            "region": "us-east-1",
            "profile": "production",
            "endpoint": "https://bedrock-runtime.us-east-1.vpce-xxxxx.amazonaws.com"
          }
        }
      }
    }
```

Заметка

Параметр `endpoint` — это псевдоним общего параметра `baseURL`, использующий терминологию, специфичную для AWS. Если указаны и `endpoint`, и `baseURL`, `endpoint` имеет приоритет.

#### Методы аутентификации

     * **`AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY`**: создайте пользователя IAM и сгенерируйте ключи доступа в консоли AWS.
     * **`AWS_PROFILE`** : использовать именованные профили из `~/.aws/credentials`. Сначала настройте `aws configure --profile my-profile` или `aws sso login`.
     * **`AWS_BEARER_TOKEN_BEDROCK`** : создание долгосрочных ключей API из консоли Amazon Bedrock.
     * **`AWS_WEB_IDENTITY_TOKEN_FILE`/`AWS_ROLE_ARN`**: для EKS IRSA (роли IAM для учетных записей служб) или других сред Kubernetes с федерацией OIDC. Эти переменные среды автоматически вводятся Kubernetes при использовании аннотаций учетной записи службы.

#### Приоритет аутентификации

Amazon Bedrock использует следующий приоритет аутентификации:

     1. **Токен носителя** — переменная среды `AWS_BEARER_TOKEN_BEDROCK` или токен из команды `/connect`.
     2. **Цепочка учетных данных AWS** — профиль, ключи доступа, общие учетные данные, роли IAM, токены веб-идентификации (EKS IRSA), метаданные экземпляра.

Заметка

Когда токен-носитель установлен (через `/connect` или `AWS_BEARER_TOKEN_BEDROCK`), он имеет приоритет над всеми методами учетных данных AWS, включая настроенные профили.

  3. Запустите команду `/models`, чтобы выбрать нужную модель.
```
/models
```




Заметка

Для пользовательских профилей вывода используйте имя модели и поставщика в ключе и задайте для свойства `id` значение arn. Это обеспечивает правильное кэширование:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "provider": {
        "amazon-bedrock": {
          // ...
          "models": {
            "anthropic-claude-sonnet-4.5": {
              "id": "arn:aws:bedrock:us-east-1:xxx:application-inference-profile/yyy"
            }
          }
        }
      }
    }
```

* * *

### Anthropic

  1. После регистрации введите команду `/connect` и выберите Anthropic.
```
/connect
```

  2. Здесь вы можете выбрать опцию **Claude Pro/Max** , и ваш браузер откроется. и попросите вас пройти аутентификацию.
```
┌ Select auth method
         │
         │ Claude Pro/Max
         │ Create an API Key
         │ Manually enter API Key
         └
```

  3. Теперь все модели Anthropic должны быть доступны при использовании команды `/models`.
```
/models
```




Использование вашей подписки Claude Pro/Max в opencode официально не поддерживается [Anthropic](https://anthropic.com).

##### Использование ключей API

Вы также можете выбрать **Создать ключ API** , если у вас нет подписки Pro/Max. Он также откроет ваш браузер и попросит вас войти в Anthropic и предоставит вам код, который вы можете вставить в свой терминал.

Или, если у вас уже есть ключ API, вы можете выбрать **Ввести ключ API вручную** и вставить его в свой терминал.

* * *

### Azure OpenAI

Заметка

Если вы столкнулись с ошибками «Извините, но я не могу помочь с этим запросом», попробуйте изменить фильтр содержимого с **DefaultV2** на **Default** в своем ресурсе Azure.

  1. Перейдите на [портал Azure](https://portal.azure.com/) и создайте ресурс **Azure OpenAI**. Вам понадобится:

     * **Имя ресурса** : оно становится частью вашей конечной точки API (`https://RESOURCE_NAME.openai.azure.com/`).
     * **Ключ API** : `KEY 1` или `KEY 2` из вашего ресурса.
  2. Перейдите в [Azure AI Foundry](https://ai.azure.com/) и разверните модель.

:::примечание Для правильной работы opencode имя развертывания должно совпадать с именем модели. :::

  3. Запустите команду `/connect` и найдите **Azure**.
```
/connect
```

  4. Введите свой ключ API.
```
┌ API key
         │
         │
         └ enter
```

  5. Задайте имя ресурса как переменную среды:

Окно терминала
```
AZURE_RESOURCE_NAME=XXX opencode
```

Или добавьте его в свой профиль bash:

~/.bash_profile
```
export AZURE_RESOURCE_NAME=XXX
```

  6. Запустите команду `/models`, чтобы выбрать развернутую модель.
```
/models
```




* * *

### Azure Cognitive Services

  1. Перейдите на [портал Azure](https://portal.azure.com/) и создайте ресурс **Azure OpenAI**. Вам понадобится:

     * **Имя ресурса** : оно становится частью вашей конечной точки API (`https://AZURE_COGNITIVE_SERVICES_RESOURCE_NAME.cognitiveservices.azure.com/`).
     * **Ключ API** : `KEY 1` или `KEY 2` из вашего ресурса.
  2. Перейдите в [Azure AI Foundry](https://ai.azure.com/) и разверните модель.

:::примечание Для правильной работы opencode имя развертывания должно совпадать с именем модели. :::

  3. Запустите команду `/connect` и найдите **Azure Cognitive Services**.
```
/connect
```

  4. Введите свой ключ API.
```
┌ API key
         │
         │
         └ enter
```

  5. Задайте имя ресурса как переменную среды:

Окно терминала
```
AZURE_COGNITIVE_SERVICES_RESOURCE_NAME=XXX opencode
```

Или добавьте его в свой профиль bash:

~/.bash_profile
```
export AZURE_COGNITIVE_SERVICES_RESOURCE_NAME=XXX
```

  6. Запустите команду `/models`, чтобы выбрать развернутую модель.
```
/models
```




* * *

### Baseten

  1. Перейдите в [Baseten](https://app.baseten.co/), создайте учетную запись и сгенерируйте ключ API.

  2. Запустите команду `/connect` и найдите **Baseten**.
```
/connect
```

  3. Введите свой ключ API Baseten.
```
┌ API key
         │
         │
         └ enter
```

  4. Запустите команду `/models`, чтобы выбрать модель.
```
/models
```




* * *

### Cerebras

  1. Перейдите в [консоль Cerebras](https://inference.cerebras.ai/), создайте учетную запись и сгенерируйте ключ API.

  2. Запустите команду `/connect` и найдите **Cerebras**.
```
/connect
```

  3. Введите свой ключ API Cerebras.
```
┌ API key
         │
         │
         └ enter
```

  4. Запустите команду `/models`, чтобы выбрать такую ​​модель, как _Qwen 3 Coder 480B_.
```
/models
```




* * *

### Cloudflare AI Gateway

Cloudflare AI Gateway позволяет вам получать доступ к моделям OpenAI, Anthropic, Workers AI и т. д. через единую конечную точку. Благодаря [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/) вам не нужны отдельные ключи API для каждого провайдера.

  1. Перейдите на [панель управления Cloudflare](https://dash.cloudflare.com/), выберите **AI** > **AI Gateway** и создайте новый шлюз.

  2. Установите идентификатор своей учетной записи и идентификатор шлюза в качестве переменных среды.

~/.bash_profile
```
export CLOUDFLARE_ACCOUNT_ID=your-32-character-account-id
         export CLOUDFLARE_GATEWAY_ID=your-gateway-id
```

  3. Запустите команду `/connect` и найдите **Cloudflare AI Gateway**.
```
/connect
```

  4. Введите свой токен API Cloudflare.
```
┌ API key
         │
         │
         └ enter
```

Или установите его как переменную среды.

~/.bash_profile
```
export CLOUDFLARE_API_TOKEN=your-api-token
```

  5. Запустите команду `/models`, чтобы выбрать модель.
```
/models
```

Вы также можете добавлять модели через конфигурацию opencode.

opencode.json
```
{
           "$schema": "https://opencode.ai/config.json",
           "provider": {
             "cloudflare-ai-gateway": {
               "models": {
                 "openai/gpt-4o": {},
                 "anthropic/claude-sonnet-4": {}
               }
             }
           }
         }
```




* * *

### Cortecs

  1. Перейдите в [консоль Cortecs](https://cortecs.ai/), создайте учетную запись и сгенерируйте ключ API.

  2. Запустите команду `/connect` и найдите **Cortecs**.
```
/connect
```

  3. Введите свой ключ API Cortecs.
```
┌ API key
         │
         │
         └ enter
```

  4. Запустите команду `/models`, чтобы выбрать такую ​​модель, как _Kimi K2 Instruct_.
```
/models
```




* * *

### DeepSeek

  1. Перейдите в [консоль DeepSeek](https://platform.deepseek.com/), создайте учетную запись и нажмите **Создать новый ключ API**.

  2. Запустите команду `/connect` и найдите **DeepSeek**.
```
/connect
```

  3. Введите свой ключ API DeepSeek.
```
┌ API key
         │
         │
         └ enter
```

  4. Запустите команду `/models`, чтобы выбрать модель DeepSeek, например _DeepSeek Reasoner_.
```
/models
```




* * *

### Deep Infra

  1. Перейдите на панель мониторинга Deep Infra](<https://deepinfra.com/dash>), создайте учетную запись и сгенерируйте ключ API.

  2. Запустите команду `/connect` и найдите **Deep Infra**.
```
/connect
```

  3. Введите свой ключ API Deep Infra.
```
┌ API key
         │
         │
         └ enter
```

  4. Запустите команду `/models`, чтобы выбрать модель.
```
/models
```




* * *

### Firmware

  1. Перейдите на [панель Firmware](https://app.firmware.ai/signup), создайте учетную запись и сгенерируйте ключ API.

  2. Запустите команду `/connect` и найдите **Firmware**.
```
/connect
```

  3. Введите ключ API Firmware.
```
┌ API key
         │
         │
         └ enter
```

  4. Запустите команду `/models`, чтобы выбрать модель.
```
/models
```




* * *

### Fireworks AI

  1. Перейдите в [консоль Fireworks AI](https://app.fireworks.ai/), создайте учетную запись и нажмите **Создать ключ API**.

  2. Запустите команду `/connect` и найдите **Fireworks AI**.
```
/connect
```

  3. Введите ключ API Fireworks AI.
```
┌ API key
         │
         │
         └ enter
```

  4. Запустите команду `/models`, чтобы выбрать такую ​​модель, как _Kimi K2 Instruct_.
```
/models
```




* * *

### GitLab Duo

GitLab Duo предоставляет агентский чат на базе искусственного интеллекта со встроенными возможностями вызова инструментов через прокси-сервер GitLab Anthropic.

  1. Запустите команду `/connect` и выберите GitLab.
```
/connect
```

  2. Выберите метод аутентификации:
```
┌ Select auth method
         │
         │ OAuth (Recommended)
         │ Personal Access Token
         └
```

#### Использование OAuth (рекомендуется)

Выберите **OAuth** , и ваш браузер откроется для авторизации.

#### Использование токена личного доступа

     1. Перейдите в [Настройки пользователя GitLab > Токены доступа](https://gitlab.com/-/user_settings/personal_access_tokens).
     2. Нажмите **Добавить новый токен**.
     3. Имя: `OpenCode`, Области применения: `api`
     4. Скопируйте токен (начинается с `glpat-`)
     5. Введите его в терминал
  3. Запустите команду `/models`, чтобы просмотреть доступные модели.
```
/models
```

Доступны три модели на основе Claude:

     * **duo-chat-haiku-4-5** (по умолчанию) — быстрые ответы на быстрые задачи.
     * **duo-chat-sonnet-4-5** — сбалансированная производительность для большинства рабочих процессов.
     * **duo-chat-opus-4-5** — Наиболее способен к комплексному анализу.



Заметка

Вы также можете указать переменную среды «GITLAB_TOKEN», если не хотите. для хранения токена в хранилище аутентификации opencode.

##### Самостоятельная GitLab

примечание о соответствии

opencode использует небольшую модель для некоторых задач ИИ, таких как создание заголовка сеанса. По умолчанию он настроен на использование gpt-5-nano, размещенного на Zen. Чтобы заблокировать opencode чтобы использовать только свой собственный экземпляр, размещенный на GitLab, добавьте следующее в свой `opencode.json` файл. Также рекомендуется отключить совместное использование сеансов.
```
{
      "$schema": "https://opencode.ai/config.json",
      "small_model": "gitlab/duo-chat-haiku-4-5",
      "share": "disabled"
    }
```

Для самостоятельных экземпляров GitLab:

Окно терминала
```
export GITLAB_INSTANCE_URL=https://gitlab.company.com
    export GITLAB_TOKEN=glpat-...
```

Если в вашем экземпляре используется собственный AI-шлюз:

Окно терминала
```
GITLAB_AI_GATEWAY_URL=https://ai-gateway.company.com
```

Или добавьте в свой профиль bash:

~/.bash_profile
```
export GITLAB_INSTANCE_URL=https://gitlab.company.com
    export GITLAB_AI_GATEWAY_URL=https://ai-gateway.company.com
    export GITLAB_TOKEN=glpat-...
```

Заметка

Ваш администратор GitLab должен включить следующее:

  1. [Платформа Duo Agent](https://docs.gitlab.com/user/gitlab_duo/turn_on_off/) для пользователя, группы или экземпляра
  2. Флаги функций (через консоль Rails): 
     * `agent_platform_claude_code`
     * `third_party_agents_enabled`



##### OAuth для локальных экземпляров

Чтобы Oauth работал на вашем локальном экземпляре, вам необходимо создать новое приложение (Настройки → Приложения) с URL обратного вызова `http://127.0.0.1:8080/callback` и следующие области:

  * API (Доступ к API от вашего имени)
  * read_user (прочитать вашу личную информацию)
  * read_repository (разрешает доступ к репозиторию только для чтения)



Затем укажите идентификатор приложения как переменную среды:

Окно терминала
```
export GITLAB_OAUTH_CLIENT_ID=your_application_id_here
```

Дополнительная документация на домашней странице [opencode-gitlab-auth](https://www.npmjs.com/package/@gitlab/opencode-gitlab-auth).

##### Конфигурация

Настройте через `opencode.json`:

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "provider": {
        "gitlab": {
          "options": {
            "instanceUrl": "https://gitlab.com",
            "featureFlags": {
              "duo_agent_platform_agentic_chat": true,
              "duo_agent_platform": true
            }
          }
        }
      }
    }
```

##### Инструменты API GitLab (необязательно, но настоятельно рекомендуется)

Чтобы получить доступ к инструментам GitLab (мерж-реквесты, задачи, конвейеры, CI/CD и т. д.):

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "plugin": ["@gitlab/opencode-gitlab-plugin"]
    }
```

Этот плагин предоставляет комплексные возможности управления репозиторием GitLab, включая проверки MR, отслеживание проблем, мониторинг конвейера и многое другое.

* * *

### GitHub Copilot

Чтобы использовать подписку GitHub Copilot с открытым кодом:

Заметка

Некоторым моделям может потребоваться [Pro+ подписка](https://github.com/features/copilot/plans) для использования.

Некоторые модели необходимо включить вручную в настройках [GitHub Copilot](https://docs.github.com/en/copilot/how-tos/use-ai-models/configure-access-to-ai-models#setup-for-individual-use).

  1. Запустите команду `/connect` и найдите GitHub Copilot.
```
/connect
```

  2. Перейдите на [github.com/login/device](https://github.com/login/device) и введите код.
```
┌ Login with GitHub Copilot
         │
         │ https://github.com/login/device
         │
         │ Enter code: 8F43-6FCF
         │
         └ Waiting for authorization...
```

  3. Теперь запустите команду `/models`, чтобы выбрать нужную модель.
```
/models
```




* * *

### Google Vertex AI

Чтобы использовать Google Vertex AI с opencode:

  1. Перейдите в **Model Garden** в Google Cloud Console и проверьте модели, доступные в вашем регионе.

Заметка

Вам необходим проект Google Cloud с включенным Vertex AI API.

  2. Установите необходимые переменные среды:

     * `GOOGLE_CLOUD_PROJECT`: идентификатор вашего проекта Google Cloud.
     * `VERTEX_LOCATION` (необязательно): регион для Vertex AI (по умолчанию `global`).
     * Аутентификация (выберите одну): 
       * `GOOGLE_APPLICATION_CREDENTIALS`: путь к ключевому файлу JSON вашего сервисного аккаунта.
       * Аутентификация через CLI gcloud: `gcloud auth application-default login`.

Установите их во время запуска opencode.

Окно терминала
```
GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json GOOGLE_CLOUD_PROJECT=your-project-id opencode
```

Или добавьте их в свой профиль bash.

~/.bash_profile
```
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json
    export GOOGLE_CLOUD_PROJECT=your-project-id
    export VERTEX_LOCATION=global
```




Совет

Регион `global` повышает доступность и уменьшает количество ошибок без дополнительных затрат. Используйте региональные конечные точки (например, `us-central1`) для требований к местонахождению данных. [Подробнее](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-partner-models#regional_and_global_endpoints)

  3. Запустите команду `/models`, чтобы выбрать нужную модель.
```
/models
```




* * *

### Groq

  1. Перейдите в консоль Groq](<https://console.groq.com/>), нажмите **Создать ключ API** и скопируйте ключ.

  2. Запустите команду `/connect` и найдите Groq.
```
/connect
```

  3. Введите ключ API для провайдера.
```
┌ API key
         │
         │
         └ enter
```

  4. Запустите команду `/models`, чтобы выбрать тот, который вам нужен.
```
/models
```




* * *

### Hugging Face

[Hugging Face Inference Providers](https://huggingface.co/docs/inference-providers) предоставляют доступ к открытым моделям, поддерживаемым более чем 17 поставщиками.

  1. Перейдите в [Настройки Hugging Face](https://huggingface.co/settings/tokens/new?ownUserPermissions=inference.serverless.write&tokenType=fineGrained), чтобы создать токен с разрешением совершать вызовы к поставщикам выводов.

  2. Запустите команду `/connect` и найдите **Hugging Face**.
```
/connect
```

  3. Введите свой токен Hugging Face.
```
┌ API key
         │
         │
         └ enter
```

  4. Запустите команду `/models`, чтобы выбрать такую ​​модель, как _Kimi-K2-Instruct_ или _GLM-4.6_.
```
/models
```




* * *

### Helicone

[Helicone](https://helicone.ai) — это платформа наблюдения LLM, которая обеспечивает ведение журнала, мониторинг и аналитику для ваших приложений искусственного интеллекта. Helicone AI Gateway автоматически направляет ваши запросы соответствующему поставщику на основе модели.

  1. Перейдите в [Helicone](https://helicone.ai), создайте учетную запись и сгенерируйте ключ API на своей панели управления.

  2. Запустите команду `/connect` и найдите **Helicone**.
```
/connect
```

  3. Введите свой ключ API Helicone.
```
┌ API key
         │
         │
         └ enter
```

  4. Запустите команду `/models`, чтобы выбрать модель.
```
/models
```




Дополнительные сведения о дополнительных провайдерах и расширенных функциях, таких как кэширование и ограничение скорости, см. в [Документация Helicone](https://docs.helicone.ai).

#### Дополнительные конфигурации

Если вы видите функцию или модель от Helicone, которая не настраивается автоматически через opencode, вы всегда можете настроить ее самостоятельно.

Вот [Справочник моделей Helicone](https://helicone.ai/models), он понадобится вам, чтобы получить идентификаторы моделей, которые вы хотите добавить.

~/.config/opencode/opencode.jsonc
```
{
      "$schema": "https://opencode.ai/config.json",
      "provider": {
        "helicone": {
          "npm": "@ai-sdk/openai-compatible",
          "name": "Helicone",
          "options": {
            "baseURL": "https://ai-gateway.helicone.ai",
          },
          "models": {
            "gpt-4o": {
              // Model ID (from Helicone's model directory page)
              "name": "GPT-4o", // Your own custom name for the model
            },
            "claude-sonnet-4-20250514": {
              "name": "Claude Sonnet 4",
            },
          },
        },
      },
    }
```

#### Пользовательские заголовки

Helicone поддерживает пользовательские заголовки для таких функций, как кэширование, отслеживание пользователей и управление сеансами. Добавьте их в конфигурацию вашего провайдера, используя `options.headers`:

~/.config/opencode/opencode.jsonc
```
{
      "$schema": "https://opencode.ai/config.json",
      "provider": {
        "helicone": {
          "npm": "@ai-sdk/openai-compatible",
          "name": "Helicone",
          "options": {
            "baseURL": "https://ai-gateway.helicone.ai",
            "headers": {
              "Helicone-Cache-Enabled": "true",
              "Helicone-User-Id": "opencode",
            },
          },
        },
      },
    }
```

##### Отслеживание сеансов

Функция Helicone [Sessions](https://docs.helicone.ai/features/sessions) позволяет группировать связанные запросы LLM вместе. Используйте плагин [opencode-helicone-session](https://github.com/H2Shami/opencode-helicone-session), чтобы автоматически регистрировать каждый диалог opencode как сеанс в Helicone.

Окно терминала
```
npm install -g opencode-helicone-session
```

Добавьте его в свою конфигурацию.

opencode.json
```
{
      "plugin": ["opencode-helicone-session"]
    }
```

Плагин вставляет в ваши запросы заголовки `Helicone-Session-Id` и `Helicone-Session-Name`. На странице «Сеансы» Helicone вы увидите каждый диалог opencode, указанный как отдельный сеанс.

##### Общие разъемы Helicone

Заголовок| Описание  
---|---  
`Helicone-Cache-Enabled`| Включить кэширование ответов (`true`/`false`)  
`Helicone-User-Id`| Отслеживание показателей по пользователю  
`Helicone-Property-[Name]`| Добавьте пользовательские свойства (например, `Helicone-Property-Environment`)  
`Helicone-Prompt-Id`| Связывание запросов с версиями промптов  
  
См. [Справочник заголовков Helicone](https://docs.helicone.ai/helicone-headers/header-directory) для всех доступных заголовков.

* * *

### llama.cpp

Вы можете настроить opencode для использования локальных моделей с помощью [утилиты llama-server llama.cpp’s](https://github.com/ggml-org/llama.cpp)

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "provider": {
        "llama.cpp": {
          "npm": "@ai-sdk/openai-compatible",
          "name": "llama-server (local)",
          "options": {
            "baseURL": "http://127.0.0.1:8080/v1"
          },
          "models": {
            "qwen3-coder:a3b": {
              "name": "Qwen3-Coder: a3b-30b (local)",
              "limit": {
                "context": 128000,
                "output": 65536
              }
            }
          }
        }
      }
    }
```

В этом примере:

  * `llama.cpp` — это идентификатор пользовательского поставщика. Это может быть любая строка, которую вы хотите.
  * `npm` указывает пакет, который будет использоваться для этого поставщика. Здесь `@ai-sdk/openai-compatible` используется для любого API-интерфейса, совместимого с OpenAI.
  * `name` — это отображаемое имя поставщика в пользовательском интерфейсе.
  * `options.baseURL` — конечная точка локального сервера.
  * `models` — это карта идентификаторов моделей с их конфигурациями. Название модели будет отображаться в списке выбора модели.



* * *

### IO.NET

IO.NET предлагает 17 моделей, оптимизированных для различных случаев использования:

  1. Перейдите в консоль IO.NET](<https://ai.io.net/>), создайте учетную запись и сгенерируйте ключ API.

  2. Запустите команду `/connect` и найдите **IO.NET**.
```
/connect
```

  3. Введите свой ключ API IO.NET.
```
┌ API key
         │
         │
         └ enter
```

  4. Запустите команду `/models`, чтобы выбрать модель.
```
/models
```




* * *

### LM Studio

Вы можете настроить opencode для использования локальных моделей через LM Studio.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "provider": {
        "lmstudio": {
          "npm": "@ai-sdk/openai-compatible",
          "name": "LM Studio (local)",
          "options": {
            "baseURL": "http://127.0.0.1:1234/v1"
          },
          "models": {
            "google/gemma-3n-e4b": {
              "name": "Gemma 3n-e4b (local)"
            }
          }
        }
      }
    }
```

В этом примере:

  * `lmstudio` — это идентификатор пользовательского поставщика. Это может быть любая строка, которую вы хотите.
  * `npm` указывает пакет, который будет использоваться для этого поставщика. Здесь `@ai-sdk/openai-compatible` используется для любого API-интерфейса, совместимого с OpenAI.
  * `name` — это отображаемое имя поставщика в пользовательском интерфейсе.
  * `options.baseURL` — конечная точка локального сервера.
  * `models` — это карта идентификаторов моделей с их конфигурациями. Название модели будет отображаться в списке выбора модели.



* * *

### Moonshot AI

Чтобы использовать Кими К2 из Moonshot AI:

  1. Перейдите в [консоль Moonshot AI](https://platform.moonshot.ai/console), создайте учетную запись и нажмите **Создать ключ API**.

  2. Запустите команду `/connect` и найдите **Moonshot AI**.
```
/connect
```

  3. Введите свой API-ключ Moonshot.
```
┌ API key
         │
         │
         └ enter
```

  4. Запустите команду `/models`, чтобы выбрать _Kimi K2_.
```
/models
```




* * *

### MiniMax

  1. Перейдите в [консоль API MiniMax](https://platform.minimax.io/login), создайте учетную запись и сгенерируйте ключ API.

  2. Запустите команду `/connect` и найдите **MiniMax**.
```
/connect
```

  3. Введите свой ключ API MiniMax.
```
┌ API key
         │
         │
         └ enter
```

  4. Запустите команду `/models`, чтобы выбрать модель типа _M2.1_.
```
/models
```




* * *

### Nebius Token Factory

  1. Перейдите в консоль Nebius Token Factory](<https://tokenfactory.nebius.com/>), создайте учетную запись и нажмите **Добавить ключ**.

  2. Запустите команду `/connect` и найдите **Nebius Token Factory**.
```
/connect
```

  3. Введите ключ API фабрики токенов Nebius.
```
┌ API key
         │
         │
         └ enter
```

  4. Запустите команду `/models`, чтобы выбрать такую ​​модель, как _Kimi K2 Instruct_.
```
/models
```




* * *

### Ollama

Вы можете настроить opencode для использования локальных моделей через Ollama.

Совет

Ollama может автоматически настроиться для opencode. Подробности см. в документации по интеграции Ollama](<https://docs.ollama.com/integrations/opencode>).

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "provider": {
        "ollama": {
          "npm": "@ai-sdk/openai-compatible",
          "name": "Ollama (local)",
          "options": {
            "baseURL": "http://localhost:11434/v1"
          },
          "models": {
            "llama2": {
              "name": "Llama 2"
            }
          }
        }
      }
    }
```

В этом примере:

  * `ollama` — это идентификатор пользовательского поставщика. Это может быть любая строка, которую вы хотите.
  * `npm` указывает пакет, который будет использоваться для этого поставщика. Здесь `@ai-sdk/openai-compatible` используется для любого API-интерфейса, совместимого с OpenAI.
  * `name` — это отображаемое имя поставщика в пользовательском интерфейсе.
  * `options.baseURL` — конечная точка локального сервера.
  * `models` — это карта идентификаторов моделей с их конфигурациями. Название модели будет отображаться в списке выбора модели.



Совет

Если вызовы инструментов не работают, попробуйте увеличить `num_ctx` в Олламе. Начните с 16–32 тысяч.

* * *

### Ollama Cloud

Чтобы использовать Ollama Cloud с opencode:

  1. Перейдите на <https://ollama.com/> и войдите в систему или создайте учетную запись.

  2. Перейдите в **Настройки** > **Ключи** и нажмите **Добавить ключ API** , чтобы создать новый ключ API.

  3. Скопируйте ключ API для использования в opencode.

  4. Запустите команду `/connect` и найдите **Ollama Cloud**.
```
/connect
```

  5. Введите свой ключ API Ollama Cloud.
```
┌ API key
         │
         │
         └ enter
```

  6. **Важно**. Перед использованием облачных моделей в opencode необходимо получить информацию о модели локально:

Окно терминала
```
ollama pull gpt-oss:20b-cloud
```

  7. Запустите команду `/models`, чтобы выбрать модель облака Ollama.
```
/models
```




* * *

### OpenAI

Мы рекомендуем подписаться на [ChatGPT Plus или Pro](https://chatgpt.com/pricing).

  1. После регистрации выполните команду `/connect` и выберите OpenAI.
```
/connect
```

  2. Здесь вы можете выбрать опцию **ChatGPT Plus/Pro** , и ваш браузер откроется. и попросите вас пройти аутентификацию.
```
┌ Select auth method
         │
         │ ChatGPT Plus/Pro
         │ Manually enter API Key
         └
```

  3. Теперь все модели OpenAI должны быть доступны при использовании команды `/models`.
```
/models
```




##### Использование ключей API

Если у вас уже есть ключ API, вы можете выбрать **Ввести ключ API вручную** и вставить его в свой терминал.

* * *

### OpenCode Zen

OpenCode Zen — это список протестированных и проверенных моделей, предоставленный командой opencode. [Подробнее](/docs/zen).

  1. Войдите в систему **[OpenCode Zen](https://opencode.ai/auth)** и нажмите **Создать ключ API**.

  2. Запустите команду `/connect` и найдите **OpenCode Zen**.
```
/connect
```

  3. Введите свой ключ API opencode.
```
┌ API key
         │
         │
         └ enter
```

  4. Запустите команду `/models`, чтобы выбрать такую ​​модель, как _Qwen 3 Coder 480B_.
```
/models
```




* * *

### OpenRouter

  1. Перейдите на панель управления OpenRouter](<https://openrouter.ai/settings/keys>), нажмите **Создать ключ API** и скопируйте ключ.

  2. Запустите команду `/connect` и найдите OpenRouter.
```
/connect
```

  3. Введите ключ API для провайдера.
```
┌ API key
         │
         │
         └ enter
```

  4. Многие модели OpenRouter предварительно загружены по умолчанию. Запустите команду `/models`, чтобы выбрать нужную.
```
/models
```

Вы также можете добавить дополнительные модели через конфигурацию opencode.

opencode.json
```
{
           "$schema": "https://opencode.ai/config.json",
           "provider": {
             "openrouter": {
               "models": {
                 "somecoolnewmodel": {}
               }
             }
           }
         }
```

  5. Вы также можете настроить их через конфигурацию opencode. Вот пример указания провайдера

opencode.json
```
{
           "$schema": "https://opencode.ai/config.json",
           "provider": {
             "openrouter": {
               "models": {
                 "moonshotai/kimi-k2": {
                   "options": {
                     "provider": {
                       "order": ["baseten"],
                       "allow_fallbacks": false
                     }
                   }
                 }
               }
             }
           }
         }
```




* * *

### SAP AI Core

SAP AI Core предоставляет доступ к более чем 40 моделям от OpenAI, Anthropic, Google, Amazon, Meta, Mistral и AI21 через единую платформу.

  1. Перейдите в [SAP BTP Cockpit](https://account.hana.ondemand.com/), перейдите к экземпляру службы SAP AI Core и создайте ключ службы.

Совет

Ключ службы — это объект JSON, содержащий `clientid`, `clientsecret`, `url` и `serviceurls.AI_API_URL`. Экземпляр AI Core можно найти в разделе **Сервисы** > **Экземпляры и подписки** в панели управления BTP.

  2. Запустите команду `/connect` и найдите **SAP AI Core**.
```
/connect
```

  3. Введите свой сервисный ключ в формате JSON.
```
┌ Service key
         │
         │
         └ enter
```

Или установите переменную среды `AICORE_SERVICE_KEY`:

Окно терминала
```
AICORE_SERVICE_KEY='{"clientid":"...","clientsecret":"...","url":"...","serviceurls":{"AI_API_URL":"..."}}' opencode
```

Или добавьте его в свой профиль bash:

~/.bash_profile
```
export AICORE_SERVICE_KEY='{"clientid":"...","clientsecret":"...","url":"...","serviceurls":{"AI_API_URL":"..."}}'
```

  4. При необходимости укажите идентификатор развертывания и группу ресурсов:

Окно терминала
```
AICORE_DEPLOYMENT_ID=your-deployment-id AICORE_RESOURCE_GROUP=your-resource-group opencode
```

Заметка

Эти параметры являются необязательными и должны быть настроены в соответствии с настройками SAP AI Core.

  5. Запустите команду `/models`, чтобы выбрать одну из более чем 40 доступных моделей.
```
/models
```




* * *

### OVHcloud AI Endpoints

  1. Перейдите к [OVHcloud Panel](https://ovh.com/manager). Перейдите в раздел `Public Cloud`, `AI & Machine Learning` > `AI Endpoints` и на вкладке `API Keys` нажмите **Создать новый ключ API**.

  2. Запустите команду `/connect` и найдите **Конечные точки OVHcloud AI**.
```
/connect
```

  3. Введите ключ API конечных точек OVHcloud AI.
```
┌ API key
         │
         │
         └ enter
```

  4. Запустите команду `/models`, чтобы выбрать модель типа _gpt-oss-120b_.
```
/models
```




* * *

### Scaleway

Чтобы использовать [Scaleway Generative APIs](https://www.scaleway.com/en/docs/generative-apis/) с opencode:

  1. Перейдите к [Настройки IAM консоли Scaleway](https://console.scaleway.com/iam/api-keys), чтобы сгенерировать новый ключ API.

  2. Запустите команду `/connect` и найдите **Scaleway**.
```
/connect
```

  3. Введите ключ API Scaleway.
```
┌ API key
         │
         │
         └ enter
```

  4. Запустите команду `/models`, чтобы выбрать модель, например _devstral-2-123b-instruct-2512_ или _gpt-oss-120b_.
```
/models
```




* * *

### Together AI

  1. Перейдите в [консоль Together AI](https://api.together.ai), создайте учетную запись и нажмите **Добавить ключ**.

  2. Запустите команду `/connect` и найдите **Together AI**.
```
/connect
```

  3. Введите ключ API Together AI.
```
┌ API key
         │
         │
         └ enter
```

  4. Запустите команду `/models`, чтобы выбрать такую ​​модель, как _Kimi K2 Instruct_.
```
/models
```




* * *

### Venice AI

  1. Перейдите к [консоли Venice AI](https://venice.ai), создайте учетную запись и сгенерируйте ключ API.

  2. Запустите команду `/connect` и найдите **Venice AI**.
```
/connect
```

  3. Введите свой ключ API Venice AI.
```
┌ API key
         │
         │
         └ enter
```

  4. Запустите команду `/models`, чтобы выбрать модель типа _Llama 3.3 70B_.
```
/models
```




* * *

### Vercel AI Gateway

Vercel AI Gateway позволяет получать доступ к моделям OpenAI, Anthropic, Google, xAI и других источников через единую конечную точку. Модели предлагаются по прейскурантной цене без наценок.

  1. Перейдите на [панель мониторинга Vercel](https://vercel.com/), перейдите на вкладку **AI Gateway** и нажмите **Ключи API** , чтобы создать новый ключ API.

  2. Запустите команду `/connect` и найдите **Vercel AI Gateway**.
```
/connect
```

  3. Введите ключ API Vercel AI Gateway.
```
┌ API key
         │
         │
         └ enter
```

  4. Запустите команду `/models`, чтобы выбрать модель.
```
/models
```




Вы также можете настраивать модели через конфигурацию opencode. Ниже приведен пример указания порядка маршрутизации поставщика.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "provider": {
        "vercel": {
          "models": {
            "anthropic/claude-sonnet-4": {
              "options": {
                "order": ["anthropic", "vertex"]
              }
            }
          }
        }
      }
    }
```

Некоторые полезные параметры маршрутизации:

Вариант| Описание  
---|---  
`order`| Последовательность провайдеров для попытки  
`only`| Ограничить конкретными провайдерами  
`zeroDataRetention`| Использовать только провайдеров с политикой нулевого хранения данных  
  
* * *

### xAI

  1. Перейдите на [консоль xAI](https://console.x.ai/), создайте учетную запись и сгенерируйте ключ API.

  2. Запустите команду `/connect` и найдите **xAI**.
```
/connect
```

  3. Введите свой ключ API xAI.
```
┌ API key
         │
         │
         └ enter
```

  4. Запустите команду `/models`, чтобы выбрать такую ​​модель, как _Grok Beta_.
```
/models
```




* * *

### Z.AI

  1. Перейдите в [консоль Z.AI API](https://z.ai/manage-apikey/apikey-list), создайте учетную запись и нажмите **Создать новый ключ API**.

  2. Запустите команду `/connect` и найдите **Z.AI**.
```
/connect
```

Если вы подписаны на **План кодирования GLM** , выберите **План кодирования Z.AI**.

  3. Введите свой ключ API Z.AI.
```
┌ API key
         │
         │
         └ enter
```

  4. Запустите команду `/models`, чтобы выбрать модель типа _GLM-4.7_.
```
/models
```




* * *

### ZenMux

  1. Перейдите на [панель управления ZenMux](https://zenmux.ai/settings/keys), нажмите **Создать ключ API** и скопируйте ключ.

  2. Запустите команду `/connect` и найдите ZenMux.
```
/connect
```

  3. Введите ключ API для провайдера.
```
┌ API key
         │
         │
         └ enter
```

  4. Многие модели ZenMux предварительно загружены по умолчанию. Запустите команду `/models`, чтобы выбрать нужную.
```
/models
```

Вы также можете добавить дополнительные модели через конфигурацию opencode.

opencode.json
```
{
           "$schema": "https://opencode.ai/config.json",
           "provider": {
             "zenmux": {
               "models": {
                 "somecoolnewmodel": {}
               }
             }
           }
         }
```




* * *

## Пользовательский поставщик

Чтобы добавить любого **совместимого с OpenAI** поставщика, не указанного в команде `/connect`:

Совет

Вы можете использовать любого OpenAI-совместимого провайдера с открытым кодом. Большинство современных поставщиков ИИ предлагают API-интерфейсы, совместимые с OpenAI.

  1. Запустите команду `/connect` и прокрутите вниз до пункта **Другое**.

Окно терминала
```
$ /connect
         
         
         ┌  Add credential
         │
         ◆  Select provider
         │  ...
         │  ● Other
         └
```

  2. Введите уникальный идентификатор провайдера.

Окно терминала
```
$ /connect
         
         
         ┌  Add credential
         │
         ◇  Enter provider id
         │  myprovider
         └
```

:::примечание Выберите запоминающийся идентификатор, вы будете использовать его в своем файле конфигурации. :::

  3. Введите свой ключ API для провайдера.

Окно терминала
```
$ /connect
         
         
         ┌  Add credential
         │
         ▲  This only stores a credential for myprovider - you will need to configure it in opencode.json, check the docs for examples.
         │
         ◇  Enter your API key
         │  sk-...
         └
```

  4. Создайте или обновите файл `opencode.json` в каталоге вашего проекта:

opencode.json
```
{
           "$schema": "https://opencode.ai/config.json",
           "provider": {
             "myprovider": {
               "npm": "@ai-sdk/openai-compatible",
               "name": "My AI ProviderDisplay Name",
               "options": {
                 "baseURL": "https://api.myprovider.com/v1"
               },
               "models": {
                 "my-model-name": {
                   "name": "My Model Display Name"
                 }
               }
             }
           }
         }
```

Вот варианты конфигурации:

     * **npm** : используемый пакет AI SDK, `@ai-sdk/openai-compatible` для поставщиков, совместимых с OpenAI.
     * **имя** : отображаемое имя в пользовательском интерфейсе.
     * **модели** : Доступные модели.
     * **options.baseURL** : URL-адрес конечной точки API.
     * **options.apiKey** : при необходимости установите ключ API, если не используется аутентификация.
     * **options.headers** : при необходимости можно установить собственные заголовки.

Подробнее о дополнительных параметрах в примере ниже.

  5. Запустите команду `/models`, и ваш пользовательский поставщик и модели появятся в списке выбора.




* * *

##### Пример

Ниже приведен пример настройки параметров `apiKey`, `headers` и модели `limit`.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "provider": {
        "myprovider": {
          "npm": "@ai-sdk/openai-compatible",
          "name": "My AI ProviderDisplay Name",
          "options": {
            "baseURL": "https://api.myprovider.com/v1",
            "apiKey": "{env:ANTHROPIC_API_KEY}",
            "headers": {
              "Authorization": "Bearer custom-token"
            }
          },
          "models": {
            "my-model-name": {
              "name": "My Model Display Name",
              "limit": {
                "context": 200000,
                "output": 65536
              }
            }
          }
        }
      }
    }
```

Детали конфигурации:

  * **apiKey** : устанавливается с использованием синтаксиса переменной `env`, [подробнее ](/docs/config#env-vars).
  * **заголовки** : пользовательские заголовки, отправляемые с каждым запросом.
  * **limit.context** : Максимальное количество входных токенов, которые принимает модель.
  * **limit.output** : Максимальное количество токенов, которые может сгенерировать модель.



Поля `limit` позволяют opencode понять, сколько контекста у вас осталось. Стандартные поставщики автоматически извлекают их из models.dev.

* * *

## Поиск неисправностей

Если у вас возникли проблемы с настройкой провайдера, проверьте следующее:

  1. **Проверьте настройку аутентификации** : запустите `opencode auth list`, чтобы проверить, верны ли учетные данные. для провайдера добавлены в ваш конфиг.

Это не относится к таким поставщикам, как Amazon Bedrock, которые для аутентификации полагаются на переменные среды.

  2. Для пользовательских поставщиков проверьте конфигурацию opencode и:

     * Убедитесь, что идентификатор провайдера, используемый в команде `/connect`, соответствует идентификатору в вашей конфигурации opencode.
     * Для провайдера используется правильный пакет npm. Например, используйте `@ai-sdk/cerebras` для Cerebras. А для всех других поставщиков, совместимых с OpenAI, используйте `@ai-sdk/openai-compatible`.
     * Убедитесь, что в поле `options.baseURL` используется правильная конечная точка API.



[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/providers.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-4"></a>
---
url: https://opencode.ai/docs/ru/network/
---

# Сеть

Настройте прокси и пользовательские сертификаты.

opencode поддерживает стандартные переменные среды прокси-сервера и пользовательские сертификаты для сетевых сред предприятия.

* * *

## Прокси

opencode учитывает стандартные переменные среды прокси.

Окно терминала
```
# HTTPS proxy (recommended)
    export HTTPS_PROXY=https://proxy.example.com:8080
    
    
    # HTTP proxy (if HTTPS not available)
    export HTTP_PROXY=http://proxy.example.com:8080
    
    
    # Bypass proxy for local server (required)
    export NO_PROXY=localhost,127.0.0.1
```

Осторожно

TUI взаимодействует с локальным HTTP-сервером. Вы должны обойти прокси-сервер для этого соединения, чтобы избежать петель маршрутизации.

Вы можете настроить порт и имя хоста сервера, используя [CLI flags](/docs/cli#run).

* * *

### Аутентификация

Если ваш прокси-сервер требует базовой аутентификации, включите учетные данные в URL-адрес.

Окно терминала
```
export HTTPS_PROXY=http://username:password@proxy.example.com:8080
```

Осторожно

Избегайте жесткого кодирования паролей. Используйте переменные среды или безопасное хранилище учетных данных.

Для прокси-серверов, требующих расширенной аутентификации, например NTLM или Kerberos, рассмотрите возможность использования шлюза LLM, поддерживающего ваш метод аутентификации.

* * *

## Пользовательские сертификаты

Если ваше предприятие использует собственные центры сертификации для HTTPS-соединений, настройте opencode, чтобы доверять им.

Окно терминала
```
export NODE_EXTRA_CA_CERTS=/path/to/ca-cert.pem
```

Это работает как для прокси-соединений, так и для прямого доступа к API.

[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/network.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-5"></a>
---
url: https://opencode.ai/docs/ru/enterprise/
---

# Корпоративное использование

Безопасное использование opencode в вашей организации.

opencode Enterprise предназначен для организаций, которые хотят быть уверены, что их код и данные никогда не покинут инфраструктуру. Это можно сделать с помощью централизованной конфигурации, которая интегрируется с вашим единым входом и внутренним шлюзом AI.

Заметка

opencode не хранит ваш код или контекстные данные.

Чтобы начать работу с opencode Enterprise:

  1. Проведите испытание внутри своей команды.
  2. **[Свяжитесь с нами](mailto:contact@anoma.ly)** , чтобы обсудить цены и варианты внедрения.



* * *

## Пробная версия

opencode имеет открытый исходный код и не хранит ваш код или контекстные данные, поэтому ваши разработчики могут просто [приступить к работе](/docs/) и провести пробную версию.

* * *

### Обработка данных

**opencode не хранит ваш код или контекстные данные.** Вся обработка происходит локально или посредством прямых вызовов API к вашему провайдеру ИИ.

Это означает, что пока вы используете поставщика, которому доверяете, или внутреннего Шлюз AI позволяет безопасно использовать opencode.

Единственное предостережение — это дополнительная функция `/share`.

* * *

#### Обмен беседами

Если пользователь включает функцию `/share`, разговор и связанные с ним данные отправляются в службу, которую мы используем для размещения этих общих страниц на opencode.ai.

В настоящее время данные передаются через периферийную сеть нашей CDN и кэшируются на периферии рядом с вашими пользователями.

Мы рекомендуем вам отключить эту функцию для пробной версии.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "share": "disabled"
    }
```

[Подробнее о совместном использовании](/docs/share).

* * *

### Владение кодом

**Вы являетесь владельцем всего кода, созданного opencode.** Никаких лицензионных ограничений или претензий на право собственности нет.

* * *

## Цены

Мы используем модель «на рабочее место» для opencode Enterprise. Если у вас есть собственный шлюз LLM, мы не взимаем плату за используемые токены. Для получения более подробной информации о ценах и вариантах реализации **[свяжитесь с нами](mailto:contact@anoma.ly)**.

* * *

## Развертывание

После завершения пробной версии и готовности использовать opencode на вашей организации, вы можете **[связаться с нами](mailto:contact@anoma.ly)** , чтобы обсудить цены и варианты реализации.

* * *

### Центральная конфигурация

Мы можем настроить opencode для использования единой центральной конфигурации для всей вашей организации.

Эта централизованная конфигурация может интегрироваться с вашим поставщиком единого входа и гарантирует всем пользователям доступ только к вашему внутреннему шлюзу AI.

* * *

### Интеграция SSO

Через центральную конфигурацию opencode может интегрироваться с провайдером единого входа вашей организации для аутентификации.

Это позволяет opencode получать учетные данные для вашего внутреннего шлюза AI через существующую систему управления идентификацией.

* * *

### Внутренний шлюз AI

Благодаря центральной конфигурации opencode также можно настроить на использование только вашего внутреннего шлюза AI.

Вы также можете отключить всех других поставщиков ИИ, гарантируя, что все запросы будут проходить через утвержденную инфраструктуру вашей организации.

* * *

### Самостоятельный хостинг

Хотя мы рекомендуем отключить страницы общего доступа, чтобы гарантировать, что ваши данные никогда не покинут вашу организацию, мы также можем помочь вам самостоятельно разместить их в вашей инфраструктуре.

В настоящее время это находится в нашей дорожной карте. Если вы заинтересованы, **[дайте нам знать](mailto:contact@anoma.ly)**.

* * *

## Часто задаваемые вопросы

Что такое opencode Enterprise?

opencode Enterprise предназначен для организаций, которые хотят быть уверены, что их код и данные никогда не покинут инфраструктуру. Это можно сделать с помощью централизованной конфигурации, которая интегрируется с вашим единым входом и внутренним шлюзом AI.

Как начать работу с opencode Enterprise?

Просто начните с внутреннего испытания со своей командой. opencode по умолчанию не сохраняет ваш код или контекстные данные, что упрощает начало работы.

Затем **[свяжитесь с нами](mailto:contact@anoma.ly)** , чтобы обсудить цены и варианты внедрения.

Как работает корпоративное ценообразование?

Мы предлагаем корпоративные цены за рабочее место. Если у вас есть собственный шлюз LLM, мы не взимаем плату за используемые токены. Для получения более подробной информации **[свяжитесь с нами](mailto:contact@anoma.ly)** , чтобы получить индивидуальное предложение, соответствующее потребностям вашей организации.

Защищены ли мои данные с помощью opencode Enterprise?

Да. opencode не хранит ваш код или контекстные данные. Вся обработка происходит локально или посредством прямых вызовов API вашего провайдера ИИ. Благодаря централизованной настройке и интеграции единого входа ваши данные остаются в безопасности в инфраструктуре вашей организации.

Можем ли мы использовать собственный частный реестр NPM?

opencode поддерживает частные реестры npm посредством встроенной поддержки файлов `.npmrc` Bun. Если ваша организация использует частный реестр, такой как JFrog Artifactory, Nexus или аналогичный, убедитесь, что разработчики прошли аутентификацию перед запуском opencode.

Чтобы настроить аутентификацию с помощью вашего частного реестра:

Окно терминала
[/code]
```
При этом создается `~/.npmrc` с данными аутентификации. opencode автоматически подхватит его.

Осторожно

Перед запуском opencode вы должны войти в частный реестр.

Альтернативно вы можете вручную настроить файл `.npmrc`:

~/.npmrc
```
[code]
Разработчики должны войти в частный реестр перед запуском opencode, чтобы гарантировать возможность установки пакетов из корпоративного реестра.

[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/enterprise.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-6"></a>
---
url: https://opencode.ai/docs/ru/troubleshooting/
---

# Поиск неисправностей

Распространенные проблемы и способы их решения.

Чтобы устранить проблемы с opencode, начните с проверки журналов и локальных данных, которые он хранит на диске.

* * *

## Журналы

Лог-файлы записываются в:

  * **macOS/Linux** : `~/.local/share/opencode/log/`
  * **Windows** : нажмите `WIN+R` и вставьте `%USERPROFILE%\.local\share\opencode\log`.



Файлам журналов присваиваются имена с метками времени (например, `2025-01-09T123456.log`), и сохраняются 10 последних файлов журналов.

Вы можете установить уровень журнала с помощью CLI-параметра `--log-level`, чтобы получить более подробную информацию об отладке. Например, `opencode --log-level DEBUG`.

* * *

## Хранилище

opencode хранит данные сеанса и другие данные приложения на диске по адресу:

  * **macOS/Linux** : `~/.local/share/opencode/`
  * **Windows** : нажмите `WIN+R` и вставьте `%USERPROFILE%\.local\share\opencode`.



Этот каталог содержит:

  * `auth.json` – данные аутентификации, такие как ключи API и токены OAuth.
  * `log/` – журналы приложений.
  * `project/` — данные, специфичные для проекта, такие как данные сеанса и сообщения. 
    * Если проект находится в репозитории Git, он хранится в `./<project-slug>/storage/`.
    * Если это не репозиторий Git, он хранится в `./global/storage/`.



* * *

## Настольное приложение

opencode Desktop запускает локальный сервер opencode (спутник `opencode-cli`) в фоновом режиме. Большинство проблем вызвано неправильно работающим плагином, поврежденным кешем или неверными настройками сервера.

### Быстрые проверки

  * Полностью закройте и перезапустите приложение.
  * Если приложение отображает экран с ошибкой, нажмите **Перезапустить** и скопируйте сведения об ошибке.
  * Только для macOS: меню `OpenCode` -> **Обновить веб-просмотр** (помогает, если пользовательский интерфейс пуст или завис).



* * *

### Отключить плагины

Если настольное приложение дает сбой при запуске, зависает или ведет себя странно, начните с отключения плагинов.

#### Проверьте глобальную конфигурацию

Откройте файл глобальной конфигурации и найдите ключ `plugin`.

  * **macOS/Linux** : `~/.config/opencode/opencode.jsonc` (или `~/.config/opencode/opencode.json`)
  * **macOS/Linux** (более ранние версии): `~/.local/share/opencode/opencode.jsonc`
  * **Windows** : нажмите `WIN+R` и вставьте `%USERPROFILE%\.config\opencode\opencode.jsonc`.



Если у вас настроены плагины, временно отключите их, удалив ключ или установив для него пустой массив:
```
{
      "$schema": "https://opencode.ai/config.json",
      "plugin": [],
    }
```

#### Проверьте каталоги плагинов

opencode также может загружать локальные плагины с диска. Временно переместите их в сторону (или переименуйте папку) и перезапустите настольное приложение:

  * **Глобальные плагины**
    * **macOS/Linux** : `~/.config/opencode/plugins/`
    * **Windows** : нажмите `WIN+R` и вставьте `%USERPROFILE%\.config\opencode\plugins`.
  * **Плагины проекта** (только если вы используете конфигурацию для каждого проекта) 
    * `<your-project>/.opencode/plugins/`



Если приложение снова начнет работать, повторно включите плагины по одному, чтобы определить, какой из них вызывает проблему.

* * *

### Очистить кеш

Если отключение плагинов не помогает (или установка плагина зависла), очистите кеш, чтобы opencode мог его пересобрать.

  1. Полностью закройте opencode Desktop.
  2. Удалите каталог кэша:


  * **macOS** : Finder -> `Cmd+Shift+G` -> вставить `~/.cache/opencode`.
  * **Linux** : удалите `~/.cache/opencode` (или запустите `rm -rf ~/.cache/opencode`).
  * **Windows** : нажмите `WIN+R` и вставьте `%USERPROFILE%\.cache\opencode`.


  3. Перезапустите рабочий стол opencode.



* * *

### Исправить проблемы с подключением к серверу

opencode Desktop может либо запустить собственный локальный сервер (по умолчанию), либо подключиться к настроенному вами URL-адресу сервера.

Если вы видите диалоговое окно **Ошибка подключения** (или приложение никогда не выходит за пределы заставки), проверьте URL-адрес пользовательского сервера.

#### Очистите URL-адрес сервера по умолчанию для рабочего стола.

На главном экране щелкните имя сервера (с точкой состояния), чтобы открыть окно выбора сервера. В разделе **Сервер по умолчанию** нажмите **Очистить**.

#### Удалите `server.port`/`server.hostname` из вашей конфигурации.

Если ваш `opencode.json(c)` содержит раздел `server`, временно удалите его и перезапустите настольное приложение.

#### Проверьте переменные среды

Если в вашей среде установлен `OPENCODE_PORT`, настольное приложение попытается использовать этот порт для локального сервера.

  * Отмените настройку `OPENCODE_PORT` (или выберите свободный порт) и перезапустите.



* * *

### Linux: проблемы с Wayland/X11

В Linux некоторые настройки Wayland могут вызывать пустые окна или ошибки компоновщика.

  * Если вы используете Wayland, а приложение не работает или вылетает, попробуйте запустить с помощью `OC_ALLOW_WAYLAND=1`.
  * Если это усугубляет ситуацию, удалите его и попробуйте вместо этого запустить сеанс X11.



* * *

### Windows: среда выполнения WebView2.

В Windows для opencode Desktop требуется Microsoft Edge **WebView2 Runtime**. Если приложение открывается в пустом окне или не запускается, установите/обновите WebView2 и повторите попытку.

* * *

### Windows: общие проблемы с производительностью

Если вы испытываете низкую производительность, проблемы с доступом к файлам или проблемы с terminal в Windows, попробуйте использовать [WSL (подсистема Windows для Linux)](/docs/windows-wsl). WSL предоставляет среду Linux, которая более эффективно работает с функциями opencode.

* * *

### Уведомления не отображаются

opencode Desktop отображает системные уведомления только в следующих случаях:

  * уведомления для opencode включены в настройках вашей ОС, и
  * окно приложения не в фокусе.



* * *

### Сбросить хранилище настольных приложений (последнее средство)

Если приложение не запускается и вы не можете очистить настройки из пользовательского интерфейса, сбросьте сохраненное состояние настольного приложения.

  1. Закройте рабочий стол opencode.
  2. Найдите и удалите эти файлы (они находятся в каталоге данных приложения opencode Desktop):


  * `opencode.settings.dat` (URL-адрес сервера по умолчанию для рабочего стола)
  * `opencode.global.dat` и `opencode.workspace.*.dat` (состояние пользовательского интерфейса, например, недавние серверы/проекты)



Чтобы быстро найти каталог:

  * **macOS** : Finder -> `Cmd+Shift+G` -> `~/Library/Application Support` (затем найдите имена файлов, указанные выше)
  * **Linux** : найдите в `~/.local/share` имена файлов, указанные выше.
  * **Windows** : нажмите `WIN+R` -> `%APPDATA%` (затем найдите имена файлов, указанные выше).



* * *

## Получение помощи

Если у вас возникли проблемы с opencode:

  1. **Сообщайте о проблемах на GitHub**

Лучший способ сообщить об ошибках или запросить новые функции — через наш репозиторий GitHub:

[**github.com/anomalyco/opencode/issues**](https://github.com/anomalyco/opencode/issues)

Прежде чем создавать новую проблему, выполните поиск по существующим проблемам, чтобы узнать, не сообщалось ли уже о вашей проблеме.

  2. **Присоединяйтесь к нашему Discord**

Для получения помощи в режиме реального времени и обсуждения в сообществе присоединяйтесь к нашему серверу Discord:

[**opencode.ai/discord**](https://opencode.ai/discord)




* * *

## Общие проблемы

Вот некоторые распространенные проблемы и способы их решения.

* * *

### opencode не запускается

  1. Проверьте журналы на наличие сообщений об ошибках
  2. Попробуйте запустить `--print-logs`, чтобы увидеть вывод в terminal.
  3. Убедитесь, что у вас установлена ​​последняя версия `opencode upgrade`.



* * *

### Проблемы аутентификации

  1. Попробуйте выполнить повторную аутентификацию с помощью команды `/connect` в TUI.
  2. Убедитесь, что ваши ключи API действительны
  3. Убедитесь, что ваша сеть разрешает подключения к API провайдера.



* * *

### Модель недоступна

  1. Убедитесь, что вы прошли аутентификацию у провайдера
  2. Проверьте правильность названия модели в вашей конфигурации.
  3. Для некоторых моделей может потребоваться специальный доступ или подписка.



Если вы столкнулись с `ProviderModelNotFoundError`, вы, скорее всего, ошибаетесь. ссылка на модель где-то. На модели следует ссылаться следующим образом: `<providerId>/<modelId>`.

Примеры:

  * `openai/gpt-4.1`
  * `openrouter/google/gemini-2.5-flash`
  * `opencode/kimi-k2`



Чтобы выяснить, к каким моделям у вас есть доступ, запустите `opencode models`.

* * *

### ProviderInitError

Если вы столкнулись с ошибкой ProviderInitError, скорее всего, у вас неверная или поврежденная конфигурация.

Чтобы решить эту проблему:

  1. Сначала убедитесь, что ваш провайдер настроен правильно, следуя [руководству провайдеров](/docs/providers)

  2. Если проблема не устранена, попробуйте очистить сохраненную конфигурацию:

Окно терминала
```
rm -rf ~/.local/share/opencode
```

В Windows нажмите `WIN+R` и удалите: `%USERPROFILE%\.local\share\opencode`.

  3. Повторно выполните аутентификацию у своего провайдера, используя команду `/connect` в TUI.




* * *

### AI_APICallError и проблемы с пакетом провайдера

Если вы столкнулись с ошибками вызова API, это может быть связано с устаревшими пакетами провайдера. opencode динамически устанавливает пакеты провайдеров (OpenAI, Anthropic, Google и т. д.) по мере необходимости и кэширует их локально.

Чтобы решить проблемы с пакетом поставщика:

  1. Очистите кеш пакетов провайдера:

Окно терминала
```
rm -rf ~/.cache/opencode
```

В Windows нажмите `WIN+R` и удалите: `%USERPROFILE%\.cache\opencode`.

  2. Перезапустите opencode, чтобы переустановить последние пакеты поставщиков.




Это заставит opencode загружать самые последние версии пакетов провайдеров, что часто решает проблемы совместимости с параметрами модели и изменениями API.

* * *

### Копирование/вставка не работает в Linux

Для работы функций копирования/вставки пользователям Linux необходимо установить одну из следующих утилит буфера обмена:

**Для систем X11:**

Окно терминала
```
apt install -y xclip
    # or
    apt install -y xsel
```

**Для систем Wayland:**

Окно терминала
```
apt install -y wl-clipboard
```

**Для headless-сред:**

Окно терминала
```
apt install -y xvfb
    # and run:
    Xvfb :99 -screen 0 1024x768x24 > /dev/null 2>&1 &
    export DISPLAY=:99.0
```

opencode определит, используете ли вы Wayland и предпочитаете `wl-clipboard`, в противном случае он попытается найти инструменты буфера обмена в порядке: `xclip` и `xsel`.

[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/troubleshooting.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-7"></a>
---
url: https://opencode.ai/docs/ru/windows-wsl
---

# Windows (WSL)

Запускайте opencode в Windows через WSL.

opencode можно запускать напрямую в Windows, но для лучшего опыта мы рекомендуем [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install). WSL дает Linux-среду, которая отлично работает с возможностями opencode.

Почему WSL?

WSL дает более высокую производительность файловой системы, полноценную поддержку терминала и совместимость с инструментами разработки, на которые опирается opencode.

* * *

## Настройка

  1. **Установите WSL**

Если вы еще не сделали этого, установите WSL по [официальному руководству Microsoft](https://learn.microsoft.com/en-us/windows/wsl/install).

  2. **Установите opencode в WSL**

После настройки WSL откройте терминал WSL и установите opencode одним из [способов установки](/docs/).

Окно терминала
```
curl -fsSL https://opencode.ai/install | bash
```

  3. **Запускайте opencode из WSL**

Перейдите в каталог проекта (к файлам Windows можно обращаться через `/mnt/c/`, `/mnt/d/` и т.д.) и запустите opencode.

Окно терминала
```
cd /mnt/c/Users/YourName/project
         opencode
```




* * *

## Десктопное приложение + сервер в WSL

Если вы предпочитаете opencode Desktop, но хотите запускать сервер в WSL:

  1. **Запустите сервер в WSL** с параметром `--hostname 0.0.0.0`, чтобы разрешить внешние подключения:

Окно терминала
```
opencode serve --hostname 0.0.0.0 --port 4096
```

  2. **Подключите десктопное приложение** к `http://localhost:4096`




Заметка

Если в вашей конфигурации `localhost` не работает, используйте IP-адрес WSL (выполните в WSL: `hostname -I`) и подключайтесь по `http://<wsl-ip>:4096`.

Осторожно

При использовании `--hostname 0.0.0.0` задайте `OPENCODE_SERVER_PASSWORD`, чтобы защитить сервер.

Окно терминала
```
OPENCODE_SERVER_PASSWORD=your-password opencode serve --hostname 0.0.0.0
```

* * *

## Веб-клиент + WSL

Для лучшего веб-опыта в Windows:

  1. **Запускайте`opencode web` в терминале WSL**, а не в PowerShell:

Окно терминала
```
opencode web --hostname 0.0.0.0
```

  2. **Открывайте в браузере Windows** адрес `http://localhost:<port>` (opencode выведет URL)




Запуск `opencode web` из WSL обеспечивает корректный доступ к файловой системе и интеграцию с терминалом, при этом интерфейс остается доступным из браузера Windows.

* * *

## Доступ к файлам Windows

WSL может получать доступ ко всем вашим файлам Windows через каталог `/mnt/`:

  * `C:` drive → `/mnt/c/`
  * `D:` drive → `/mnt/d/`
  * И так далее



Пример:

Окно терминала
```
cd /mnt/c/Users/YourName/Documents/project
    opencode
```

Совет

Для максимально плавной работы стоит клонировать или скопировать репозиторий в файловую систему WSL (например, в `~/code/`) и запускать opencode оттуда.

* * *

## Советы

  * Даже для проектов на дисках Windows запускайте opencode в WSL, чтобы получить более плавный доступ к файлам
  * Используйте opencode вместе с [расширением WSL для VS Code](https://code.visualstudio.com/docs/remote/wsl) для единого рабочего процесса
  * Конфигурация и сессии opencode хранятся в среде WSL по пути `~/.local/share/opencode/`



[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/windows-wsl.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-8"></a>
---
url: https://opencode.ai/docs/ru/tui/
---

# TUI

Использование TUI opencode.

opencode предоставляет интерактивный terminal интерфейс или TUI для работы над вашими проектами с помощью LLM.

Запуск opencode запускает TUI для текущего каталога.

Окно терминала
```
opencode
```

Или вы можете запустить его для определенного рабочего каталога.

Окно терминала
```
opencode /path/to/project
```

Как только вы окажетесь в TUI, вы можете запросить его с помощью сообщения.
```
Give me a quick summary of the codebase.
```

* * *

## Ссылки на файлы

Вы можете ссылаться на файлы в своих сообщениях, используя `@`. Это выполняет нечеткий поиск файлов в текущем рабочем каталоге.

Совет

Вы также можете использовать `@` для ссылки на файлы в своих сообщениях.
```
How is auth handled in @packages/functions/src/api/index.ts?
```

Содержимое файла добавляется в беседу автоматически.

* * *

## Bash-команды

Начните сообщение с `!`, чтобы запустить shell-команду.
```
!ls -la
```

Вывод команды добавляется в диалог как результат работы инструмента.

* * *

## Команды

При использовании opencode TUI вы можете ввести `/`, а затем имя команды, чтобы быстро выполнить действия. Например:
```
/help
```

Большинство команд также имеют привязку клавиш с использованием `ctrl+x` в качестве ведущей клавиши, где `ctrl+x` — это ведущая клавиша по умолчанию. [Подробнее ](/docs/keybinds).

Вот все доступные слэш-команды:

* * *

### connect

Добавьте провайдера в opencode. Позволяет выбирать из доступных поставщиков и добавлять их ключи API.
```
/connect
```

* * *

### compact

Сжать текущий сеанс. _Псевдоним_ : `/summarize`
```
/compact
```

**Привязка клавиш:** `ctrl+x c`

* * *

### details

Переключить детали выполнения инструмента.
```
/details
```

**Привязка клавиш:** `ctrl+x d`

* * *

### editor

Открыть внешний редактор для составления сообщений. Использует редактор, установленный в переменной среды `EDITOR`. Подробнее .
```
/editor
```

**Привязка клавиш:** `ctrl+x e`

* * *

### exit

Выйдите из opencode. _Псевдонимы_ : `/quit`, `/q`
```
/exit
```

**Привязка клавиш:** `ctrl+x q`

* * *

### export

Экспортируйте текущий разговор в Markdown и откройте его в редакторе по умолчанию. Использует редактор, установленный в переменной среды `EDITOR`. Подробнее .
```
/export
```

**Привязка клавиш:** `ctrl+x x`

* * *

### help

Показать диалоговое окно помощи.
```
/help
```

**Привязка клавиш:** `ctrl+x h`

* * *

### init

Создайте или обновите файл `AGENTS.md`. [Подробнее ](/docs/rules).
```
/init
```

**Привязка клавиш:** `ctrl+x i`

* * *

### models

Перечислите доступные модели.
```
/models
```

**Привязка клавиш:** `ctrl+x m`

* * *

### new

Начать новый сеанс. _Псевдоним_ : `/clear`
```
/new
```

**Привязка клавиш:** `ctrl+x n`

* * *

### redo

Повторить ранее отмененное сообщение. Доступно только после использования `/undo`.

Совет

Любые изменения файлов также будут восстановлены.

Внутри это использует Git для управления изменениями файлов. Итак, ваш проект ** должен быть репозиторием Git**.
```
/redo
```

**Привязка клавиш:** `ctrl+x r`

* * *

### sessions

Составляйте список и переключайтесь между сеансами. _Псевдонимы_ : `/resume`, `/continue`
```
/sessions
```

**Привязка клавиш:** `ctrl+x l`

* * *

### share

Поделиться текущим сеансом. [Подробнее](/docs/share).
```
/share
```

**Привязка клавиш:** `ctrl+x s`

* * *

### theme

Список доступных тем.
```
/theme
```

**Привязка клавиш:** `ctrl+x t`

* * *

### thinking

Переключить видимость блоков мышления/рассуждения в разговоре. Если этот параметр включен, вы можете увидеть процесс рассуждения модели для моделей, поддерживающих расширенное мышление.

Заметка

Эта команда только контролирует, будут ли **отображаться** блоки мышления, но не включает и не отключает возможности модели по рассуждению. Чтобы переключить фактические возможности рассуждения, используйте `ctrl+t` для циклического переключения вариантов модели.
```
/thinking
```

* * *

### undo

Отменить последнее сообщение в разговоре. Удаляет самое последнее сообщение пользователя, все последующие ответы и любые изменения файлов.

Совет

Любые внесенные изменения в файле также будут отменены.

Внутри это использует Git для управления изменениями файлов. Итак, ваш проект ** должен быть репозиторием Git**.
```
/undo
```

**Привязка клавиш:** `ctrl+x u`

* * *

### unshare

Отменить общий доступ к текущему сеансу. [Подробнее](/docs/share#un-sharing).
```
/unshare
```

* * *

## Настройка редактора

Команды `/editor` и `/export` используют редактор, указанный в переменной среды `EDITOR`.

  * Linux/macOS 
  * Windows (CMD) 
  * Windows (PowerShell) 



Окно терминала
```
# Example for nano or vim
    export EDITOR=nano
    export EDITOR=vim
    
    
    # For GUI editors, VS Code, Cursor, VSCodium, Windsurf, Zed, etc.
    # include --wait
    export EDITOR="code --wait"
```

Чтобы сделать его постоянным, добавьте это в свой профиль shell; `~/.bashrc`, `~/.zshrc` и т. д.

Окно терминала
```
set EDITOR=notepad
    # For GUI editors, VS Code, Cursor, VSCodium, Windsurf, Zed, etc.# include --waitset EDITOR=code --wait
```

Чтобы сделать его постоянным, используйте **Свойства системы** > **Среда Переменные**.

Окно терминала
```
$env:EDITOR = "notepad"
    # For GUI editors, VS Code, Cursor, VSCodium, Windsurf, Zed, etc.# include --wait$env:EDITOR = "code --wait"
```

Чтобы сделать его постоянным, добавьте его в свой профиль PowerShell.

Популярные варианты редактора включают в себя:

  * `code` — VS Code
  * `cursor` — Cursor
  * `windsurf` \- Windsurf
  * `nvim` \- Редактор Neovim
  * `vim` — редактор Vim
  * `nano` — Нано-редактор
  * `notepad` — Блокнот Windows
  * `subl` — Sublime Text



Заметка

Некоторые редакторы, такие как VS Code, необходимо запускать с флагом `--wait`.

Некоторым редакторам для работы в режиме блокировки необходимы CLI-аргументы. Флаг `--wait` блокирует процесс редактора до его закрытия.

* * *

## Настройка

Вы можете настроить поведение TUI через файл конфигурации opencode.

opencode.json
```
{
      "$schema": "https://opencode.ai/config.json",
      "tui": {
        "scroll_speed": 3,
        "scroll_acceleration": {
          "enabled": true
        }
      }
    }
```

### Параметры

  * `scroll_acceleration` — включите ускорение прокрутки в стиле macOS для плавной и естественной прокрутки. Если этот параметр включен, скорость прокрутки увеличивается при быстрой прокрутке и остается точной при более медленных движениях. **Этот параметр имеет приоритет над`scroll_speed` и переопределяет его, если он включен.**
  * `scroll_speed` — контролирует скорость прокрутки TUI при использовании команд прокрутки (минимум: `1`). По умолчанию `3`. **Примечание. Это игнорируется, если для`scroll_acceleration.enabled` установлено значение `true`.**



* * *

## Кастомизация

Вы можете настроить различные аспекты представления TUI, используя палитру команд (`ctrl+x h` или `/help`). Эти настройки сохраняются после перезапуска.

* * *

#### Отображение имени пользователя

Включите, будет ли ваше имя пользователя отображаться в сообщениях чата. Доступ к этому через:

  * Палитра команд: поиск «имя пользователя» или «скрыть имя пользователя».
  * Настройка сохраняется автоматически и будет запоминаться во время сеансов TUI.



[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/tui.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-9"></a>
---
url: https://opencode.ai/docs/ru/cli/
---

# CLI

Параметры и команда opencode CLI.

CLI opencode по умолчанию запускает [TUI](/docs/tui) при запуске без каких-либо аргументов.

Окно терминала
```
opencode
```

Но он также принимает команды, описанные на этой странице. Это позволяет вам программно взаимодействовать с opencode.

Окно терминала
```
opencode run "Explain how closures work in JavaScript"
```

* * *

### tui

Запустите TUI opencode.

Окно терминала
```
opencode [project]
```

#### Флаги

Флаг| Короткий| Описание  
---|---|---  
`--continue`| `-c`| Продолжить последний сеанс  
`--session`| `-s`| Идентификатор сеанса для продолжения  
`--fork`| | Разветвить сеанс при продолжении (используйте с `--continue` или `--session`)  
`--prompt`| | Промпт для использования  
`--model`| `-m`| Модель для использования в виде поставщика/модели.  
`--agent`| | Агент для использования  
`--port`| | Порт для прослушивания  
`--hostname`| | Имя хоста для прослушивания  
  
* * *

## Команды

CLI opencode также имеет следующие команды.

* * *

### agent

Управляйте агентами для opencode.

Окно терминала
```
opencode agent [command]
```

* * *

### attach

Подключите терминал к уже работающему внутреннему серверу opencode, запущенному с помощью команд `serve` или `web`.

Окно терминала
```
opencode attach [url]
```

Это позволяет использовать TUI с удаленным сервером opencode. Например:

Окно терминала
```
# Start the backend server for web/mobile access
    opencode web --port 4096 --hostname 0.0.0.0
    
    
    # In another terminal, attach the TUI to the running backend
    opencode attach http://10.20.30.40:4096
```

#### Флаги

Флаг| Короткий| Описание  
---|---|---  
`--dir`| | Рабочий каталог для запуска TUI  
`--session`| `-s`| Идентификатор сеанса для продолжения  
  
* * *

#### create

Создайте нового агента с пользовательской конфигурацией.

Окно терминала
```
opencode agent create
```

Эта команда поможет вам создать новый агент с настраиваемой системной подсказкой и настройкой инструмента.

* * *

#### list

Перечислите всех доступных агентов.

Окно терминала
```
opencode agent list
```

* * *

### auth

Команда для управления учетными данными и входом в систему для провайдеров.

Окно терминала
```
opencode auth [command]
```

* * *

#### login

opencode использует список провайдеров с [Models.dev](https://models.dev), поэтому вы можете использовать `opencode auth login` для настройки ключей API для любого поставщика, которого вы хотите использовать. Это хранится в `~/.local/share/opencode/auth.json`.

Окно терминала
```
opencode auth login
```

Когда opencode запускается, он загружает поставщиков из файла учетных данных. И если в ваших средах определены какие-либо ключи или файл `.env` в вашем проекте.

* * *

#### list

Перечисляет всех проверенных поставщиков, которые хранятся в файле учетных данных.

Окно терминала
```
opencode auth list
```

Или короткая версия.

Окно терминала
```
opencode auth ls
```

* * *

#### logout

Выключает вас из провайдера, удаляя его из файла учетных данных.

Окно терминала
```
opencode auth logout
```

* * *

### github

Управляйте агентом GitHub для автоматизации репозитория.

Окно терминала
```
opencode github [command]
```

* * *

#### install

Установите агент GitHub в свой репозиторий.

Окно терминала
```
opencode github install
```

Это настроит необходимый рабочий процесс GitHub Actions и проведет вас через процесс настройки. [Подробнее](/docs/github).

* * *

#### run

Запустите агент GitHub. Обычно это используется в действиях GitHub.

Окно терминала
```
opencode github run
```

##### Флаги

Флаг| Описание  
---|---  
`--event`| Имитирующее событие GitHub для запуска агента  
`--token`| Токен личного доступа GitHub  
  
* * *

### mcp

Управляйте серверами протокола контекста модели.

Окно терминала
```
opencode mcp [command]
```

* * *

#### add

Добавьте сервер MCP в свою конфигурацию.

Окно терминала
```
opencode mcp add
```

Эта команда поможет вам добавить локальный или удаленный сервер MCP.

* * *

#### list

Перечислите все настроенные серверы MCP и состояние их подключения.

Окно терминала
```
opencode mcp list
```

Или используйте короткую версию.

Окно терминала
```
opencode mcp ls
```

* * *

#### auth

Аутентификация с помощью сервера MCP с поддержкой OAuth.

Окно терминала
```
opencode mcp auth [name]
```

Если вы не укажете имя сервера, вам будет предложено выбрать один из доступных серверов с поддержкой OAuth.

Вы также можете перечислить серверы с поддержкой OAuth и их статус аутентификации.

Окно терминала
```
opencode mcp auth list
```

Или используйте короткую версию.

Окно терминала
```
opencode mcp auth ls
```

* * *

#### logout

Удалите учетные данные OAuth для сервера MCP.

Окно терминала
```
opencode mcp logout [name]
```

* * *

#### debug

Отладка проблем с подключением OAuth для сервера MCP.

Окно терминала
```
opencode mcp debug <name>
```

* * *

### models

Перечислите все доступные модели от настроенных поставщиков.

Окно терминала
```
opencode models [provider]
```

Эта команда отображает все модели, доступные у настроенных вами поставщиков, в формате `provider/model`.

Это полезно для определения точного названия модели, которое будет использоваться в [вашем config](/docs/config/).

При желании вы можете передать идентификатор поставщика, чтобы фильтровать модели по этому поставщику.

Окно терминала
```
opencode models anthropic
```

#### Флаги

Флаг| Описание  
---|---  
`--refresh`| Обновите кеш моделей на сайте models.dev.  
`--verbose`| Используйте более подробный вывод модели (включая метаданные, такие как затраты).  
  
Используйте флаг `--refresh` для обновления списка кэшированных моделей. Это полезно, когда к поставщику добавлены новые модели и вы хотите увидеть их в opencode.

Окно терминала
```
opencode models --refresh
```

* * *

### run

Запустите opencode в неинтерактивном режиме, передав приглашение напрямую.

Окно терминала
```
opencode run [message..]
```

Это полезно для создания сценариев, автоматизации или когда вам нужен быстрый ответ без запуска полного TUI. Например.

Окно терминала
```
opencode run Explain the use of context in Go
```

Вы также можете подключиться к работающему экземпляру `opencode serve`, чтобы избежать холодной загрузки сервера MCP при каждом запуске:

Окно терминала
```
# Start a headless server in one terminal
    opencode serve
    
    
    # In another terminal, run commands that attach to it
    opencode run --attach http://localhost:4096 "Explain async/await in JavaScript"
```

#### Флаги

Флаг| Короткий| Описание  
---|---|---  
`--command`| | Команда для запуска, используйте сообщение для аргументов  
`--continue`| `-c`| Продолжить последний сеанс  
`--session`| `-s`| Идентификатор сеанса для продолжения  
`--fork`| | Разветвить сеанс при продолжении (используйте с `--continue` или `--session`)  
`--share`| | Поделиться сеансом  
`--model`| `-m`| Модель для использования в виде поставщика/модели.  
`--agent`| | Агент для использования  
`--file`| `-f`| Файл(ы) для прикрепления к сообщению  
`--format`| | Формат: по умолчанию (отформатированный) или json (необработанные события JSON).  
`--title`| | Название сеанса (использует усеченное приглашение, если значение не указано)  
`--attach`| | Подключитесь к работающему серверу opencode (например, <http://localhost:4096>)  
`--port`| | Порт локального сервера (по умолчанию случайный порт)  
  
* * *

### serve

Запустите автономный сервер opencode для доступа к API. Полный HTTP-интерфейс можно найти в [server docs](/docs/server).

Окно терминала
```
opencode serve
```

При этом запускается HTTP-сервер, который обеспечивает доступ API к функциям opencode без интерфейса TUI. Установите `OPENCODE_SERVER_PASSWORD`, чтобы включить базовую аутентификацию HTTP (имя пользователя по умолчанию — `opencode`).

#### Флаги

Флаг| Описание  
---|---  
`--port`| Порт для прослушивания  
`--hostname`| Имя хоста для прослушивания  
`--mdns`| Включить обнаружение mDNS  
`--cors`| Дополнительные источники браузера, позволяющие разрешить CORS  
  
* * *

### session

Управляйте сессиями opencode.

Окно терминала
```
opencode session [command]
```

* * *

#### list

Перечислите все сеансы opencode.

Окно терминала
```
opencode session list
```

##### Флаги

Флаг| Короткий| Описание  
---|---|---  
`--max-count`| `-n`| Ограничить N последних сеансов.  
`--format`| | Формат вывода: таблица или json (таблица)  
  
* * *

### stats

Покажите статистику использования токенов и затрат для ваших сеансов opencode.

Окно терминала
```
opencode stats
```

#### Флаги

Флаг| Описание  
---|---  
`--days`| Показать статистику за последние N дней (все время)  
`--tools`| Количество инструментов для отображения (все)  
`--models`| Показать разбивку по использованию модели (по умолчанию скрыто). Передайте номер, чтобы показать верхнюю N  
`--project`| Фильтровать по проекту (все проекты, пустая строка: текущий проект)  
  
* * *

### export

Экспортируйте данные сеанса в формате JSON.

Окно терминала
```
opencode export [sessionID]
```

Если вы не укажете идентификатор сеанса, вам будет предложено выбрать один из доступных сеансов.

* * *

### import

Импортируйте данные сеанса из файла JSON или URL-адреса общего ресурса opencode.

Окно терминала
```
opencode import <file>
```

Вы можете импортировать из локального файла или URL-адреса общего ресурса opencode.

Окно терминала
```
opencode import session.json
    opencode import https://opncd.ai/s/abc123
```

* * *

### web

Запустите автономный сервер opencode с веб-интерфейсом.

Окно терминала
```
opencode web
```

При этом запускается HTTP-сервер и открывается веб-браузер для доступа к opencode через веб-интерфейс. Установите `OPENCODE_SERVER_PASSWORD`, чтобы включить базовую аутентификацию HTTP (имя пользователя по умолчанию — `opencode`).

#### Флаги

Флаг| Описание  
---|---  
`--port`| Порт для прослушивания  
`--hostname`| Имя хоста для прослушивания  
`--mdns`| Включить обнаружение mDNS  
`--cors`| Дополнительные источники браузера, позволяющие разрешить CORS  
  
* * *

### acp

Запустите сервер ACP (агент-клиентский протокол).

Окно терминала
```
opencode acp
```

Эта команда запускает сервер ACP, который обменивается данными через stdin/stdout с использованием nd-JSON.

#### Флаги

Флаг| Описание  
---|---  
`--cwd`| Рабочий каталог  
`--port`| Порт для прослушивания  
`--hostname`| Имя хоста для прослушивания  
  
* * *

### uninstall

Удалите opencode и удалите все связанные файлы.

Окно терминала
```
opencode uninstall
```

#### Флаги

Флаг| Короткий| Описание  
---|---|---  
`--keep-config`| `-c`| Сохраняйте файлы конфигурации  
`--keep-data`| `-d`| Храните данные сеанса и снимки  
`--dry-run`| | Покажите, что было бы удалено без удаления  
`--force`| `-f`| Пропустить запросы подтверждения  
  
* * *

### upgrade

Обновляет opencode до последней версии или определенной версии.

Окно терминала
```
opencode upgrade [target]
```

Чтобы обновиться до последней версии.

Окно терминала
```
opencode upgrade
```

Для обновления до определенной версии.

Окно терминала
```
opencode upgrade v0.1.48
```

#### Флаги

Флаг| Короткий| Описание  
---|---|---  
`--method`| `-m`| Используемый метод установки: local, npm, pnpm, bun, brew  
  
* * *

## Глобальные флаги

CLI opencode принимает следующие глобальные флаги.

Флаг| Короткий| Описание  
---|---|---  
`--help`| `-h`| Отобразить справку  
`--version`| `-v`| Распечатать номер версии  
`--print-logs`| | Печать журналов в stderr  
`--log-level`| | Уровень журнала (DEBUG, INFO, WARN, ERROR)  
  
* * *

## Переменные среды

opencode можно настроить с помощью переменных среды.

Переменная| Тип| Описание  
---|---|---  
`OPENCODE_AUTO_SHARE`| логическое значение| Автоматически делиться сеансами  
`OPENCODE_GIT_BASH_PATH`| строка| Путь к исполняемому файлу Git Bash в Windows  
`OPENCODE_CONFIG`| строка| Путь к файлу конфигурации  
`OPENCODE_CONFIG_DIR`| строка| Путь к каталогу конфигурации  
`OPENCODE_CONFIG_CONTENT`| строка| Встроенное содержимое конфигурации json  
`OPENCODE_DISABLE_AUTOUPDATE`| логическое значение| Отключить автоматическую проверку обновлений  
`OPENCODE_DISABLE_PRUNE`| логическое значение| Отключить удаление старых данных  
`OPENCODE_DISABLE_TERMINAL_TITLE`| логическое значение| Отключить автоматическое обновление заголовка терминала  
`OPENCODE_PERMISSION`| строка| Встроенная конфигурация разрешений json  
`OPENCODE_DISABLE_DEFAULT_PLUGINS`| логическое значение| Отключить плагины по умолчанию  
`OPENCODE_DISABLE_LSP_DOWNLOAD`| логическое значение| Отключить автоматическую загрузку LSP-сервера  
`OPENCODE_ENABLE_EXPERIMENTAL_MODELS`| логическое значение| Включить экспериментальные модели  
`OPENCODE_DISABLE_AUTOCOMPACT`| логическое значение| Отключить автоматическое сжатие контекста  
`OPENCODE_DISABLE_CLAUDE_CODE`| логическое значение| Отключить чтение из `.claude` (подсказка + навыки)  
`OPENCODE_DISABLE_CLAUDE_CODE_PROMPT`| логическое значение| Отключить чтение `~/.claude/CLAUDE.md`  
`OPENCODE_DISABLE_CLAUDE_CODE_SKILLS`| логическое значение| Отключить загрузку `.claude/skills`  
`OPENCODE_DISABLE_MODELS_FETCH`| логическое значение| Отключить получение моделей из удаленных источников  
`OPENCODE_FAKE_VCS`| строка| Поддельный поставщик VCS для целей тестирования  
`OPENCODE_DISABLE_FILETIME_CHECK`| логическое значение| Отключить проверку времени файла для оптимизации  
`OPENCODE_CLIENT`| строка| Идентификатор клиента (по умолчанию `cli`)  
`OPENCODE_ENABLE_EXA`| логическое значение| Включить инструменты веб-поиска Exa  
`OPENCODE_SERVER_PASSWORD`| строка| Включить базовую аутентификацию для `serve`/`web`  
`OPENCODE_SERVER_USERNAME`| строка| Переопределить имя пользователя базовой аутентификации (по умолчанию `opencode`)  
`OPENCODE_MODELS_URL`| строка| Пользовательский URL-адрес для получения конфигурации модели  
  
* * *

### Экспериментальные функции

Эти переменные среды позволяют использовать экспериментальные функции, которые могут быть изменены или удалены.

Переменная| Тип| Описание  
---|---|---  
`OPENCODE_EXPERIMENTAL`| логическое значение| Включить все экспериментальные функции  
`OPENCODE_EXPERIMENTAL_ICON_DISCOVERY`| логическое значение| Включить обнаружение значков  
`OPENCODE_EXPERIMENTAL_DISABLE_COPY_ON_SELECT`| логическое значение| Отключить копирование при выборе в TUI  
`OPENCODE_EXPERIMENTAL_BASH_DEFAULT_TIMEOUT_MS`| число| Таймаут по умолчанию для команд bash в мс  
`OPENCODE_EXPERIMENTAL_OUTPUT_TOKEN_MAX`| число| Максимальное количество токенов вывода для ответов LLM  
`OPENCODE_EXPERIMENTAL_FILEWATCHER`| логическое значение| Включить просмотр файлов для всего каталога  
`OPENCODE_EXPERIMENTAL_OXFMT`| логическое значение| Включить форматтер oxfmt  
`OPENCODE_EXPERIMENTAL_LSP_TOOL`| логическое значение| Включить экспериментальный инструмент LSP  
`OPENCODE_EXPERIMENTAL_DISABLE_FILEWATCHER`| логическое значение| Отключить просмотрщик файлов  
`OPENCODE_EXPERIMENTAL_EXA`| логическое значение| Включить экспериментальные функции Exa  
`OPENCODE_EXPERIMENTAL_LSP_TY`| логическое значение| Включить экспериментальную проверку типа LSP  
`OPENCODE_EXPERIMENTAL_MARKDOWN`| логическое значение| Включить экспериментальные функции Markdown  
`OPENCODE_EXPERIMENTAL_PLAN_MODE`| логическое значение| Включить режим плана  
  
[Редактировать страницу](https://github.com/anomalyco/opencode/edit/dev/packages/web/src/content/docs/ru/cli.mdx)[Found a bug? Open an issue](https://github.com/anomalyco/opencode/issues/new)[Join our Discord community](https://opencode.ai/discord) Выберите язык EnglishالعربيةBosanskiDanskDeutschEspañolFrançaisItaliano日本語한국어Norsk BokmålPolskiPortuguês (Brasil)РусскийไทยTürkçe简体中文繁體中文

© [Anomaly](https://anoma.ly)

Последнее обновление: 21 февр. 2026 г.


---

<a id="page-10"></a>
---
url: https://opencode.ai/docs/ru/web/
---

# Интернет

Использование opencode в вашем браузере.

opencode может работать как веб-приложение в вашем браузере, обеспечивая такой же мощный опыт кодирования AI без необходимости использования терминала.

![opencode Web — новый сеанс](https://opencode.ai/docs/_astro/web-homepage-new-session.BB1mEdgo_Z1AT1v3.webp)

## Начало работы

Запустите веб-интерфейс, выполнив:

Окно терминала
```
opencode web
```

Это запустит локальный сервер `127.0.0.1` со случайным доступным портом и автоматически откроет opencode в браузере по умолчанию.

Осторожно

Если `OPENCODE_SERVER_PASSWORD` не установлен, сервер будет незащищен. Это подходит для локального использования, но его следует настроить для доступа к сети.

Пользователи Windows

Для получения наилучших результатов запустите `opencode web` из [WSL](/docs/windows-wsl), а не из PowerShell. Это обеспечивает правильный доступ к файловой системе и интеграцию терминала.

* * *

## Конфигурация

Вы можете настроить веб-сервер с помощью CLI-флагов или в файле [config file](/docs/config).

### Порт

По умолчанию opencode выбирает доступный порт. Вы можете указать порт:

Окно терминала
```
opencode web --port 4096
```

### Имя хоста

По умолчанию сервер привязывается к `127.0.0.1` (только локальный хост). Чтобы сделать opencode доступным в вашей сети:

Окно терминала
```
opencode web --hostname 0.0.0.0
```

При использовании `0.0.0.0` opencode будет отображать как локальные, так и сетевые адреса:
```
Local access:       http://localhost:4096
      Network access:     http://192.168.1.100:4096
```

### Обнаружение mDNS

Включите mDNS, чтобы ваш сервер был доступен для обнаружения в локальной сети:

Окно терминала
```
opencode web --mdns
```

Это автоматически устанавливает имя хоста `0.0.0.0` и объявляет сервер как `opencode.local`.

Вы можете настроить доменное имя mDNS для запуска нескольких экземпляров в одной сети:

Окно терминала
```
opencode web --mdns --mdns-domain myproject.local
```

### CORS

Чтобы разрешить дополнительные домены для CORS (полезно для пользовательских интерфейсов):

Окно терминала
```
opencode web --cors https://example.com
```

### Аутентификация

Чтобы защитить доступ, установите пароль, используя переменную среды `OPENCODE_SERVER_PASSWORD`:

Окно терминала
```
OPENCODE_SERVER_PASSWORD=secret opencode web
```

Имя пользователя по умолчанию — `opencode`, но его можно изменить с помощью `OPENCODE_SERVER_USERNAME`.

* * *

## Использование веб-интерфейса

После запуска веб-интерфейс предоставляет доступ к вашим сеансам opencode.

### Сессии

Просматривайте свои сеансы и управляйте ими с главной страницы. Вы можете видеть активные сеансы и начинать новые.

![opencode Web — активный сеанс](https://opencode.ai/docs/_astro/web-homepage-active-session.BbK4Ph6e_Z1O7nO1.webp)

### Статус сервера

Нажмите «Просмотреть серверы», чтобы просмотреть подключенные серверы и их статус.

![opencode Web — см. Серверы](https://opencode.ai/docs/_astro/web-homepage-see-servers.BpCOef2l_ZB0rJd.webp)

* * *

## Подключение терминала

Вы можете подключить TUI терминала к работающему веб-серверу:

Окно терминала
```
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

