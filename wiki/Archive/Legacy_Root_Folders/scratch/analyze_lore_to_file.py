import os
import re

lore_dir = r"D:\.antigravity\AI-ИМПЕРИИ3\AI-ИМПЕРИИ"
wiki_dir = r"D:\.antigravity\AI-ИМПЕРИИ3\wiki"
output_file = r"D:\.antigravity\AI-ИМПЕРИИ3\scratch\lore_analysis_results.md"

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

with open(output_file, "w", encoding="utf-8") as out:
    out.write("# АНАЛИЗ ЛОРА (AI-ИМПЕРИИ)\n\n")
    for lf in lore_files:
        out.write(f"## Извлечение структуры из {lf}:\n")
        headings = extract_headings(os.path.join(lore_dir, lf))
        for h in headings[:20]:
            out.write(f"- {h[:100]}\n")
        out.write("\n")

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
                matches = re.findall(r'(?i)Скилл\s*\d+', content)
                if not matches:
                     matches = re.findall(r'\n### \d+\.', content)
                total_lore_skills += len(matches)
        except:
            pass

    out.write(f"## Скиллы в Лоре\nПримерное количество скиллов в лоре: {total_lore_skills}\n")

    implemented_skills = 0
    skills_dir = os.path.join(wiki_dir, "entities", "System", "Tools", "Skills")
    if os.path.exists(skills_dir):
        for root, dirs, files in os.walk(skills_dir):
            for file in files:
                if file.endswith('.md') and file != "SKILLS_INDEX.md":
                    implemented_skills += 1

    out.write(f"Реализовано скиллов в системе (.md файлы): {implemented_skills}\n")
    
    if total_lore_skills > 0:
        pct = (implemented_skills / total_lore_skills) * 100
        out.write(f"Процент внедрения скиллов: {pct:.1f}%\n")
