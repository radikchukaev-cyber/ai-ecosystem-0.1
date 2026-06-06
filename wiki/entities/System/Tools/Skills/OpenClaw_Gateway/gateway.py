import os
import subprocess
import json
import logging
import httpx
import asyncio
import re
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
    if not os.path.exists(REPO_DIR):
        run_cmd(f"git clone {REPO_URL} {REPO_DIR}")
    else:
        run_cmd("git reset --hard", cwd=REPO_DIR)
        run_cmd("git pull origin main --rebase", cwd=REPO_DIR)

def push_changes(commit_message="Cloud Swarm Update"):
    run_cmd("git add .", cwd=REPO_DIR)
    status = run_cmd("git status --porcelain", cwd=REPO_DIR)
    if not status:
        return False
    run_cmd('git config user.email "cloud-swarm@ai-ecosystem.local"', cwd=REPO_DIR)
    run_cmd('git config user.name "Cloud Swarm Orchestrator"', cwd=REPO_DIR)
    run_cmd(f'git commit -m "{commit_message}"', cwd=REPO_DIR)
    run_cmd("git push origin main", cwd=REPO_DIR)
    return True

async def send_telegram(chat_id, text):
    async with httpx.AsyncClient() as client:
        await client.post(TELEGRAM_URL, json={"chat_id": chat_id, "text": text})

def get_agent_identity(agent_name):
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

async def get_agent_reply(agent_name, prompt):
    try:
        response = await model.generate_content_async(prompt)
        return response.text
    except Exception as e:
        logger.error(f"Error for {agent_name}: {e}")
        return "IGNORE"

async def process_message(chat_id, text, sender="User", depth=0):
    if depth > 3:
        return # Prevent infinite loops
        
    try:
        sync_repo()
        routing_file = os.path.join(REPO_DIR, "wiki", "entities", "System", "Configs", "telegram_routing.json")
        
        target_agents = []
        all_group_agents = set()
        group_config = {}
        
        if os.path.exists(routing_file):
            with open(routing_file, 'r', encoding='utf-8') as f:
                routing_data = json.load(f)
            
            chat_str = str(chat_id)
            if chat_str in routing_data:
                group_config = routing_data[chat_str]
                text_lower = text.lower()
                all_group_agents = set(group_config.get("mentions", {}).values())
                
                # Direct mentions
                for trigger, agent in group_config.get("mentions", {}).items():
                    if trigger in text_lower:
                        target_agents.append(agent)
                        
                # Remove duplicates but keep order
                target_agents = list(dict.fromkeys(target_agents))
                
                # If no direct mention, BROADCAST to all
                if not target_agents and all_group_agents:
                    target_agents = list(all_group_agents)
                    
        if not target_agents:
            target_agents = ["RAMS"]

        memory_path = os.path.join(REPO_DIR, "wiki", "MEMORY.md")
        system_context = ""
        if os.path.exists(memory_path):
            with open(memory_path, "r", encoding="utf-8") as f:
                system_context = f.read()[-3000:]
                
        tasks = []
        is_broadcast = (len(target_agents) > 1) and (sender == "User")
        
        for agent_name in target_agents:
            agent_identity = get_agent_identity(agent_name)
            
            broadcast_instruction = ""
            if is_broadcast:
                broadcast_instruction = "ШЕФ НАПИСАЛ В ОБЩУЮ ГРУППУ. Отвечай только если эта тема напрямую касается твоей компетенции или у тебя есть важное замечание. Если тебе нечего добавить, ответь ровно одним словом: IGNORE"
            
            prompt = f"""
{agent_identity}

ПАМЯТЬ:
{system_context}

Отправитель сообщения: {sender}
СООБЩЕНИЕ В ГРУППЕ:
{text}

Твоя задача: Ответить коротко, в своем характере ({agent_name}). Не выходи из образа.
Если хочешь передать слово другому агенту, просто обратись к нему по имени.
{broadcast_instruction}

Команды [APPEND_MEMORY] и [CREATE_FILE] работают как обычно.
"""
            tasks.append(get_agent_reply(agent_name, prompt))
            
        replies = await asyncio.gather(*tasks)
        changes_made = False
        
        for i, ai_reply in enumerate(replies):
            agent_name = target_agents[i]
            
            # Check if agent decided to ignore the broadcast
            if is_broadcast and ("IGNORE" in ai_reply.strip() or len(ai_reply.strip()) < 10):
                continue
                
            final_reply_text = f"[{agent_name}]:\n" + ai_reply
            
            # Extract Commands
            memory_matches = re.finditer(r"\[APPEND_MEMORY\](.*?)\[/APPEND_MEMORY\]", final_reply_text, re.DOTALL)
            for match in memory_matches:
                memory_content = match.group(1).strip()
                final_reply_text = final_reply_text.replace(match.group(0), "").strip()
                if os.path.exists(memory_path):
                    with open(memory_path, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                    insert_idx = len(lines)
                    for idx in range(len(lines)-1, -1, -1):
                        if lines[idx].startswith("***"):
                            insert_idx = idx
                            break
                    lines.insert(insert_idx, f"\n{memory_content}\n")
                    with open(memory_path, "w", encoding="utf-8") as f:
                        f.writelines(lines)
                    changes_made = True

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
            
            await send_telegram(chat_id, final_reply_text.strip())
            
            # Check for Roundtable Handoff
            if depth < 3 and group_config:
                reply_lower = final_reply_text.lower()
                handoff_targets = []
                for trigger, tgt_agent in group_config.get("mentions", {}).items():
                    if trigger in reply_lower and tgt_agent != agent_name and tgt_agent not in handoff_targets:
                        handoff_targets.append(tgt_agent)
                
                if handoff_targets:
                    # Wait 1 second before passing the mic
                    await asyncio.sleep(1)
                    await process_message(chat_id, final_reply_text, sender=agent_name, depth=depth+1)

        if changes_made:
            push_changes(commit_message="Swarm Activity: Updates from Telegram")
            
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
            if text:
                background_tasks.add_task(process_message, chat_id, text, sender="User", depth=0)
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error"}
