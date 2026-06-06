import os
import sys

def search_memory(directory, keyword):
    """Searches memory files for specific keywords."""
    results = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md') or file.endswith('.txt'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        for i, line in enumerate(lines):
                            if keyword.lower() in line.lower():
                                results.append(f"{filepath}:{i+1}:{line.strip()}")
                except Exception as e:
                    pass
    return results

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python memory_search.py <directory> <keyword>")
        sys.exit(1)
    
    res = search_memory(sys.argv[1], sys.argv[2])
    for r in res:
        print(r)
