import os
import sys

def validate_structure(base_path, expected_dirs):
    """Validates if expected subdirectories exist in the given base path."""
    missing = []
    for d in expected_dirs:
        path = os.path.join(base_path, d)
        if not os.path.exists(path) or not os.path.isdir(path):
            missing.append(d)
            
    return missing

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python structure_validator.py <base_path>")
        sys.exit(1)
        
    expected = ["Agents", "System", "Projects"]
    missing = validate_structure(sys.argv[1], expected)
    if missing:
        print("Missing directories:", missing)
    else:
        print("Structure is valid.")
