import os
import glob
import re

targets = [
    r"D:\.antigravity\AI-ИМПЕРИИ3\RAMS.Awakening",
    r"D:\.antigravity\AI-ИМПЕРИИ3\wiki"
]

source_txt = r"D:\.antigravity\AI-ИМПЕРИИ3\AI-ИМПЕРИИ\1.КОНСТИТУЦИЯ AI-ИМПЕРИИ.TXT"

with open(source_txt, 'r', encoding='utf-8') as f:
    constitution = f.read()

# Extract the SHEF PROFILE
shef_match = re.search(r'(# shef\.md - About Your Human.*?)(?=---[\r\n]+# |$)', constitution, re.DOTALL | re.IGNORECASE)
shef_profile = shef_match.group(1).strip() if shef_match else "ERROR: SHEF PROFILE NOT FOUND IN CONSTITUTION"

navigator = """
***
🗺️**ГЛАВНЫЙ НАВИГАТОР🗺️🌍 
👑 **[[wiki/entities/System/Configs/SHEF_PROFILE|ШЕФ]]** | 📍 **[[wiki/index|ГЛАВНЫЙ ИНДЕКС]]** | 🤖 **[[wiki/entities/AGENTS_INDEX|АГЕНТЫ]]** | 🧠 **[[wiki/concepts/CONCEPTS_INDEX|КОНЦЕПТЫ]]** | ⚖️ **[[wiki/concepts/LAWS_FRAMEWORK|ЗАКОНЫ]]** | 🛠️ **[[wiki/entities/System/Tools/TOOLS_INDEX|ИНСТРУМЕНТЫ]]** | 🕰️ **[[wiki/synthesis/History/HISTORY_INDEX|ИСТОРИЯ]]**

**🏛️ [[wiki/concepts/CONSTITUTION|КОНСТИТУЦИЯ ]] 📜 [[wiki/MEMORY.md|MEMORY.md]] 🧠 [[wiki/index|ГЛАВНЫЙ ИНДЕКС]] 🏆[[wiki/entities/Agents/RAMS/identity|RAMS ]]**
"""

files_cleared = 0
placeholders_found = 0

for target in targets:
    for root, dirs, files in os.walk(target):
        for file in files:
            if not file.endswith('.md'): continue
            if file == "50_missing_items.md" or file == "task.md" or file == "implementation_plan.md" or file == "walkthrough.md": continue
            
            filepath = os.path.join(root, file)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # Erase tags array completely
                new_content = re.sub(r'^tags:\s*\[.*?\]', 'tags: []', content, flags=re.MULTILINE)
                
                if "7.USER.shef" in file or "SHEF_PROFILE" in file:
                    # FIX THE SHEF FILE COMPLETELY
                    frontmatter = f"""---
title: "{file.replace('.md', '')}"
agent: "RAMS"
tags: []
status: "active"
---
"""
                    new_content = frontmatter + "\n" + shef_profile + "\n\n" + navigator
                
                # Check if it's a placeholder
                is_placeholder = False
                if "Skill placeholder" in new_content or "status: \"pending\"" in new_content or "Модуль " in new_content and " активирован для" in new_content:
                    is_placeholder = True
                if "Агент MNEMOSYNE выполняет роль:" in new_content or "Агент VULCAN выполняет роль:" in new_content:
                    is_placeholder = True
                if "АЛЬФА И ОМЕГА" in new_content:
                    is_placeholder = True
                
                if is_placeholder:
                    placeholders_found += 1
                    
                # Write back the tag-erased content
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                files_cleared += 1
                    
            except Exception as e:
                pass

print(f"Tags erased in {files_cleared} files.")
print(f"Number of placeholder/generic files remaining: {placeholders_found}")
