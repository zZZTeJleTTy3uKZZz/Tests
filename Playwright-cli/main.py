import os
import csv
import sys
import time
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright


def main():
    load_dotenv()
    phone = os.getenv("PHONE")
    password = os.getenv("PASSWORD")

    if not phone or not password:
        print("Не задан логин или пароль в .env файле")
        return

    # Получаем URL из аргументов, либо используем по умолчанию
    url = (
        sys.argv[1]
        if len(sys.argv) > 1
        else "https://p.newpeople.pro/app/event-group/2004"
    )

    # User agent от обычного Chrome (Windows 10)
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context_options = {
            "user_agent": user_agent,
            "viewport": {"width": 1280, "height": 720},
        }

        # Загрузка сохраненной сессии, если она есть
        if os.path.exists("state.json"):
            context_options["storage_state"] = "state.json"

        context = browser.new_context(**context_options)
        page = context.new_page()

        print(f"Открываем {url}")
        page.goto(url)

        # Ждем загрузки - если редирект на /login, то логинимся
        page.wait_for_load_state("networkidle")
        time.sleep(2)  # небольшая пауза для SPA

        if "login" in page.url:
            print("Нужна авторизация, вводим данные...")
            # Номер телефона
            phone_input = page.get_by_role("textbox", name="Введите номер телефона*")
            phone_input.wait_for(timeout=10000)
            phone_input.click()
            # Убираем все символы кроме цифр
            clean_phone = "".join(filter(str.isdigit, phone))
            # Если номер начинается с 7, убираем первую семерку, т.к. маска +7 уже есть
            if clean_phone.startswith("7") and len(clean_phone) == 11:
                clean_phone = clean_phone[1:]

            # Вводим по символу для надежности
            page.keyboard.type(clean_phone, delay=50)

            # Пароль
            password_input = page.get_by_role("textbox", name="Введите пароль")
            password_input.fill(password)

            # Войти
            page.get_by_text("Войти").click()
            print("Ожидание завершения авторизации...")

            # Ждем перехода обратно на нужную страницу или на главную
            page.wait_for_url("**/app/**", timeout=20000)
            print("Авторизация успешна.")

            # Сохраняем сессию
            context.storage_state(path="state.json")
            print("Сессия сохранена в state.json")

            # Если после логина оказались не на нужной странице, переходим
            if url not in page.url:
                print("Переход на страницу мероприятия...")
                page.goto(url)
                page.wait_for_load_state("networkidle")

        print("Ожидаем вкладку 'Все касания'...")
        tab_btn = page.get_by_role("button", name="Все касания")
        tab_btn.wait_for(state="visible", timeout=30000)
        tab_btn.click()
        print("Вкладка открыта, ожидаем загрузки таблицы...")

        time.sleep(3)  # ждем рендера таблицы

        all_rows_data = []

        page_num = 1

        # Получаем структуру таблицы
        table = page.locator("table")
        table.wait_for(state="visible", timeout=10000)

        # ДИНАМИЧЕСКОЕ ИЗВЛЕЧЕНИЕ ЗАГОЛОВКОВ
        # Собираем все <th> элементы таблицы
        header_elements = table.locator("th").all()
        headers = [th.inner_text().strip() for th in header_elements]
        headers = [h for h in headers if h]  # Убираем пустые

        print("ДИНАМИЧЕСКИ Найдены заголовки:", headers)

        while True:
            print(f"Сбор данных со страницы {page_num}...")
            time.sleep(1)  # даем таблице обновиться после клика

            rows = table.locator("tbody tr, tr").all()
            page_rows = 0

            for row in rows:
                cells = row.locator("td").all()
                if not cells:
                    continue  # это строка с заголовками th

                row_data = [cell.inner_text().strip() for cell in cells]
                if any(row_data):
                    all_rows_data.append(row_data)
                    page_rows += 1

            print(
                f"На странице {page_num} собрано {page_rows} записей. Итого: {len(all_rows_data)}"
            )

            # Пробуем найти кнопку следующей страницы по тексту (цифре)
            next_page_str = str(page_num + 1)
            next_btn = page.get_by_role("button", name=next_page_str, exact=True)

            if next_btn.is_visible() and not next_btn.is_disabled():
                print(f"Переход на страницу {page_num + 1}...")
                next_btn.click()
                page_num += 1
                time.sleep(2)
            else:
                # Пробуем поискать общую кнопку "Вперед"
                forward_btn = page.locator("button:has-text('>')").first
                if forward_btn.is_visible() and not forward_btn.is_disabled():
                    print(f"Клик по кнопке 'Вперед'...")
                    forward_btn.click()
                    page_num += 1
                    time.sleep(2)
                else:
                    print(
                        "Больше страниц не найдено или кнопка не активна. Завершаем сбор."
                    )
                    break

        # Сохранение в CSV
        # Сгенерируем имя файла из ID мероприятия, чтобы не перезаписывать прошлые
        event_id = url.rstrip("/").split("/")[-1]
        csv_filename = f"contacts_{event_id}.csv"
        print(f"Начинаем запись данных в {csv_filename}...")

        with open(csv_filename, mode="w", encoding="utf-8-sig", newline="") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(headers)
            for row in all_rows_data:
                # обрезаем или дополняем до длины заголовков, чтобы таблица была ровной
                padded_row = row + [""] * (len(headers) - len(row))
                writer.writerow(padded_row[: len(headers)])

        print(
            f"Успешно выгружено {len(all_rows_data)} контактов в файл {csv_filename}!"
        )

        # Держим браузер открытым пару секунд
        time.sleep(2)
        browser.close()


if __name__ == "__main__":
    main()
