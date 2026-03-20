with open('main.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re

old_imports = """import argparse
import asyncio
import sys
import importlib
from playwright.async_api import async_playwright

PARSERS = {"""

new_imports = """import argparse
import asyncio
import sys
import json
import os
import importlib
from playwright.async_api import async_playwright

PARSERS = {"""

text = text.replace(old_imports, new_imports)

old_run = """def run_parser(parser_name):
    print(f"============================================")"""

new_run = """def load_config():
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
    print(f"============================================")"""

text = text.replace(old_run, new_run)


old_exec = """    # Запускаем оригинальный скрипт модуля (он сам поднимет playwright_context)
    if hasattr(parser_module, "main"):
        print(f"[{parser_name}] Инициализация парсинга...")
        asyncio.run(parser_module.main())
    else:
        print(f"[{parser_name}] Ошибка: Модуль не имеет функции main()!")"""

new_exec = """    # Запускаем скрипт модуля, прокидывая в него глобальный конфиг
    if hasattr(parser_module, "parse_with_config"):
        print(f"[{parser_name}] Инициализация парсинга с глобальным конфигом...")
        asyncio.run(parser_module.parse_with_config(config))
    elif hasattr(parser_module, "main"):
        print(f"[{parser_name}] Внимание: Модуль использует старый метод main() без конфига. Рекомендуется обновить модуль.")
        asyncio.run(parser_module.main())
    else:
        print(f"[{parser_name}] Ошибка: Модуль не имеет функции parse_with_config() или main()!")"""

text = text.replace(old_exec, new_exec)

old_args = """    args = parser.parse_args()

    if args.command == "list":"""

new_args = """    args = parser.parse_args()
    config = load_config()

    if args.command == "list":"""

text = text.replace(old_args, new_args)

old_calls = """        if args.target == "all":
            print("Запуск всех парсеров по очереди...")
            for target in PARSERS:
                run_parser(target)
        elif args.target in PARSERS:
            run_parser(args.target)"""

new_calls = """        if args.target == "all":
            print("Запуск всех парсеров по очереди...")
            for target in PARSERS:
                run_parser(target, config)
        elif args.target in PARSERS:
            run_parser(args.target, config)"""

text = text.replace(old_calls, new_calls)

with open('main.py', 'w', encoding='utf-8') as f:
    f.write(text)

