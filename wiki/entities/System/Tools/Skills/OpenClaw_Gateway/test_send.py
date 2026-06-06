import os
import httpx
import asyncio
from dotenv import load_dotenv

# Загрузка токена из .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# ВАЖНО: Укажи chat_id получателя (твоего Telegram аккаунта)
CHAT_ID = "5918052388" 
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

async def send_test_message():
    async with httpx.AsyncClient() as client:
        response = await client.post(TELEGRAM_URL, json={
            "chat_id": CHAT_ID,
            "text": "Сообщение от AI-ИМПЕРИИ3: Проверка шлюза OpenClaw прошла успешно."
        })
        print(f"Статус отправки: {response.status_code}")
        print(f"Ответ API: {response.json()}")

if __name__ == "__main__":
    asyncio.run(send_test_message())
