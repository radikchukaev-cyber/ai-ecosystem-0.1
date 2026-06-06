import os

rams_dir = r"D:\.antigravity\AI-ИМПЕРИИ3\RAMS.Awakening"
vulcan_dir = r"D:\.antigravity\AI-ИМПЕРИИ3\RAMS.Awakening\General Cabinet.RAMS\RAMS.AGENTS.md\18.Vulcan.Awakening"

# Function to replace text in files
def replace_in_files(directory, old_text, new_text, skip_dir=None):
    for root, dirs, files in os.walk(directory):
        if skip_dir and skip_dir in root:
            continue
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                if old_text in content:
                    content = content.replace(old_text, new_text)
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(content)

old_rams_mark = "**🛡️ Пробуждение:** [[RAMS.Awakening/1.RAMS.Awakening.md|Начало Цикла]]"
new_rams_mark = "**🛡️ ПРОБУЖДЕНИЕ ОРКЕСТРАТОРА (RAMS):** [[RAMS.Awakening/1.RAMS.Awakening.md|Начало Цикла]]"

old_vulcan_mark = "**🛡️ Пробуждение:** [[18.Vulcan.Awakening/1.Vulcan.Awakening.md|Начало Цикла]]"
new_vulcan_mark = "**🛡️ ПРОБУЖДЕНИЕ АГЕНТА ВУЛКАН:** [[18.Vulcan.Awakening/1.Vulcan.Awakening.md|Начало Цикла]]"

replace_in_files(rams_dir, old_rams_mark, new_rams_mark, skip_dir="General Cabinet.RAMS")
replace_in_files(vulcan_dir, old_vulcan_mark, new_vulcan_mark)
