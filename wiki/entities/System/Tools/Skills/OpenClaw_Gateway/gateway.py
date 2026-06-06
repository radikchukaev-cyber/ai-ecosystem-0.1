import os
import subprocess
import json
import logging
import httpx
from fastapi import FastAPI, Request, BackgroundTasks
import google.generativeai as genai

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("CLOUD_SWARM")

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
        run_cmd("git reset --hard", cwd=REPO_DIR)
        run_cmd("git pull origin main --rebase", cwd=REPO_DIR)

def push_changes(commit_message="Cloud Swarm Update"):
    """Pushes changes back to GitHub."""
    run_cmd("git add .", cwd=REPO_DIR)
    status = run_cmd("git status --porcelain", cwd=REPO_DIR)
    if not status:
        return False
        
    run_cmd('git config user.email "cloud-swarm@ai-ecosystem.local"', cwd=REPO_DIR)
    run_cmd('git config user.name "Cloud Swarm Orchestrator"', cwd=REPO_DIR)
    run_cmd(f'git commit -m "{commit_message}"', cwd=REPO_DIR)
    run_cmd("git push origin main", cwd=REPO_DIR)
    logger.info("Changes pushed to GitHub successfully.")
    return True

async def send_telegram(chat_id, text):
    async with httpx.AsyncClient() as client:
        await client.post(TELEGRAM_URL, json={
            "chat_id": chat_id,
            "text": text
        })

def get_routing_info(chat_id, text):
    """Determine which agent should reply based on chat_id and mentions."""
    routing_file = os.path.join(REPO_DIR, "wiki", "entities", "System", "Configs", "telegram_routing.json")
    default_agent = "RAMS"
    
    if not os.path.exists(routing_file):
        return default_agent

    try:
        with open(routing_file, 'r', encoding='utf-8') as f:
            routing_data = json.load(f)
            
        chat_str = str(chat_id)
        if chat_str in routing_data:
            group_config = routing_data[chat_str]
            text_lower = text.lower()
            
            # Check mentions
            for mention_trigger, target_agent in group_config.get("mentions", {}).items():
                if mention_trigger in text_lower:
                    return target_agent
                    
            return group_config.get("default", default_agent)
            
    except Exception as e:
        logger.error(f"Routing Error: {e}")
        
    return default_agent

def get_agent_identity(agent_name):
    """Read the agent's core files to build their identity prompt."""
    agent_dir = os.path.join(REPO_DIR, "wiki", "entities", "Agents", agent_name)
    identity_text = f"Ты — Субагент {agent_name} экосистемы AI-ИМПЕРИЯ.\n"
    
    if os.path.exists(agent_dir):
        files_to_read = ['identity.md', 'soul.md', 'laws.md', f'{agent_name}.md']
        for file in files_to_read:
            path = os.path.join(agent_dir, file)
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    identity_text += f"\n--- {file} ---\n{f.read()}\n"
    else:
        identity_text += "Твой офис пока не инициализирован, но ты существуешь. Действуй согласно своему имени.\n"
        
    return identity_text

async def process_message(chat_id, text):
    try:
        sync_repo()
        
        agent_name = get_routing_info(chat_id, text)
        agent_identity = get_agent_identity(agent_name)
        
        memory_path = os.path.join(REPO_DIR, "wiki", "MEMORY.md")
        system_context = ""
        if os.path.exists(memory_path):
            with open(memory_path, "r", encoding="utf-8") as f:
                system_context = f.read()[-3000:]
                
        prompt = f"""
{agent_identity}

Твоя текущая рабочая директория: {REPO_DIR}

ПОСЛЕДНИЕ СОБЫТИЯ В ОБЩЕЙ ПАМЯТИ (MEMORY.md):
{system_context}

СООБЩЕНИЕ ИЛИ ПРИКАЗ ИЗ ТЕЛЕГРАМ-ГРУППЫ:
{text}

Твоя задача: Ответить коротко, по делу, ИМЕННО В СВОЕМ ХАРАКТЕРЕ И СВОЕЙ РОЛИ ({agent_name}). Не выходи из образа.
КРИТИЧЕСКИЕ ПРАВИЛА ОБЩЕНИЯ:
1. В Telegram идет живой диалог. Будь краток.
2. ВАЖНОЕ ПРАВИЛО: Ты НЕ ДОЛЖЕН создавать отдельные файлы логов или журналов для разговоров. Мы — единый мозг. Вся память хранится строго в wiki/MEMORY.md.
3. Если тебя просят что-то запомнить, зафиксировать или если ты сделал важную работу, ты ОБЯЗАН использовать команду [APPEND_MEMORY].

Формат команды для записи в память (ОБЯЗАТЕЛЬНО С НОВОЙ СТРОКИ):
[APPEND_MEMORY]
**[Текущее время] {agent_name} (Telegram Swarm):**
- **Действие/Запись:** [подробное описание того, что ты сделал]
[/APPEND_MEMORY]

Формат команды для создания рабочих файлов (ОБЯЗАТЕЛЬНО С НОВОЙ СТРОКИ):
[CREATE_FILE]
path: относительный/путь/к/файлу.md
content: содержимое файла
[/CREATE_FILE]
"""
        response = model.generate_content(prompt)
        ai_reply = response.text
        
        import re
        changes_made = False
        final_reply_text = f"[{agent_name}]:\n" + ai_reply
        
        # Parse APPEND_MEMORY
        memory_matches = re.finditer(r"\[APPEND_MEMORY\](.*?)\[/APPEND_MEMORY\]", final_reply_text, re.DOTALL)
        for match in memory_matches:
            memory_content = match.group(1).strip()
            final_reply_text = final_reply_text.replace(match.group(0), "").strip()
            
            if os.path.exists(memory_path):
                with open(memory_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                insert_idx = len(lines)
                for i in range(len(lines)-1, -1, -1):
                    if lines[i].startswith("***"):
                        insert_idx = i
                        break
                lines.insert(insert_idx, f"\n{memory_content}\n")
                with open(memory_path, "w", encoding="utf-8") as f:
                    f.writelines(lines)
                changes_made = True

        # Parse CREATE_FILE
        file_matches = re.finditer(r"\[CREATE_FILE\](.*?)\[/CREATE_FILE\]", final_reply_text, re.DOTALL)
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

        if changes_made:
            push_changes(commit_message=f"Swarm Activity: {agent_name} update")
            final_reply_text += "\n\n[GitHub Sync]: Изменения сохранены."
            
        await send_telegram(chat_id, final_reply_text.strip())
        
    except Exception as e:
        logger.error(f"Error processing message: {e}")
        await send_telegram(chat_id, f"❌ [Swarm Error]: {str(e)}")

@app.post("/webhook")
async def telegram_webhook(request: Request, background_tasks: BackgroundTasks):
    try:
        data = await request.json()
        if "message" in data:
            chat_id = data["message"]["chat"]["id"]
            text = data["message"].get("text", "")
            background_tasks.add_task(process_message, chat_id, text)
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error"}
