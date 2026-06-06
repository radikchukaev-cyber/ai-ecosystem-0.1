import os
import glob
import re
import datetime

source_dir = r"D:\.antigravity\AI-ИМПЕРИИ3\AI-ИМПЕРИИ"
target_dir = r"D:\.antigravity\AI-ИМПЕРИИ3\RAMS.Awakening\General Cabinet.RAMS\RAMS.AGENTS.md"

navigator = '''
***
🗺️**ГЛАВНЫЙ НАВИГАТОР🗺️🌍 
👑 **[[wiki/entities/System/Configs/SHEF_PROFILE|ШЕФ]]** | 📍 **[[wiki/index|ГЛАВНЫЙ ИНДЕКС]]** | 🤖 **[[wiki/entities/AGENTS_INDEX|АГЕНТЫ]]** | 🧠 **[[wiki/concepts/CONCEPTS_INDEX|КОНЦЕПТЫ]]** | ⚖️ **[[wiki/concepts/LAWS_FRAMEWORK|ЗАКОНЫ]]** | 🛠️ **[[wiki/entities/System/Tools/TOOLS_INDEX|ИНСТРУМЕНТЫ]]** | 🕰️ **[[wiki/synthesis/History/HISTORY_INDEX|ИСТОРИЯ]]**
'''

# 1. Load all source data
all_text = ""
for txt_file in glob.glob(os.path.join(source_dir, "*.TXT")):
    try:
        with open(txt_file, 'r', encoding='utf-8') as f:
            all_text += f.read() + "\n\n"
    except Exception as e:
        print(f"Error reading {txt_file}: {e}")

# 2. Extract Skills (split by yaml---)
skills_raw = re.split(r'yaml---', all_text)
parsed_skills = []
for block in skills_raw[1:]:
    # Try to extract agent and title
    title_match = re.search(r'title:\s*"(.*?)"', block)
    agent_match = re.search(r'agent:\s*"(.*?)"', block)
    
    if title_match and agent_match:
        title = title_match.group(1)
        agent = agent_match.group(1).upper()
        # The body is everything after ---
        parts = block.split('---', 1)
        if len(parts) > 1:
            body = parts[1].strip()
            parsed_skills.append({'agent': agent, 'title': title, 'body': body})

# Print how many skills found
print(f"Found {len(parsed_skills)} total skills.")

# 3. Agent base lore (Fallback mapping)
agent_lore = {
    "ARGUS": {"color": "Red", "role": "Perception Filter", "desc": "Очищает данные, ищет факты, парсит raw."},
    "VULCAN": {"color": "Green", "role": "Execution & Action", "desc": "Пишет код, скрипты, интеграции, Vault Manager."},
    "MNEMOSYNE": {"color": "Yellow", "role": "Memory Keeper", "desc": "Организует файлы по методу Карпаты, следит за тегами."},
    "SOCRATES": {"color": "Purple", "role": "Reflection", "desc": "Анализ корня проблем (Root Cause Analysis), эволюция."},
    "CASPER": {"color": "Cyber-Samurai", "role": "Guardian", "desc": "Бэкапы, защита от потери данных, очистка."}
}

# 4. Map the deeply nested files
for agent_folder in os.listdir(target_dir):
    agent_path = os.path.join(target_dir, agent_folder)
    if not os.path.isdir(agent_path): continue
    
    # Extract agent name from folder (e.g. 14.Argus.Awakening -> ARGUS)
    agent_name_match = re.search(r'\.(.*?)\.', agent_folder)
    if not agent_name_match: continue
    agent_name = agent_name_match.group(1).upper()
    
    # Get this agent's skills
    my_skills = [s for s in parsed_skills if s['agent'] == agent_name]
    
    # Walk through all deep files for this agent
    for root, dirs, files in os.walk(agent_path):
        for file in files:
            if not file.endswith('.md'): continue
            
            filepath = os.path.join(root, file)
            filename = file.replace('.md', '')
            
            # Determine Category / Tag
            cat = "general"
            if "SKILL" in filename.upper() or "SKILL" in root.upper(): cat = "skills"
            elif "TOOL" in filename.upper() or "TOOL" in root.upper(): cat = "tools"
            elif "MEMORY" in filename.upper() or "MEMORY" in root.upper(): cat = "memory"
            elif "RHYTHM" in filename.upper() or "RHYTHM" in root.upper(): cat = "daily_rhythm"
            elif "BOOTSTRAP" in filename.upper() or "BOOTSTRAP" in root.upper(): cat = "bootstrap"
            
            # Formulate the body
            body_content = f"# {filename}\n\n"
            
            if cat == "skills":
                if len(my_skills) > 0:
                    body_content += "> [!IMPORTANT]\n> **ИМПЛАНТАЦИЯ СКИЛЛОВ**\n\nНиже загружены все извлеченные навыки для этого агента:\n\n"
                    for sk in my_skills:
                        body_content += f"## {sk['title']}\n"
                        # Append a snippet or the full body (limit to avoid giant files, but we need full)
                        body_content += sk['body'] + "\n\n---\n\n"
                else:
                    body_content += f"> [!NOTE]\n> **ОЖИДАНИЕ СКИЛЛОВ**\nДля агента {agent_name} скиллы еще загружаются из базы данных.\n"
                    
            elif cat == "daily_rhythm":
                body_content += f"> [!TIP]\n> **РАСПИСАНИЕ АГЕНТА**\nАгент {agent_name} выполняет роль: {agent_lore.get(agent_name, {}).get('role', 'Unknown')}.\nЕжедневный ритм включает синхронизацию в 06:00, работу по пулу задач, и рапорт в 23:00.\n"
                
            elif cat == "memory":
                body_content += f"> [!IMPORTANT]\n> **ПАМЯТЬ АГЕНТА**\nЗаписи ведутся строго по формату.\n"
                
            else:
                body_content += f"> [!NOTE]\n> **ПРОТОКОЛ**\nАктивация модуля {filename} для агента {agent_name}.\n"
            
            # Beautiful YAML Frontmatter
            tags = f"[#{agent_name.lower()}, #{cat}, #awakening, #deep_lore]"
            frontmatter = f"""---
title: "{filename}"
agent: "{agent_name}"
date: "{datetime.datetime.now().strftime("%Y-%m-%d")}"
category: "{cat}"
tags: {tags}
status: "active"
---
"""
            # Write out
            full_content = frontmatter + "\n" + body_content + "\n\n" + navigator
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(full_content)

print("Deep injection complete.")
