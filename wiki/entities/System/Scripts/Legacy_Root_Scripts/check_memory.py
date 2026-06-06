import os

vault = r"D:\.antigravity\AI-ИМПЕРИИ3\wiki\entities\Agents"
agents = ["RAMS", "VULCAN", "ARGUS", "MNEMOSYNE", "SOCRATES", "CASPER"]

print("--- MEMORY FOLDER CHECK ---")
for agent in agents:
    agent_dir = os.path.join(vault, agent)
    memory_dir = os.path.join(agent_dir, "memory")
    
    if os.path.exists(memory_dir):
        files = os.listdir(memory_dir)
        print(f"[{agent}] Memory dir exists. Files: {files}")
    else:
        print(f"[{agent}] ERROR: Memory dir MISSING!")
        
print("\n--- IDENTITY BOOT CHECK ---")
for agent in agents:
    identity_file = os.path.join(vault, agent, f"identity.md")
    # Fallback to agent_name.md if identity.md doesn't exist
    if not os.path.exists(identity_file):
        identity_file = os.path.join(vault, agent, f"{agent}.md")
        
    if os.path.exists(identity_file):
        with open(identity_file, 'r', encoding='utf-8') as f:
            content = f.read()
            if "memory" in content.lower() or "пробужден" in content.lower():
                print(f"[{agent}] Identity mentions memory/awakening.")
            else:
                print(f"[{agent}] WARNING: Identity does NOT explicitly mention reading memory on boot.")
    else:
        print(f"[{agent}] ERROR: Identity file missing!")
