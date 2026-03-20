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
