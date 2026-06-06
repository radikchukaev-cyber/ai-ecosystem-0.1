import os

system_dir = r"D:\.antigravity\AI-ИМПЕРИИ3\wiki\entities\System"
scripts_dir = os.path.join(system_dir, "Scripts")
tools_dir = os.path.join(system_dir, "Tools")
skills_dir = os.path.join(tools_dir, "Skills")

def get_files(directory, ext=None):
    found = []
    if not os.path.exists(directory): return found
    for root, dirs, files in os.walk(directory):
        for file in files:
            if ext and not file.endswith(ext): continue
            if file.endswith("_INDEX.md") or file.endswith("Scripts.md") or file.endswith("Skills.md"): continue
            rel_path = os.path.relpath(os.path.join(root, file), r"D:\.antigravity\AI-ИМПЕРИИ3").replace("\\", "/")
            found.append(f"[[{rel_path}]]")
    return found

def get_folders(directory):
    found = []
    if not os.path.exists(directory): return found
    for item in os.listdir(directory):
        p = os.path.join(directory, item)
        if os.path.isdir(p):
            rel_path = os.path.relpath(p, r"D:\.antigravity\AI-ИМПЕРИИ3").replace("\\", "/")
            found.append(f"[[{rel_path}/]]")
    return found

scripts_files = get_files(scripts_dir, ".py")
skills_folders = get_folders(skills_dir)
tools_files = get_files(tools_dir, ".py")

# Rewrite SKILLS_INDEX.md
skills_index_path = os.path.join(skills_dir, "SKILLS_INDEX.md")
with open(skills_index_path, "w", encoding="utf-8") as f:
    f.write("# AI Skills & Tools - Master Index\n\n")
    f.write("> [!TIP]\n> **СВОДНЫЙ КАТАЛОГ ВСЕХ НАВЫКОВ И СКРИПТОВ СИСТЕМЫ**\n> Эти скрипты — это физическое оружие наших агентов.\n\n")
    
    f.write("## 1. Автономные Python Скрипты (Папка Scripts/)\n")
    for script in sorted(scripts_files):
        f.write(f"- {script}\n")
        
    f.write("\n## 2. Интеграции и Системные Навыки (Папка Skills/)\n")
    for skill in sorted(skills_folders):
        f.write(f"- {skill}\n")
        
    f.write("\n## 3. Системные Инструменты (Папка Tools/)\n")
    for tool in sorted(tools_files):
        f.write(f"- {tool}\n")
        
    f.write("\n***\n**Отметки:** [[wiki/entities/System/SYSTEM_INDEX.md|#system-skills]]\n")

# Rewrite TOOLS_INDEX.md
tools_index_path = os.path.join(tools_dir, "TOOLS_INDEX.md")
with open(tools_index_path, "w", encoding="utf-8") as f:
    f.write("# Системные Инструменты\n\n")
    f.write("Здесь хранятся утилиты для внутренней работы системы. Полный список всех скриптов и навыков собран в едином индексе:\n\n")
    f.write("➡️ **[[wiki/entities/System/Tools/Skills/SKILLS_INDEX.md|ПЕРЕЙТИ К ПОЛНОМУ КАТАЛОГУ СКИЛЛОВ]]**\n")
