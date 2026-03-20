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
