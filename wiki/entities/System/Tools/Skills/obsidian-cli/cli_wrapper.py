#!/usr/bin/env python3
"""
Obsidian CLI Wrapper
Provides a programmable interface to interact with Obsidian vaults.
Allows creating, reading, updating, and querying markdown notes and their metadata.
"""

import os
import re
import json

class ObsidianVault:
    def __init__(self, vault_path):
        self.vault_path = vault_path
        if not os.path.exists(self.vault_path):
            raise FileNotFoundError(f"Vault not found at {self.vault_path}")

    def create_note(self, title, content="", folder="", tags=None):
        """Creates a new note with optional frontmatter."""
        if tags is None:
            tags = []
            
        file_path = os.path.join(self.vault_path, folder, f"{title}.md")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        frontmatter = "---\n"
        if tags:
            frontmatter += f"tags: {json.dumps(tags)}\n"
        frontmatter += "---\n\n"
        
        full_content = frontmatter + content
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(full_content)
        return file_path

    def get_links(self, note_path):
        """Extracts wikilinks from a note."""
        if not os.path.exists(note_path):
            return []
            
        with open(note_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Match [[Link]] or [[Link|Alias]]
        pattern = r'\[\[(.*?)\]\]'
        links = re.findall(pattern, content)
        return [link.split('|')[0] for link in links]

if __name__ == "__main__":
    # Simple test
    vault_dir = os.environ.get("OBSIDIAN_VAULT", ".")
    try:
        vault = ObsidianVault(vault_dir)
        print(f"Initialized vault wrapper for {vault_dir}")
    except Exception as e:
        print(f"Error: {e}")
