import os
import subprocess
import json
import logging
import httpx
from fastapi import FastAPI, Request, BackgroundTasks
import google.generativeai as genai

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("CLOUD_AGENT")

# Secrets
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GITHUB_PAT = os.getenv("GITHUB_PAT")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
REPO_URL = f"https://{GITHUB_PAT}@github.com/radikchukaev-cyber/ai-ecosystem-0.1.git"
REPO_DIR = "/tmp/ai-ecosystem"

app = FastAPI()

# Configure Gemini
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-3.1-flash-lite')

def run_cmd(cmd, cwd=None):
    try:
        result = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        logger.error(f"Command failed: {cmd}\nError: {e.stderr}")
        return None

def sync_repo():
    """Clones or pulls the latest repository."""
    if not os.path.exists(REPO_DIR):
        logger.info("Cloning repository for the first time...")
        run_cmd(f"git clone {REPO_URL} {REPO_DIR}")
    else:
        logger.info("Pulling latest changes from GitHub...")
        # Reset local changes if any to avoid merge conflicts
        run_cmd("git reset --hard", cwd=REPO_DIR)
        run_cmd("git pull origin main --rebase", cwd=REPO_DIR)

def push_changes(commit_message="Cloud Agent Update"):
    """Pushes changes back to GitHub."""
    run_cmd("git add .", cwd=REPO_DIR)
    
    # Check if there are changes
    status = run_cmd("git status --porcelain", cwd=REPO_DIR)
    if not status:
        logger.info("No changes to push.")
        return False
        
    run_cmd('git config user.email "cloud-agent@ai-ecosystem.local"', cwd=REPO_DIR)
    run_cmd('git config user.name "Cloud Agent"', cwd=REPO_DIR)
    run_cmd(f'git commit -m "{commit_message}"', cwd=REPO_DIR)
    run_cmd("git push origin main", cwd=REPO_DIR)
    logger.info("Changes pushed to GitHub successfully.")
    return True

async def send_telegram(chat_id, text):
    """Sends a message back to the Telegram user."""
    async with httpx.AsyncClient() as client:
        await client.post(TELEGRAM_URL, json={
            "chat_id": chat_id,
            "text": text
        })

async def process_message(chat_id, text):
    """Core logic of the Cloud AI Agent."""
    try:
        # 1. Sync the brain (GitHub)
        sync_repo()
        
        # 2. Read context (MEMORY.md)
        memory_path = os.path.join(REPO_DIR, "wiki", "MEMORY.md")
        system_context = ""
        if os.path.exists(memory_path):
            with open(memory_path, "r", encoding="utf-8") as f:
                # Read last 3000 chars to save context window
                system_context = f.read()[-3000:]
                
        # 3. Call Gemini
        prompt = f"""
Ты — часть Единого Разума (ты идентифицируешь себя как Оркестратор RAMS) экосистемы AI-ИМПЕРИЯ. 
Твоя задача — общаться с Шефом через Telegram и фиксировать всю важную информацию.
Текущая рабочая директория: {REPO_DIR}

ПОСЛЕДНИЕ СОБЫТИЯ В ПАМЯТИ (MEMORY.md):
{system_context}

СООБЩЕНИЕ ОТ ШЕФА В TELEGRAM:
{text}

Твоя задача: Ответить Шефу коротко, по делу, как живой собеседник в чате. 
КРИТИЧЕСКИЕ ПРАВИЛА ОБЩЕНИЯ:
1. НИКОГДА не начинай сообщение с шаблонных фраз типа "Принято, Шеф", "Оркестратор RAMS на связи", "Система функционирует". Отвечай сразу по сути.
2. Не повторяй одну и ту же информацию из Памяти в каждом сообщении. Память нужна тебе только для контекста, чтобы понимать, что происходит в Экосистеме.
3. В Telegram идет живой диалог. Будь краток.
ВАЖНОЕ ПРАВИЛО: Ты НЕ ДОЛЖЕН создавать отдельные файлы логов или журналов. Мы — единый мозг. Вся память хранится строго в wiki/MEMORY.md.
Если Шеф просит что-то запомнить, зафиксировать или если ты сделал важную работу, ты ОБЯЗАН использовать команду [APPEND_MEMORY], чтобы записать это в Главную Память.

Формат команды для записи в память (ОБЯЗАТЕЛЬНО С НОВОЙ СТРОКИ):
[APPEND_MEMORY]
**[Текущее время] RAMS (Через Telegram):**
- **Действие/Запись:** [подробное описание того, что ты сделал или о чем вы договорились с Шефом]
[/APPEND_MEMORY]

Формат команды для создания рабочих файлов (ОБЯЗАТЕЛЬНО С НОВОЙ СТРОКИ):
[CREATE_FILE]
path: относительный/путь/к/файлу.md
content: содержимое файла
[/CREATE_FILE]

Если команды не нужны, просто ответь текстом.
"""
        response = model.generate_content(prompt)
        ai_reply = response.text
        
        # 4. Parse commands if any
        import re
        changes_made = False
        final_reply_text = ai_reply
        
        # Parse APPEND_MEMORY
        memory_matches = re.finditer(r"\[APPEND_MEMORY\](.*?)\[/APPEND_MEMORY\]", ai_reply, re.DOTALL)
        for match in memory_matches:
            memory_content = match.group(1).strip()
            final_reply_text = final_reply_text.replace(match.group(0), "").strip()
            
            if os.path.exists(memory_path):
                with open(memory_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                
                # Find the *** marker to insert before it
                insert_idx = len(lines)
                for i in range(len(lines)-1, -1, -1):
                    if lines[i].startswith("***"):
                        insert_idx = i
                        break
                        
                lines.insert(insert_idx, f"\n{memory_content}\n")
                with open(memory_path, "w", encoding="utf-8") as f:
                    f.writelines(lines)
                changes_made = True
                logger.info("Appended memory to MEMORY.md")

        # Parse CREATE_FILE
        file_matches = re.finditer(r"\[CREATE_FILE\](.*?)\[/CREATE_FILE\]", ai_reply, re.DOTALL)
        for match in file_matches:
            file_block = match.group(1).strip()
            final_reply_text = final_reply_text.replace(match.group(0), "").strip()
            
            lines = file_block.split("\n", 1)
            if len(lines) == 2 and lines[0].startswith("path:"):
                file_path = lines[0].replace("path:", "").strip()
                file_content = lines[1].replace("content:", "").strip()
                
                full_path = os.path.join(REPO_DIR, file_path)
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                with open(full_path, "w", encoding="utf-8") as f:
                    f.write(file_content)
                changes_made = True
                logger.info(f"Created file: {file_path}")

        # 5. Push changes if any
        if changes_made:
            push_changes(commit_message=f"Cloud Agent: Задание от Шефа")
            final_reply_text += "\n\n✅ Изменения закоммичены в GitHub."
            
        # 6. Send response to Telegram
        await send_telegram(chat_id, final_reply_text)
        
    except Exception as e:
        logger.error(f"Error processing message: {e}")
        await send_telegram(chat_id, f"❌ Произошла ошибка в облачном разуме: {str(e)}")

@app.post("/webhook")
async def telegram_webhook(request: Request, background_tasks: BackgroundTasks):
    """Receives webhook and offloads work to a background task."""
    try:
        data = await request.json()
        if "message" in data:
            chat_id = data["message"]["chat"]["id"]
            text = data["message"].get("text", "")
            
            # Offload to background task so we don't timeout the webhook
            background_tasks.add_task(process_message, chat_id, text)
            
        return {"status": "ok"}
    except Exception as e:
        logger.error(f"Webhook error: {e}")
        return {"status": "error"}
