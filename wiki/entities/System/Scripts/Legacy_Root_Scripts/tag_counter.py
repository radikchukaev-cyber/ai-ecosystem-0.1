import os
import re
from collections import Counter

vault_dir = r"D:\.antigravity\AI-ИМПЕРИИ3"
all_tags = []

for root, dirs, files in os.walk(vault_dir):
    if "Archive" in root or "node_modules" in root or ".git" in root:
        continue
    for file in files:
        if file.endswith(".md"):
            try:
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    match = re.search(r'^tags:\s*\[(.*?)\]', content, re.MULTILINE)
                    if match:
                        tags = match.group(1).split(",")
                        for t in tags:
                            tag = t.strip()
                            if tag:
                                all_tags.append(tag)
            except:
                pass

counter = Counter(all_tags)
print("TAG DISTRIBUTION:")
for tag, count in counter.most_common(20):
    print(f"{tag}: {count}")
