import os
import shutil
import glob

root_dir = r"D:\.antigravity\AI-ИМПЕРИИ3"

whitelist = [
    "RAMS.Awakening",
    "wiki",
    "AI-ИМПЕРИИ",
    ".git",
    ".obsidian",
    ".gitignore",
    "scratch" # Wait, I shouldn't move scratch because the MCP server uses it for scratch files. Ah, the prompt says "scratch" is part of the system generated artifacts but wait, MCP uses `<appDataDir>\brain\<conversation-id>/scratch/`. The root `scratch/` is mine, I created it! Yes, I should keep it or move it? Let's move it to wiki/Archive, wait, no, if I move `scratch/` any script inside `scratch/` will stop working, but that's fine. Wait, I will just keep `scratch/` as it's a temp folder. Actually, user wants it clean. I will move it.
]

# Create target directories
scripts_target = os.path.join(root_dir, "wiki", "entities", "System", "Scripts", "Legacy_Root_Scripts")
folders_target = os.path.join(root_dir, "wiki", "Archive", "Legacy_Root_Folders")
files_target = os.path.join(root_dir, "wiki", "Archive", "Legacy_Root_Files")

os.makedirs(scripts_target, exist_ok=True)
os.makedirs(folders_target, exist_ok=True)
os.makedirs(files_target, exist_ok=True)

for item in os.listdir(root_dir):
    if item in whitelist:
        continue
    
    item_path = os.path.join(root_dir, item)
    
    try:
        if os.path.isdir(item_path):
            print(f"Moving folder: {item} -> {folders_target}")
            shutil.move(item_path, os.path.join(folders_target, item))
        elif os.path.isfile(item_path):
            if item.endswith(".py") or item.endswith(".bat"):
                print(f"Moving script: {item} -> {scripts_target}")
                shutil.move(item_path, os.path.join(scripts_target, item))
            else:
                print(f"Moving file: {item} -> {files_target}")
                shutil.move(item_path, os.path.join(files_target, item))
    except Exception as e:
        print(f"Failed to move {item}: {e}")

print("Cleanup complete.")
