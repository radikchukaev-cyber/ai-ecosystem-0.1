import os
import glob
import re

targets = [
    r"D:\.antigravity\AI-ИМПЕРИИ3\RAMS.Awakening",
    r"D:\.antigravity\AI-ИМПЕРИИ3\wiki"
]

correct_files = []
incorrect_files = []
empty_files = []

# Known "good" manual tags from previous run
good_patterns = [
    "#golden_rules", "#critical_directives", "#constitution", "#history", 
    "#failures", "#postmortems", "#archive_management", "#retention"
]

def check_tags(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        tags_match = re.search(r'^tags:\s*\[(.*?)\]', content, re.MULTILINE)
        if not tags_match:
            return "NO_TAGS"
            
        tags_inner = tags_match.group(1).strip()
        if not tags_inner:
            return "EMPTY_TAGS"
            
        tags_list = [t.strip() for t in tags_inner.split(',')]
        
        # Check if tags are just the generic script dump
        # e.g. [#active, #wiki/entities, #category/tools_index]
        has_good = False
        for g in good_patterns:
            if any(g in t for t in tags_list):
                has_good = True
                break
                
        # If the file has a specific skill tag like #skill/..., it might be decent
        # But let's check if it lacks deep specific tags.
        generic_count = 0
        for t in tags_list:
            if t in ["#active", "#wiki", "#wiki/entities", "#wiki/concepts", "#wiki/synthesis", "#daily_rhythm", "#protocol"]:
                generic_count += 1
                
        if has_good:
            return "CORRECT"
        elif len(tags_list) == generic_count:
            return "GENERIC_INCORRECT"
        elif any("#category/" in t for t in tags_list):
            return "GENERIC_INCORRECT"
        elif "TOOLS_INDEX" in filepath and not has_good:
            return "GENERIC_INCORRECT"
        else:
            # Let's consider most script-generated tags as incorrect if they don't have deep context
            return "GENERIC_INCORRECT"
            
    except Exception as e:
        return "ERROR"

for target in targets:
    for root, dirs, files in os.walk(target):
        for file in files:
            if not file.endswith('.md'): continue
            if file in ["50_missing_items.md", "task.md", "implementation_plan.md", "walkthrough.md"]: continue
            
            filepath = os.path.join(root, file)
            status = check_tags(filepath)
            
            rel_path = filepath.replace(r"D:\.antigravity\AI-ИМПЕРИИ3\\", "")
            
            if status == "CORRECT":
                correct_files.append(rel_path)
            elif status == "EMPTY_TAGS":
                empty_files.append(rel_path)
            else:
                incorrect_files.append(rel_path)

print(f"CORRECT: {len(correct_files)}")
print(f"INCORRECT: {len(incorrect_files)}")
print(f"EMPTY: {len(empty_files)}")

# Write table to a file for easy reading
with open("tag_analysis.md", "w", encoding="utf-8") as f:
    f.write("| Статус | Количество | Описание |\n")
    f.write("|---|---|---|\n")
    f.write(f"| ✅ Правильные ручные теги | {len(correct_files)} | Теги прописаны точечно (например, LAWS_FRAMEWORK) |\n")
    f.write(f"| ❌ Неправильные/Шаблонные | {len(incorrect_files)} | Автоматические пустышки (например, TOOLS_INDEX) |\n")
    f.write(f"| ⚠️ Пустые (tags: []) | {len(empty_files)} | Теги стерты, но не восстановлены |\n")
    f.write("\n## Примеры неправильных:\n")
    for file in incorrect_files[:10]:
        f.write(f"- {file}\n")
