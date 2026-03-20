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
