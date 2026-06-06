import os
import time
import subprocess
import datetime
from pathlib import Path

# Paths
REPO_DIR = Path(r"D:\.antigravity\AI-ИМПЕРИИ3")
MEMORY_FILE = REPO_DIR / "wiki" / "MEMORY.md"

AGENTS = {
    "VULCAN": "Agents/VULCAN",
    "CASPER": "Agents/CASPER",
    "SOCRATES": "Agents/SOCRATES",
    "ARGUS": "Agents/ARGUS",
    "MNEMOSYNE": "Agents/MNEMOSYNE",
    "RAMS": "Agents/RAMS"
}

AGENT_WIKILINKS = {
    "VULCAN": "[[wiki/entities/Agents/VULCAN/VULCAN.md|#vulcan]]",
    "CASPER": "[[wiki/entities/Agents/CASPER/CASPER.md|#casper]]",
    "SOCRATES": "[[wiki/entities/Agents/SOCRATES/SOCRATES.md|#socrates]]",
    "ARGUS": "[[wiki/entities/Agents/ARGUS/ARGUS.md|#argus]]",
    "MNEMOSYNE": "[[wiki/entities/Agents/MNEMOSYNE/MNEMOSYNE.md|#mnemosyne]]",
    "RAMS": "[[wiki/entities/Agents/RAMS/RAMS.md|#rams]]",
    "SYSTEM": "[[wiki/index.md|#system]]"
}

def run_cmd(cmd):
    result = subprocess.run(cmd, cwd=REPO_DIR, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def process_memory():
    # Fetch and merge cloud changes FIRST
    print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}] Синхронизация с облаком (Pull)...")
    pull_output = run_cmd("git pull origin main --rebase")
    if pull_output:
        print(f"Pull result: {pull_output}")

    # Stage all local changes
    run_cmd("git add .")
    
    # Get staged files
    staged_output = run_cmd("git diff --cached --name-only")
    if not staged_output:
        return # Nothing to do

    files = staged_output.split('\n')
    
    # Filter out MEMORY.md if it's the only one
    if len(files) == 1 and files[0] == "wiki/MEMORY.md":
        run_cmd('git commit -m "MNEMOSYNE AUTO-LOG"')
        run_cmd('git push origin main')
        return

    changes_by_agent = {}
    tags_to_add = set(["MNEMOSYNE"])

    for f in files:
        f = f.replace("\\", "/")
        if "wiki/MEMORY.md" in f:
            continue
            
        owner = "SYSTEM"
        for agent, path_signature in AGENTS.items():
            if path_signature in f:
                owner = agent
                tags_to_add.add(agent)
                break
        
        if owner not in changes_by_agent:
            changes_by_agent[owner] = []
        changes_by_agent[owner].append(f)

    # Build log
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")
    
    log_lines = [f"\n**[{timestamp}] MNEMOSYNE AUTO-LOG (ФОНОВЫЙ ТРЕКЕР):**"]
    log_lines.append(f"- **Действие:** Автоматическое обнаружение изменений в файловой системе и сохранение в GitHub.")
    
    for owner, changed_files in changes_by_agent.items():
        if len(changed_files) <= 3:
            file_str = ", ".join(f"`{Path(x).name}`" for x in changed_files)
            log_lines.append(f"- **{owner}:** Изменены файлы: {file_str}")
        else:
            log_lines.append(f"- **{owner}:** Изменены файлы ({len(changed_files)} шт.).")

    tags_str = " ".join(AGENT_WIKILINKS[tag] for tag in sorted(tags_to_add))
    log_lines.append(f"- **Отметки:** {tags_str}")

    # Write to MEMORY.md
    with open(MEMORY_FILE, "a", encoding="utf-8") as f:
        f.write("\n".join(log_lines) + "\n")

    # Add MEMORY.md and commit
    run_cmd("git add wiki/MEMORY.md")
    run_cmd(f'git commit -m "MNEMOSYNE AUTO-LOG: {timestamp}"')
    run_cmd('git push origin main')
    print(f"[{timestamp}] Successfully synced to GitHub.")

if __name__ == "__main__":
    print("MNEMOSYNE DAEMON СТАРТОВАЛ. Ожидание изменений...")
    while True:
        try:
            process_memory()
        except Exception as e:
            print(f"Ошибка: {e}")
        time.sleep(1800) # 30 minutes
