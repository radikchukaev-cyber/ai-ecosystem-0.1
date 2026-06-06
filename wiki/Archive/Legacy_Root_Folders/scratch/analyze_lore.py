import os
import re

lore_dir = r"D:\.antigravity\AI-ИМПЕРИИ3\AI-ИМПЕРИИ"
wiki_dir = r"D:\.antigravity\AI-ИМПЕРИИ3\wiki"
rams_dir = r"D:\.antigravity\AI-ИМПЕРИИ3\RAMS.Awakening"

def extract_headings(filepath):
    headings = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if re.match(r'^(#+ |[0-9]+\.|- \*\*)', line):
                    headings.append(line)
    except Exception as e:
        pass
    return headings

lore_files = [
    "1.КОНСТИТУЦИЯ AI-ИМПЕРИИ.TXT",
    "4.ПОЛНАЯ КАРТА ЭКОСИСТЕМЫ(index).TXT",
    "10.ПОЛНЫЙ ПРОФИЛЬ КАЖДОГО АГЕНТА.TXT"
]

print("--- АНАЛИЗ ЛОРА (AI-ИМПЕРИИ) ---")
for lf in lore_files:
    print(f"\nИзвлечение структуры из {lf}:")
    headings = extract_headings(os.path.join(lore_dir, lf))
    # Print first 20 headings to get an idea
    for h in headings[:20]:
        print("  " + h[:80])

# Basic metric: check how many skills are implemented
skills_files = [
    "6.ПОЛНАЯ СИСТЕМА СКИЛЛОВ (SKILLS).1.TXT",
    "7.ПОЛНАЯ СИСТЕМА СКИЛЛОВ (SKILLS).2.TXT",
    "8.ПОЛНАЯ СИСТЕМА СКИЛЛОВ (SKILLS).3.TXT",
    "9.ПОЛНАЯ СИСТЕМА СКИЛЛОВ (SKILLS).4.TXT"
]
total_lore_skills = 0
for sf in skills_files:
    try:
        with open(os.path.join(lore_dir, sf), 'r', encoding='utf-8') as f:
            content = f.read()
            # Count occurrences of "Скилл:" or similar headers
            total_lore_skills += len(re.findall(r'(?i)Скилл\s*\d+|Skill\s*\d+', content))
            if total_lore_skills == 0:
                 # fallback, just count headings with numbers
                 total_lore_skills += len(re.findall(r'\n### \d+\.', content))
    except:
        pass

print(f"\n--- ПРЕДВАРИТЕЛЬНАЯ МЕТРИКА ---")
print(f"Примерное количество скиллов в Лоре: {total_lore_skills}")

# Count implemented skills in wiki
implemented_skills = 0
skills_dir = os.path.join(wiki_dir, "entities", "System", "Tools", "Skills")
if os.path.exists(skills_dir):
    for root, dirs, files in os.walk(skills_dir):
        for file in files:
            if file.endswith('.md') and file != "SKILLS_INDEX.md":
                implemented_skills += 1

print(f"Реализовано скиллов в системе (.md файлы): {implemented_skills}")
