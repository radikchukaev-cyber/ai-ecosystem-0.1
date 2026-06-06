import os
import json
import uuid

# Paths
LORE_FILE = r"D:\.antigravity\AI-ИМПЕРИИ3\scratch\canvas_extracted_lore.md"
CANVAS_DIR = r"D:\.antigravity\AI-ИМПЕРИИ3\wiki\synthesis\Canvases"

def read_lore():
    with open(LORE_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by "## " to get blocks
    blocks = []
    parts = content.split("\n## ")
    
    # The first part might be just the title "# Извлеченные сырые тексты..."
    if parts[0].strip():
        blocks.append(parts[0].strip())
        
    for part in parts[1:]:
        blocks.append("## " + part.strip())
    
    return blocks

def generate_nodes(blocks):
    nodes = []
    x_pos = 0
    y_pos = 0
    
    colors = ["1", "2", "3", "4", "5", "6"]
    
    for i, block in enumerate(blocks):
        node = {
            "id": uuid.uuid4().hex[:16],
            "type": "text",
            "text": block,
            "x": x_pos,
            "y": y_pos,
            "width": 600,
            "height": 500,
            "color": colors[i % len(colors)]
        }
        nodes.append(node)
        x_pos += 650 # space them out horizontally
    return nodes

def process_canvases():
    blocks = read_lore()
    
    count = 0
    for filename in os.listdir(CANVAS_DIR):
        if filename.endswith(".canvas"):
            filepath = os.path.join(CANVAS_DIR, filename)
            
            # Create a clean canvas with lore blocks
            new_canvas = {
                "nodes": generate_nodes(blocks),
                "edges": []
            }
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(new_canvas, f, ensure_ascii=False, indent=2)
            
            print(f"Cleaned and updated: {filename}")
            count += 1
            
    print(f"Successfully processed {count} files.")

if __name__ == "__main__":
    process_canvases()
