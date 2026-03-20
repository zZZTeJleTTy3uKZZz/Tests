import os
import io
import re

LIMIT_BYTES = 200 * 1024  # 200 KB - режем мельче, чтобы NotebookLM глотал мгновенно
LIMIT_WORDS = 25_000  # около 25k слов на часть


def count_words(text: str) -> int:
    # Примерный подсчет слов (разбивка по пробельным символам)
    return len(text.split())


def split_markdown_file(file_path: str) -> list[str]:
    """
    Разбивает Markdown-файл на части, если он превышает лимиты NotebookLM
    (190 МБ или 490 000 слов).

    Возвращает список путей к созданным частям (или оригинальный путь, если разбивка не требуется).
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл не найден: {file_path}")

    # Убираем проверку на < 1MB, чтобы принудительно резать файлы больше 200КБ
    # file_size = os.path.getsize(file_path)
    # if file_size < 1024 * 1024:
    #     return [file_path]

    base_dir = os.path.dirname(file_path)
    base_name, ext = os.path.splitext(os.path.basename(file_path))

    parts = []

    with open(file_path, "r", encoding="utf-8") as f:
        current_part_num = 1
        current_words = 0
        current_bytes = 0
        current_lines = []

        for line in f:
            line_bytes = len(line.encode("utf-8"))
            line_words = count_words(line)

            # Проверяем, не превышен ли лимит (стараемся резать на заголовках, если возможно, но жестко если лимит близко)
            is_header = line.startswith("# ") or line.startswith("## ")

            exceeds_size = (current_bytes + line_bytes) > LIMIT_BYTES
            exceeds_words = (current_words + line_words) > LIMIT_WORDS

            # Если превышаем или если мы близки к лимиту и встретили новый заголовок
            close_to_limit = (current_words > LIMIT_WORDS * 0.9) or (
                current_bytes > LIMIT_BYTES * 0.9
            )

            if exceeds_size or exceeds_words or (close_to_limit and is_header):
                if not current_lines:
                    # Если одна строка превышает лимит (маловероятно), просто добавляем ее
                    current_lines.append(line)
                    continue

                # Сохраняем текущую часть
                part_path = os.path.join(
                    base_dir, f"{base_name}_part{current_part_num}{ext}"
                )
                with open(part_path, "w", encoding="utf-8") as p:
                    p.writelines(current_lines)
                parts.append(part_path)

                # Сбрасываем счетчики
                current_part_num += 1
                current_words = 0
                current_bytes = 0
                current_lines = []

            current_lines.append(line)
            current_bytes += line_bytes
            current_words += line_words

        # Сохраняем последний кусок
        if current_lines:
            # Если это первая и единственная часть, просто возвращаем оригинал
            if current_part_num == 1:
                return [file_path]

            part_path = os.path.join(
                base_dir, f"{base_name}_part{current_part_num}{ext}"
            )
            with open(part_path, "w", encoding="utf-8") as p:
                p.writelines(current_lines)
            parts.append(part_path)

    return parts
