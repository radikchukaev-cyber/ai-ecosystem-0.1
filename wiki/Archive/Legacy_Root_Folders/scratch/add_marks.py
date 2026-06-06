import os

rams_dir = r"D:\.antigravity\AI-ИМПЕРИИ3\RAMS.Awakening"
vulcan_dir = r"D:\.antigravity\AI-ИМПЕРИИ3\RAMS.Awakening\General Cabinet.RAMS\RAMS.AGENTS.md\18.Vulcan.Awakening"
vulcan_cabinet_dir = os.path.join(vulcan_dir, "Cabinet.Vulcan")

# 1. Fix 2.SOUL.md for RAMS specifically
soul_file = os.path.join(rams_dir, "2.SOUL.md")
if os.path.exists(soul_file):
    with open(soul_file, "r", encoding="utf-8") as f:
        content = f.read()
    if "➡️ **Следующий этап:**" not in content:
        content += "\n\n➡️ **Следующий этап:** [[RAMS.Awakening/3.HEARTBEAT.md|Пульс Бизнеса]]\n"
        with open(soul_file, "w", encoding="utf-8") as f:
            f.write(content)

# 2. Add RAMS Awakening mark
rams_mark = "\n\n***\n**🛡️ Пробуждение:** [[RAMS.Awakening/1.RAMS.Awakening.md|Начало Цикла]]\n"
for root, dirs, files in os.walk(rams_dir):
    if "General Cabinet.RAMS" in root:
        continue # Skip subagents for now
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            if "🛡️ Пробуждение" not in content:
                with open(filepath, "a", encoding="utf-8") as f:
                    f.write(rams_mark)

# 3. Add Vulcan Awakening mark
vulcan_mark = "\n\n***\n**🛡️ Пробуждение:** [[18.Vulcan.Awakening/1.Vulcan.Awakening.md|Начало Цикла]]\n"
for root, dirs, files in os.walk(vulcan_dir):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            if "🛡️ Пробуждение" not in content:
                with open(filepath, "a", encoding="utf-8") as f:
                    f.write(vulcan_mark)
