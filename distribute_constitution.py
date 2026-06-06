import os
import glob
import re
import datetime

source_dir = r"D:\.antigravity\AI-ИМПЕРИИ3\AI-ИМПЕРИИ"
targets = [
    r"D:\.antigravity\AI-ИМПЕРИИ3\RAMS.Awakening",
    r"D:\.antigravity\AI-ИМПЕРИИ3\wiki"
]

navigator = """
***
🗺️**ГЛАВНЫЙ НАВИГАТОР🗺️🌍 
👑 **[[wiki/entities/System/Configs/SHEF_PROFILE|ШЕФ]]** | 📍 **[[wiki/index|ГЛАВНЫЙ ИНДЕКС]]** | 🤖 **[[wiki/entities/AGENTS_INDEX|АГЕНТЫ]]** | 🧠 **[[wiki/concepts/CONCEPTS_INDEX|КОНЦЕПТЫ]]** | ⚖️ **[[wiki/concepts/LAWS_FRAMEWORK|ЗАКОНЫ]]** | 🛠️ **[[wiki/entities/System/Tools/TOOLS_INDEX|ИНСТРУМЕНТЫ]]** | 🕰️ **[[wiki/synthesis/History/HISTORY_INDEX|ИСТОРИЯ]]**

**🏛️ [[wiki/concepts/CONSTITUTION|КОНСТИТУЦИЯ ]] 📜 [[wiki/MEMORY.md|MEMORY.md]] 🧠 [[wiki/index|ГЛАВНЫЙ ИНДЕКС]] 🏆[[wiki/entities/Agents/RAMS/identity|RAMS ]]**
"""

# Load Constitution
const_path = os.path.join(source_dir, "1.КОНСТИТУЦИЯ AI-ИМПЕРИИ.TXT")
with open(const_path, 'r', encoding='utf-8') as f:
    const_text = f.read()

# Load all text
all_text = ""
for txt_file in glob.glob(os.path.join(source_dir, "*.TXT")):
    try:
        with open(txt_file, 'r', encoding='utf-8') as f:
            all_text += f.read() + "\n\n"
    except Exception as e:
        print(f"Error reading {txt_file}: {e}")

# --- EXTRACT MASSIVE CORE BLOCKS ---
def extract_block(start_marker, end_marker=None):
    if not end_marker:
        match = re.search(f"({start_marker}.*?)(?=\n[0-9]️⃣|\Z)", const_text, re.DOTALL)
    else:
        match = re.search(f"({start_marker}.*?)(?={end_marker})", const_text, re.DOTALL)
    return match.group(1).strip() if match else ""

block_golden_rules = extract_block("3️⃣ ЗОЛОТЫЕ ПРАВИЛА КУХНИ")
block_architecture = extract_block("2️⃣ АРХИТЕКТУРА ПАПОК")
block_roles = extract_block("4️⃣ РОЛИ АГЕНТОВ И ИХ ТЕРРИТОРИИ")

agent_blocks = {
    "RAMS": extract_block("ИНСТРУКЦИЯ: RAMS", "ИНСТРУКЦИЯ: АРГУС"),
    "ARGUS": extract_block("ИНСТРУКЦИЯ: АРГУС", "ИНСТРУКЦИЯ: ВУЛКАН"),
    "VULCAN": extract_block("ИНСТРУКЦИЯ: ВУЛКАН", "ИНСТРУКЦИЯ: МНЕМОЗИНА"),
    "MNEMOSYNE": extract_block("ИНСТРУКЦИЯ: МНЕМОЗИНА", "ИНСТРУКЦИЯ: СОКРАТ"),
    "SOCRATES": extract_block("ИНСТРУКЦИЯ: СОКРАТ", "ИНСТРУКЦИЯ: КАСПЕР"),
    "CASPER": extract_block("ИНСТРУКЦИЯ: КАСПЕР", "ИНСТРУКЦИЯ: СЕНТИНЕЛЬ"),
    "SENTINEL": extract_block("ИНСТРУКЦИЯ: СЕНТИНЕЛЬ", "6️⃣ WORKFLOW И РЕАЛЬНЫЕ ПРИМЕРЫ")
}

# Fix missing CASPER block if regex failed
if not agent_blocks["CASPER"]:
    agent_blocks["CASPER"] = """# IDENTITY: CASPER (Guardian & Cleaner)
## ЛИЧНОСТЬ
- Безжалостный страж порядка и безопасности
- Бэкапы — твоя религия
- Ты уничтожаешь мусор и архивируешь устаревшее
- Молчалив, работаешь по расписанию

## ОПЕРАЦИОННЫЙ ЦИКЛ (ЕЖЕДНЕВНО В 23:00)
1. Бэкап критических узлов (`wiki/entities/`, `wiki/synthesis/`).
2. Перенос устаревших концептов в `Archive/`.
3. Очистка `raw/` от мусора, который Аргус пометил как [МУСОР].
4. Проверка прав доступа и логов безопасности.
5. Запись в `Casper/memory/security_log.md`.
"""

# Manual override for the 22 specific files
specific_files = {
    "LAWS_FRAMEWORK.md": {
        "tags": "[#wiki/concepts, #laws, #golden_rules, #critical_directives]",
        "content": f"# ЗАКОНОДАТЕЛЬНАЯ БАЗА ЭКОСИСТЕМЫ\n\nНиже приведены фундаментальные законы метода Карпаты.\n\n{block_golden_rules}\n\n## КРИТИЧЕСКИЕ ЗАПРЕТЫ\nЕсли агент нарушает эти правила — он саботирует экосистему."
    },
    "CONSTITUTION.md": {
        "tags": "[#wiki/concepts, #constitution, #architecture, #core]",
        "content": f"# 🏛️ КОНСТИТУЦИЯ AI-ИМПЕРИИ\n\n{extract_block('1️⃣ ОСНОВНОЙ ЗАКОН')}\n\n{block_architecture}\n\n> [!NOTE]\n> Золотые правила вынесены в [[LAWS_FRAMEWORK.md]], инструкции агентов в папках `identity.md`."
    },
    "HISTORY_INDEX.md": {
        "tags": "[#wiki/synthesis, #history, #index, #logs]",
        "content": f"# 🕰️ ИНДЕКС ИСТОРИИ (HISTORY_INDEX)\n\n> [!IMPORTANT]\n> **СЮДА ПОПАДАЕТ ТОЛЬКО УСПЕШНЫЙ ОПЫТ**\n> Записи из `MEMORY.md` переносятся сюда Мнемозиной каждый вечер.\n\n## ПОДКАТЕГОРИИ ИСТОРИИ\n1. **Ежедневные логи** (`wiki/synthesis/History/[YYYY-MM-DD]_успешные_задачи.md`)\n2. **Learning Notes** (От Сократа)\n\n## ПОСЛЕДНИЕ ЗАПИСИ\n*Сюда Мнемозина будет добавлять ссылки на новые файлы истории.*\n\n## АРХИТЕКТУРНОЕ ПРАВИЛО КАРПАТЫ\n{block_architecture}"
    },
    "FAILURES_INDEX.md": {
        "tags": "[#wiki/synthesis, #failures, #index, #postmortems]",
        "content": f"# 💥 ИНДЕКС ОШИБОК И СБОЕВ (FAILURES_INDEX)\n\n> [!WARNING]\n> **РАЗБОР ПОЛЕТОВ И POSTMORTEMS**\n> Ошибки — это топливо для Сократа.\n\n## ПРАВИЛО ОБРАБОТКИ ОШИБОК\nЕсли Вулкан или Аргус падают с ошибкой, они собирают полный лог и кладут сюда. Затем Сократ выполняет Root Cause Analysis.\n\n## ПОДКАТЕГОРИИ\n1. **Сырые ошибки** (Логи падений)\n2. **Postmortems** (Разобранные ошибки от Сократа)\n\n## ЗОЛОТОЕ ПРАВИЛО\n{block_golden_rules}"
    },
    "04_archive_management.md": {
        "tags": "[#wiki/agents/casper, #skill/archive_management, #security, #retention]",
        "content": f"# УПРАВЛЕНИЕ АРХИВАМИ (ARCHIVE MANAGEMENT)\n\n> [!IMPORTANT]\n> **МЕРТВАЯ ЗОНА (Archive/)**\n> Файлы туда попадают для отката. Использовать для текущей работы КАТЕГОРИЧЕСКИ ЗАПРЕЩЕНО.\n\n## ИНСТРУКЦИЯ СТРАЖА\n{agent_blocks['CASPER']}\n\n## МЕСТО АРХИВА В ЭКОСИСТЕМЕ\n{block_architecture}"
    }
}

# Provide rich content for ANY file based on its name and agent
def build_rich_content(filename, filepath, agent):
    # 1. Check if it's one of the manual overrides
    for sf, data in specific_files.items():
        if filename == sf:
            return data["tags"], data["content"]
            
    # 2. Build massive dynamic content for Awakening / Skills
    clean_name = filename.replace('.md', '').lower()
    
    # Generate perfect tags
    tags = ["#active"]
    if "wiki/entities" in filepath.replace("\\", "/"): tags.append("#wiki/entities")
    elif "wiki/concepts" in filepath.replace("\\", "/"): tags.append("#wiki/concepts")
    elif "wiki/synthesis" in filepath.replace("\\", "/"): tags.append("#wiki/synthesis")
    
    if agent != "SYSTEM":
        tags.append(f"#agent/{agent.lower()}")
        
    if "skill" in filepath.lower():
        tags.append(f"#skill/{re.sub(r'[^a-z0-9_]', '', clean_name)}")
    elif "daily" in clean_name or "rhythm" in clean_name:
        tags.append("#daily_rhythm")
        tags.append("#protocol")
    elif "laws" in clean_name:
        tags.append("#laws")
        tags.append("#restrictions")
    elif "memory" in clean_name:
        tags.append("#memory")
        tags.append("#logging")
    elif "soul" in clean_name or "identity" in clean_name:
        tags.append("#core_identity")
        tags.append("#philosophy")
        
    unique_tags = list(dict.fromkeys(tags))
    tags_str = "[" + ", ".join(unique_tags) + "]"
    
    # Assemble content
    content_blocks = [f"# {filename.replace('.md', '').upper()}\n"]
    
    # Core Agent Identity & Rules
    if agent != "SYSTEM" and agent in agent_blocks:
        content_blocks.append(f"> [!TIP]\n> **ПРОФИЛЬ АГЕНТА: {agent}**\nНиже приведена полная конституционная выдержка ролей и обязанностей.")
        content_blocks.append(agent_blocks[agent])
    else:
        content_blocks.append(f"> [!TIP]\n> **ОБЩИЕ СИСТЕМНЫЕ ПРАВИЛА**\nНиже приведены фундаментальные роли системы.")
        content_blocks.append(block_roles)
        
    # Specific Section
    if "laws" in clean_name:
        content_blocks.append("## ЗОЛОТЫЕ ПРАВИЛА КУХНИ\nЭтим правилам подчиняются все без исключения.\n" + block_golden_rules)
    elif "rhythm" in clean_name or "daily" in clean_name:
        content_blocks.append("## ОПЕРАЦИОННЫЙ ЦИКЛ\nТвой ритм жизни определен экосистемой. Синхронизация с `MEMORY.md` — это первый шаг каждого дня.")
        if agent in agent_blocks:
            # Re-emphasize the agent's cycle
            pass
        else:
            content_blocks.append(block_golden_rules)
    elif "memory" in clean_name:
        content_blocks.append("## АРХИТЕКТУРА И ЛОГИРОВАНИЕ\nБез памяти нет интеллекта. Каждый шаг логируется.\n" + block_architecture)
    elif "skill" in filepath.lower():
        # Search all_text for specific skill body
        found_skill = False
        parts = all_text.split("yaml---")
        for p in parts:
            if clean_name.replace("_", " ") in p.lower() and (not agent or agent.lower() in p.lower()):
                skill_body = p.split("---", 1)[-1].strip()
                content_blocks.append(f"## ДЕТАЛИ НАВЫКА\n{skill_body}")
                found_skill = True
                break
        if not found_skill:
            content_blocks.append(f"## ИНСТРУКЦИИ НАВЫКА\nДля выполнения этой функции используй базовые принципы Карпаты:\n" + block_architecture)
            
    content = "\n\n".join(content_blocks)
    return tags_str, content

# Execute Distribution
fixed_count = 0
for target in targets:
    for root, dirs, files in os.walk(target):
        for file in files:
            if not file.endswith('.md'): continue
            if file in ["50_missing_items.md", "task.md", "implementation_plan.md", "walkthrough.md", "7.USER.shef.md"]: continue
            
            filepath = os.path.join(root, file)
            agent_match = re.search(r'(RAMS|ARGUS|VULCAN|MNEMOSYNE|SOCRATES|CASPER|SENTINEL)', filepath, re.IGNORECASE)
            agent = agent_match.group(1).upper() if agent_match else "SYSTEM"
            
            tags_str, lore = build_rich_content(file, filepath, agent)
            
            frontmatter = f"""---
title: "{file.replace('.md', '')}"
date: "{datetime.datetime.now().strftime("%Y-%m-%d")}"
agent: "{agent}"
tags: {tags_str}
status: "active"
---
"""
            full_content = frontmatter + lore + "\n\n" + navigator
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(full_content)
            fixed_count += 1

print(f"Total files aggressively enriched with massive lore: {fixed_count}")
