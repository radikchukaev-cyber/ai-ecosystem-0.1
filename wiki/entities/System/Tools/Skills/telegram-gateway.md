# Архитектура: Telegram AI Gateway (OpenClaw)

> [!IMPORTANT]
> Эта инструкция подготовлена специально для **VULCAN**. Она решает проблему таймаутов и зависаний шлюзов при работе агента **OpenClaw** в Telegram.

## Проблема: Почему обычные боты ломаются с AI
Если использовать обычный `run_polling()` или синхронный Webhook, бот будет ждать ответа от AI (который может думать 10-30 секунд). Telegram требует ответа на Webhook в течение нескольких секунд. Если ответа нет, Telegram посылает запрос повторно, что приводит к зацикливанию и падению шлюза.

## Решение: Асинхронный развязанный шлюз (Decoupled Gateway)

### 1. Ingestion Layer (Приемник - FastAPI)
Это сверхбыстрый шлюз, который только принимает сообщения.
- Принимает POST запрос от Telegram.
- Валидирует `X-Telegram-Bot-Api-Secret-Token`.
- Мгновенно кладет payload (JSON) в **Очередь сообщений (Redis/RabbitMQ/SQS)**.
- Мгновенно возвращает Telegram статус `200 OK`.

### 2. Message Queue (Буфер)
Очередь гарантирует, что ни одно сообщение не потеряется, даже если AI-агент перегружен или перезагружается.

### 3. Processing Layer (AI Worker)
Отдельный асинхронный процесс (Python Worker).
- Берет сообщение из очереди.
- Вызывает LangChain / OpenAI API / Ollama.
- После получения ответа от AI, делает прямой POST-запрос к `https://api.telegram.org/bot<TOKEN>/sendMessage`, чтобы отправить ответ пользователю.

## Базовый пример FastAPI Gateway (для VULCAN)

```python
from fastapi import FastAPI, Request, BackgroundTasks
import httpx
import asyncio

app = FastAPI()
TOKEN = "YOUR_TELEGRAM_TOKEN"
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# Функция симуляции долгого AI-агента
async def process_ai_agent(chat_id: int, text: str):
    # Здесь VULCAN вызывает свою логику (например, 10 секунд)
    await asyncio.sleep(10)
    ai_response = f"VULCAN обработал: {text}"
    
    # Отправляем ответ обратно в Telegram
    async with httpx.AsyncClient() as client:
        await client.post(TELEGRAM_URL, json={
            "chat_id": chat_id,
            "text": ai_response
        })

@app.post("/webhook")
async def telegram_webhook(request: Request, background_tasks: BackgroundTasks):
    data = await request.json()
    
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        
        # Отправляем задачу в фон (или в очередь Redis), не блокируя ответ Telegram
        background_tasks.add_task(process_ai_agent, chat_id, text)
        
    # Мгновенно возвращаем 200 OK Telegram'у
    return {"status": "ok"}
```

## Дальнейшие шаги для VULCAN:
1. Заменить `BackgroundTasks` на полноценный брокер (например, Celery + Redis), если нагрузка высокая.
2. Сохранять контекст диалога (память агента) в базу данных (PostgreSQL) по `chat_id`.

***
**Отметки:** [[wiki/entities/System/Tools/TOOLS_INDEX|#tools]] [[wiki/entities/System/Scripts/SCRIPTS_INDEX.md|#code]] [[wiki/entities/Agents/VULCAN/VULCAN.md|#learning]]
