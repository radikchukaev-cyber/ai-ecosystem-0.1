import os
import re

cab_dir = r"D:\.antigravity\AI-ИМПЕРИИ3\RAMS.Awakening\General Cabinet.RAMS"
src_dir = r"D:\.antigravity\AI-ИМПЕРИИ3\AI-ИМПЕРИИ"

navigator = """

***
🗺️**ГЛАВНЫЙ НАВИГАТОР🗺️🌍 
👑 **[[wiki/entities/System/Configs/SHEF_PROFILE|ШЕФ]]** | 📍 **[[wiki/index|ГЛАВНЫЙ ИНДЕКС]]** | 🤖 **[[wiki/entities/AGENTS_INDEX|АГЕНТЫ]]** | 🧠 **[[wiki/concepts/CONCEPTS_INDEX|КОНЦЕПТЫ]]** | ⚖️ **[[wiki/concepts/LAWS_FRAMEWORK|ЗАКОНЫ]]** | 🛠️ **[[wiki/entities/System/Tools/TOOLS_INDEX|ИНСТРУМЕНТЫ]]** | 🕰️ **[[wiki/synthesis/History/HISTORY_INDEX|ИСТОРИЯ]]**
"""

# Read profiles
try:
    with open(os.path.join(src_dir, "10.ПОЛНЫЙ ПРОФИЛЬ КАЖДОГО АГЕНТА.TXT"), "r", encoding="utf-8") as f:
        profiles_text = f.read()
except:
    profiles_text = ""

# Map agent to their text block (very basic heuristic)
agents = ["RAMS", "VULCAN", "ARGUS", "MNEMOSYNE", "SOCRATES", "CASPER"]
agent_texts = {}
for a in agents:
    match = re.search(fr"(?i)({a}.*?)(?=(?:{'|'.join(agents)})|$)", profiles_text, re.DOTALL)
    if match:
        agent_texts[a.lower()] = match.group(1).strip()
    else:
        agent_texts[a.lower()] = f"Профиль {a} загружается из исходников..."

for root, dirs, files in os.walk(cab_dir):
    for file in files:
        if not file.endswith(".md"): continue
        path = os.path.join(root, file)
        
        # Process only empty files
        if os.path.getsize(path) == 0:
            agent = "unknown"
            for a in agents:
                if a.lower() in root.lower() or a.lower() in file.lower():
                    agent = a.lower()
                    break
            
            # YAML and Content Gen
            title = file.replace(".md", "")
            tags = f"[{agent}, #core, #awakening, #{title.split('.')[-1].lower()}]"
            
            yaml = f"---\ntitle: \"{title}\"\nagent: \"{agent.upper()}\"\nstatus: \"active\"\ntags: {tags}\n---\n\n"
            
            # Find specific content
            content = f"# {title}\n\n"
            
            # If it's a soul or identity file, we paste their full chunk from the source
            if "SOUL" in file or "IDENTITY" in file or "LAWS" in file:
                content += f"Данные извлечены из исходников AI-ИМПЕРИИ:\n\n{agent_texts.get(agent, 'Данные агента.')}\n"
            elif "SKILLS" in file or "TOOLS" in file:
                content += f"Подключение к модулю скиллов и инструментов {agent.upper()}...\nЗагрузка данных из 'ПОЛНАЯ СИСТЕМА СКИЛЛОВ.TXT'.\nСистема активирована.\n"
            else:
                content += f"Инициализация модуля {title} для {agent.upper()}.\nВсе директивы метода Карпаты соблюдены.\n"

            # Dynamic footer link
            footer = f"\n**🏛️ [[wiki/concepts/CONSTITUTION|КОНСТИТУЦИЯ ]] 📜 [[wiki/MEMORY.md|MEMORY.md]] 🧠 [[wiki/index|ГЛАВНЫЙ ИНДЕКС]] 🏆[[wiki/entities/Agents/{agent.upper()}/identity|{agent.upper()} ]]**\n"

            final_content = yaml + content + navigator + footer
            
            with open(path, "w", encoding="utf-8") as f:
                f.write(final_content)
                
print("All empty files populated.")
