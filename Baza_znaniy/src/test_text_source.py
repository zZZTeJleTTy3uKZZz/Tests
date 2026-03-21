import asyncio

from app.services.notebooklm_adapter import get_notebooklm_adapter


async def main():
    print("--- Запускаем добавление текста в NotebookLM ---")
    adapter = get_notebooklm_adapter()

    with open("../../docs_parsing/small_test.md", "r", encoding="utf-8") as f:
        text_content = f.read()

    notebook = await adapter.get_or_create_notebook("Small_Test_Text")
    source = await adapter.add_text_source(
        notebook_id=notebook["id"],
        title="Small Test Text",
        content=text_content,
    )
    print(source)

    result = await adapter.ask_notebook(
        notebook_id=notebook["id"],
        question="Кратко ответь, что находится в этом блокноте?",
    )
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
