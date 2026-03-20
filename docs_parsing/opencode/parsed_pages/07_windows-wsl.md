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
