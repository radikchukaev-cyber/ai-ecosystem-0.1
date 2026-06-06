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
    ".gitignore"
]

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
            shutil.move(item_path, os.path.join(folders_target, item))
        elif os.path.isfile(item_path):
            if item.endswith(".py") or item.endswith(".bat"):
                shutil.move(item_path, os.path.join(scripts_target, item))
            else:
                shutil.move(item_path, os.path.join(files_target, item))
    except Exception as e:
        pass
