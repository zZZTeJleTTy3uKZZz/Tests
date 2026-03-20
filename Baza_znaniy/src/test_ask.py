import asyncio
import httpx


async def ask():
    print(f"Получаем список сохраненных блокнотов в библиотеке...")
    async with httpx.AsyncClient(timeout=120) as client:
        resp = await client.get(f"http://localhost:3030/notebooks")
        data = resp.json()
        import json

        print(json.dumps(data, indent=2, ensure_ascii=False))

        target_notebook = None
        for nb in data.get("data", {}).get("notebooks", []):
            if nb["name"] == "Tiny_Test":
                target_notebook = nb
                break

        if target_notebook:
            lib_id = target_notebook["id"]

            print(f"\nЗадаем вопрос в блокнот (ID из библиотеки = {lib_id})...")

            resp2 = await client.post(
                f"http://localhost:3030/ask",
                json={
                    "notebook_id": lib_id,
                    "question": "Кратко перечисли основные модули платформы Opencode?",
                },
            )
            print(resp2.json())


if __name__ == "__main__":
    asyncio.run(ask())
