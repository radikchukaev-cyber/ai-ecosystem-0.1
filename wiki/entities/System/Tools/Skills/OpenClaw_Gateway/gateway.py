import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
import httpx
import logging
import json

# Настройка логирования - будем писать все в stdout
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("GATEWAY_DEBUG")

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
BOT_ID = 8822677933 
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

app = FastAPI()

@app.post("/webhook")
async def telegram_webhook(request: Request):
    try:
        data = await request.json()
        logger.info(f"WEBHOOK_RAW_DATA: {json.dumps(data)}") # Полный дамп
        
        if "message" in data:
            message = data["message"]
            chat_id = message.get("chat", {}).get("id")
            text = message.get("text", "No text")
            
            # Логируем, чтобы мы видели, что это доходит до RAMS
            logger.info(f"RAMS_PERCEPTION: Message received from chat_id={chat_id}, text='{text}'")
            
            # Мгновенный ответ, чтобы подтвердить, что я (RAMS) вижу это
            async with httpx.AsyncClient() as client:
                await client.post(TELEGRAM_URL, json={
                    "chat_id": chat_id,
                    "text": f"RAMS увидел твое сообщение: '{text}'"
                })
        else:
            logger.info("WEBHOOK_DATA: No message field found.")
            
    except Exception as e:
        logger.error(f"WEBHOOK_ERROR: {str(e)}")
        
    return {"status": "ok"}
