import asyncio
import json
import httpx


def print_response(label: str, response: httpx.Response) -> dict | list | None:
    print(f"\n{label}: status={response.status_code}")
    try:
        payload = response.json()
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return payload
    except json.JSONDecodeError:
        print(response.text)
        return None


async def ask():
    notebook_title = "Tiny_Test"
    question = "Summarize the content of this notebook in one sentence."

    print("Проверяем состояние NotebookLM через локальный FastAPI API...")
    async with httpx.AsyncClient(timeout=120) as client:
        health_resp = await client.get("http://localhost:8000/api/v1/notebooklm/health")
        print_response("health", health_resp)

        print("\nПолучаем список блокнотов...")
        resp = await client.get("http://localhost:8000/api/v1/notebooklm/notebooks")
        data = print_response("notebooks", resp)
        if not isinstance(data, list):
            print("\nAPI не вернул список блокнотов, продолжаем нельзя.")
            return

        target_notebook = None
        for nb in data:
            if nb["title"] == notebook_title:
                target_notebook = nb
                break

        if not target_notebook:
            print(f"\nНе найден блокнот с названием {notebook_title}")
            return

        notebook_id = target_notebook["id"]
        print(f"\nЗадаем вопрос в блокнот {notebook_id}...")

        resp2 = await client.post(
            "http://localhost:8000/api/v1/notebooklm/ask",
            json={
                "notebook_id": notebook_id,
                "question": question,
            },
        )
        print_response("ask", resp2)

        print("\nПроверяем batch-роутинг...")
        batch_resp = await client.post(
            "http://localhost:8000/api/v1/notebooklm/ask-batch",
            json={
                "notebook_ids": [notebook_id],
                "question": question,
            },
        )
        print_response("ask-batch", batch_resp)


if __name__ == "__main__":
    asyncio.run(ask())
