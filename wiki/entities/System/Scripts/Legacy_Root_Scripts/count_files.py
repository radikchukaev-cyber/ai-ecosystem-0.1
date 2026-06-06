import os
import glob

vault_dir = r"D:\.antigravity\AI-ИМПЕРИИ3"
md_files = glob.glob(os.path.join(vault_dir, "**", "*.md"), recursive=True)

valid_files = []
for f in md_files:
    if "Archive" in f or "node_modules" in f or ".git" in f:
        continue
    valid_files.append(f)

print(f"Total Markdown files to process: {len(valid_files)}")
