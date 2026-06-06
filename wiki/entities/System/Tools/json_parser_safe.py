import json
import ast
import re

def safe_parse_json(text):
    """Safely parse JSON that might have trailing commas or missing quotes."""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    
    try:
        # Try evaluating as python dict literal
        return ast.literal_eval(text)
    except (ValueError, SyntaxError):
        pass
        
    # Attempt simple regex fixes
    text_fixed = re.sub(r',\s*}', '}', text)
    text_fixed = re.sub(r',\s*]', ']', text_fixed)
    
    try:
        return json.loads(text_fixed)
    except json.JSONDecodeError as e:
        raise ValueError(f"Could not parse json safely: {e}")

if __name__ == "__main__":
    test_str = "{'key': 'value', 'bad': 1, }"
    print("Parsed:", safe_parse_json(test_str))
