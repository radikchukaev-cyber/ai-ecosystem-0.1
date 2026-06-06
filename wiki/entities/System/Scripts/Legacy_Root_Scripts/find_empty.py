import os

def find_empty_files(directory):
    empty_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            if os.path.getsize(path) == 0:
                empty_files.append(path)
    return empty_files

empty_files = find_empty_files(r'D:\.antigravity\AI-ИМПЕРИИ3\RAMS.Awakening\General Cabinet.RAMS')
with open(r'D:\.antigravity\AI-ИМПЕРИИ3\empty_files_list.txt', 'w', encoding='utf-8') as f:
    for ef in empty_files:
        f.write(ef + '\n')
