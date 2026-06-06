import os
import re

vault_dir = r"D:\.antigravity\AI-ИМПЕРИИ3"
map_file = os.path.join(vault_dir, "user_map.md")

with open(map_file, "r", encoding="utf-8") as f:
    text = f.read()

links = re.findall(r'\[\[(.*?)\]\]', text)
missing = []
found = []

for link in links:
    link = link.strip()
    if "|" in link:
        link = link.split("|")[0]
        
    if link == "":
        continue
        
    is_dir = link.endswith("/")
    
    # Try exact match relative to vault
    exact_path = os.path.join(vault_dir, link.replace("/", os.sep))
    if os.path.exists(exact_path):
        found.append(link)
        continue
        
    # Try appending .md if not dir and doesn't have extension
    if not is_dir and "." not in os.path.basename(link):
        md_path = exact_path + ".md"
        if os.path.exists(md_path):
            found.append(link)
            continue
            
    # If the link doesn't have a path, just a filename, search for it
    if "/" not in link:
        filename = link + (".md" if not is_dir and "." not in link else "")
        file_found = False
        for root, dirs, files in os.walk(vault_dir):
            if is_dir:
                if link.strip("/") in dirs:
                    file_found = True
                    break
            else:
                if filename in files:
                    file_found = True
                    break
        if file_found:
            found.append(link)
            continue
            
    missing.append(link)

print(f"Total links: {len(links)}")
print(f"Found: {len(found)}")
print(f"Missing: {len(missing)}")

print("\n--- MISSING LINKS ---")
for m in sorted(list(set(missing))):
    print("- " + m)
