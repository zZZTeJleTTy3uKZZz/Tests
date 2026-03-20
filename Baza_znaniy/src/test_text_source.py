import asyncio
import os
import sys
import httpx


async def main():
    print("--- Запускаем добавление текста в NotebookLM ---")
    notebook_url = (
        "https://notebooklm.google.com/notebook/04594cba-567d-4ad6-8852-c12dbdfcff5a"
    )

    os.environ["NOTEBOOKLM_API_URL"] = "http://localhost:3030"

    with open("../../docs_parsing/small_test.md", "r", encoding="utf-8") as f:
        text_content = f.read()

    print(f"\n--- Отправляем текст в блокнот ---")
    async with httpx.AsyncClient(timeout=120) as client:
        resp = await client.post(
            f"http://localhost:3030/content/sources",
            json={
                "source_type": "text",
                "text": text_content,
                "notebook_url": notebook_url,
                "title": "Small Test Text",
            },
        )
        print(resp.json())


if __name__ == "__main__":
    asyncio.run(main())
