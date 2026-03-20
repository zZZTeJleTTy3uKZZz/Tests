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
