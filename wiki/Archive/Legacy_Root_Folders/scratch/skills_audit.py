import os
import re

lore_dir = r"D:\.antigravity\AI-ИМПЕРИИ3\AI-ИМПЕРИИ"
skills_dir = r"D:\.antigravity\AI-ИМПЕРИИ3\wiki\entities\System\Tools\Skills"
output_file = r"D:\.antigravity\AI-ИМПЕРИИ3\scratch\skills_audit.md"

lore_files = [
    "6.ПОЛНАЯ СИСТЕМА СКИЛЛОВ (SKILLS).1.TXT",
    "7.ПОЛНАЯ СИСТЕМА СКИЛЛОВ (SKILLS).2.TXT",
    "8.ПОЛНАЯ СИСТЕМА СКИЛЛОВ (SKILLS).3.TXT",
    "9.ПОЛНАЯ СИСТЕМА СКИЛЛОВ (SKILLS).4.TXT"
]

all_lore_skills = []

for lf in lore_files:
    filepath = os.path.join(lore_dir, lf)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # The lore has titles like: title: "🎼 СКИЛЛ: Оркестрация (Распределение задач)"
            # Or headings like 🧠 СКИЛЛЫ RAMS
            # Let's extract agent blocks and title lines
            current_agent = "UNKNOWN"
            for line in content.split('\n'):
                if 'СКИЛЛЫ' in line and any(agent in line for agent in ['RAMS', 'VULCAN', 'ARGUS', 'MNEMOSYNE', 'SOCRATES', 'CASPER']):
                    for agent in ['RAMS', 'VULCAN', 'ARGUS', 'MNEMOSYNE', 'SOCRATES', 'CASPER']:
                        if agent in line:
                            current_agent = agent
                elif line.startswith('title:'):
                    title = line.replace('title:', '').strip().strip('"').strip("'")
                    all_lore_skills.append({"agent": current_agent, "title": title})

# Find existing files
existing_files = []
for root, dirs, files in os.walk(skills_dir):
    for f in files:
        if f.endswith('.md') and f != "SKILLS_INDEX.md":
            existing_files.append(f)

with open(output_file, 'w', encoding='utf-8') as out:
    out.write("# Аудит Скиллов\n\n")
    out.write("## Найдено в лоре:\n")
    for s in all_lore_skills:
        out.write(f"- [{s['agent']}] {s['title']}\n")
    
    out.write("\n## Существующие файлы в директории:\n")
    for e in existing_files:
        out.write(f"- {e}\n")
