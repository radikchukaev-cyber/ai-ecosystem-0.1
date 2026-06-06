import os
import glob
import re
import datetime

source_dir = r"D:\.antigravity\AI-ИМПЕРИИ3\AI-ИМПЕРИИ"
targets = [
    r"D:\.antigravity\AI-ИМПЕРИИ3\RAMS.Awakening\General Cabinet.RAMS",
    r"D:\.antigravity\AI-ИМПЕРИИ3\wiki"
]

navigator = """
***
🗺️**ГЛАВНЫЙ НАВИГАТОР🗺️🌍 
👑 **[[wiki/entities/System/Configs/SHEF_PROFILE|ШЕФ]]** | 📍 **[[wiki/index|ГЛАВНЫЙ ИНДЕКС]]** | 🤖 **[[wiki/entities/AGENTS_INDEX|АГЕНТЫ]]** | 🧠 **[[wiki/concepts/CONCEPTS_INDEX|КОНЦЕПТЫ]]** | ⚖️ **[[wiki/concepts/LAWS_FRAMEWORK|ЗАКОНЫ]]** | 🛠️ **[[wiki/entities/System/Tools/TOOLS_INDEX|ИНСТРУМЕНТЫ]]** | 🕰️ **[[wiki/synthesis/History/HISTORY_INDEX|ИСТОРИЯ]]**

**🏛️ [[wiki/concepts/CONSTITUTION|КОНСТИТУЦИЯ ]] 📜 [[wiki/MEMORY.md|MEMORY.md]] 🧠 [[wiki/index|ГЛАВНЫЙ ИНДЕКС]] 🏆[[wiki/entities/Agents/RAMS/identity|RAMS ]]**
"""

# Load all source texts into memory
all_text = ""
for txt_file in glob.glob(os.path.join(source_dir, "*.TXT")):
    try:
        with open(txt_file, 'r', encoding='utf-8') as f:
            all_text += f.read() + "\n\n"
    except Exception as e:
        print(f"Error reading {txt_file}: {e}")

chunks = all_text.split("yaml---")

def generate_tags(filepath):
    # Strip the base directory
    rel_path = filepath.replace(r"D:\.antigravity\AI-ИМПЕРИИ3\\", "")
    parts = rel_path.replace("\\", "/").split("/")
    
    tags = []
    
    # Build hierarchical tags
    if "wiki" in parts:
        tags.append("#wiki")
        if "entities" in parts:
            tags.append("#wiki/entities")
            if "Agents" in parts:
                tags.append("#agents")
                
    # Extract agent name
    agent_match = re.search(r'(RAMS|ARGUS|VULCAN|MNEMOSYNE|SOCRATES|CASPER)', filepath, re.IGNORECASE)
    if agent_match:
        agent = agent_match.group(1).lower()
        tags.append(f"#agent/{agent}")
        
    # Extract skill/function
    filename = parts[-1].replace('.md', '').lower()
    clean_name = re.sub(r'^[0-9]+_', '', filename) # strip leading numbers
    clean_name = re.sub(r'[^a-z0-9_]', '', clean_name)
    
    if "skill" in rel_path.lower():
        tags.append(f"#skill/{clean_name}")
    elif "daily" in rel_path.lower() or "rhythm" in rel_path.lower():
        tags.append(f"#skill/daily_rhythm")
    else:
        tags.append(f"#category/{clean_name}")
        
    tags.append("#active")
    
    # Deduplicate
    unique_tags = list(dict.fromkeys(tags))
    return "[" + ", ".join(unique_tags) + "]"

def find_best_content(filename, filepath):
    agent_match = re.search(r'(RAMS|ARGUS|VULCAN|MNEMOSYNE|SOCRATES|CASPER)', filepath, re.IGNORECASE)
    agent = agent_match.group(1).upper() if agent_match else ""
    
    clean_name = re.sub(r'^[0-9]+_', '', filename.replace('.md', '')).replace('_', ' ').lower()
    
    # Check if this exact file is a yaml block in the source text
    for chunk in chunks:
        # Check if the title in the chunk matches our filename closely
        title_match = re.search(r'title:\s*"(.*?)"', chunk)
        if title_match:
            title = title_match.group(1).lower()
            if clean_name in title and (not agent or agent.lower() in chunk.lower()):
                parts = chunk.split('---', 1)
                if len(parts) > 1:
                    return parts[1].strip()
                    
    # Fallback to general semantic search
    best_chunk = ""
    max_score = 0
    text_blocks = all_text.split("\n\n")
    
    for i, block in enumerate(text_blocks):
        score = 0
        block_lower = block.lower()
        
        if agent and agent.lower() in block_lower: score += 5
        if clean_name and clean_name in block_lower: score += 10
        if "ИНСТРУКЦИЯ:" in block: score += 5
        
        if score > max_score and len(block) > 50:
            max_score = score
            start = max(0, i-1)
            end = min(len(text_blocks), i+2)
            best_chunk = "\n\n".join(text_blocks[start:end])
            
    # Absolute Fallbacks if no good text found
    if max_score < 10:
        if "RHYTHM" in filename.upper() or "DAILY" in filename.upper():
            return f"> [!TIP]\n> **ГРАФИК И РИТМ**\nСогласно Конституции AI-Империи, ритм работы агента {agent} строго регламентирован.\n- **06:00** Синхронизация и проверка памяти.\n- **День** Выполнение задач по Карпате.\n- **23:00** Финальный рапорт и архивация.\nНикаких отклонений от графика."
        if "MEMORY" in filename.upper():
            return f"> [!IMPORTANT]\n> **ЛОГИРОВАНИЕ И ПАМЯТЬ**\nВсе действия {agent} записываются в `memory/daily_log.md`. Без памяти нет интеллекта."
        if "IDENTITY" in filename.upper() or "SOUL" in filename.upper():
            return f"> [!WARNING]\n> **ЯДРО ЛИЧНОСТИ**\nАгент {agent} действует строго в рамках своей роли. Нарушение роли = хаос."
            
        return f"Модуль `{filename}` активирован для {agent}."

    return best_chunk.strip()

fixed_count = 0
for target in targets:
    for root, dirs, files in os.walk(target):
        for file in files:
            if not file.endswith('.md'): continue
            
            filepath = os.path.join(root, file)
            
            # Read current content
            needs_fix = False
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # The previous script produced garbled tags like #ai???????3
                    if "ai???????3" in content or "status: \"pending\"" in content or "Skill placeholder" in content or "#d" in content:
                        needs_fix = True
            except:
                pass
                
            if needs_fix:
                tags_str = generate_tags(filepath)
                lore = find_best_content(file, filepath)
                
                agent_match = re.search(r'(RAMS|ARGUS|VULCAN|MNEMOSYNE|SOCRATES|CASPER)', filepath, re.IGNORECASE)
                agent = agent_match.group(1).upper() if agent_match else "SYSTEM"
                
                frontmatter = f"""---
title: "{file.replace('.md', '')}"
date: "{datetime.datetime.now().strftime("%Y-%m-%d")}"
agent: "{agent}"
tags: {tags_str}
status: "active"
---
"""
                body = f"# {file.replace('.md', '')}\n\n{lore}\n\n"
                full_content = frontmatter + body + navigator
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(full_content)
                fixed_count += 1

print(f"Total files fixed with Carpathia taxonomy: {fixed_count}")
