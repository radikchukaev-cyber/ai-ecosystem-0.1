import os
import hashlib
import sys

def get_file_hash(filepath, block_size=65536):
    hasher = hashlib.md5()
    try:
        with open(filepath, 'rb') as f:
            buf = f.read(block_size)
            while len(buf) > 0:
                hasher.update(buf)
                buf = f.read(block_size)
        return hasher.hexdigest()
    except Exception as e:
        return None

def find_duplicates(directory):
    hashes = {}
    duplicates = []
    
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            file_hash = get_file_hash(filepath)
            
            if file_hash:
                if file_hash in hashes:
                    duplicates.append((filepath, hashes[file_hash]))
                else:
                    hashes[file_hash] = filepath
                    
    return duplicates

if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    dupes = find_duplicates(target_dir)
    if dupes:
        print("Found duplicates:")
        for dup in dupes:
            print(f"{dup[0]} == {dup[1]}")
    else:
        print("No duplicates found.")
