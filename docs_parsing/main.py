import argparse
import asyncio
import sys
import json
import os
import importlib
from playwright.async_api import async_playwright

PARSERS = {
    "opencode": "opencode.parser",
    "antigravity": "antigravity.parser",
    "payload": "payload.parser",
    "nextjs": "nextjs.parser",
    "pencil": "pencil.parser",
}


def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    # Дефолтный конфиг, если файла нет
    return {
        "max_concurrent_connections": 5, # 0 = без ограничений
        "browser_viewport": {"width": 1280, "height": 720},
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "headless": True
    }


def run_parser(parser_name, config):
    print(f"============================================")
    print(f" Запуск парсера: {parser_name}")
    print(f"============================================")

    module_path = PARSERS.get(parser_name)
    if not module_path:
        print(f"Ошибка: парсер '{parser_name}' не найден.")
        return

    try:
        parser_module = importlib.import_module(module_path)
    except Exception as e:
        print(f"Ошибка при импорте модуля '{module_path}': {e}")
        return

    # Запускаем скрипт модуля, прокидывая в него глобальный конфиг
    if hasattr(parser_module, "parse_with_config"):
        print(f"[{parser_name}] Инициализация парсинга с глобальным конфигом...")
        asyncio.run(parser_module.parse_with_config(config))
    elif hasattr(parser_module, "main"):
        print(f"[{parser_name}] Внимание: Модуль использует старый метод main() без конфига. Рекомендуется обновить модуль.")
        asyncio.run(parser_module.main())
    else:
        print(f"[{parser_name}] Ошибка: Модуль не имеет функции parse_with_config() или main()!")

    print(f"============================================")
    print(f" Парсер '{parser_name}' завершил работу.")
    print(f"============================================")


def main():
    parser = argparse.ArgumentParser(
        description="CLI для модульного парсинга сайтов документаций."
    )
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")

    list_parser = subparsers.add_parser(
        "list", help="Показать список доступных парсеров"
    )

    run_parser_cmd = subparsers.add_parser("run", help="Запустить конкретный парсер")
    run_parser_cmd.add_argument(
        "target", help='Имя парсера (например, opencode) или "all"'
    )

    args = parser.parse_args()
    config = load_config()

    if args.command == "list":
        print("Доступные модули для парсинга:")
        for name in PARSERS:
            print(f"  - {name}")
    elif args.command == "run":
        if args.target == "all":
            print("Запуск всех парсеров по очереди...")
            for target in PARSERS:
                run_parser(target, config)
        elif args.target in PARSERS:
            run_parser(args.target, config)
        else:
            print(
                f"Неизвестный парсер: '{args.target}'. Введите 'uv run python main.py list' для просмотра доступных."
            )
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
