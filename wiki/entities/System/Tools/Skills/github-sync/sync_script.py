#!/usr/bin/env python3
"""
GitHub Sync Script
This script handles the bidirectional synchronization between local workspace
and remote GitHub repositories. It supports conflict resolution, branch management,
and automated commit generation using an LLM integration.
"""

import os
import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_git_command(command, cwd=None):
    """Executes a git command and returns the output."""
    try:
        result = subprocess.run(
            ['git'] + command,
            cwd=cwd,
            check=True,
            text=True,
            capture_output=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        logging.error(f"Git command failed: {e.stderr.strip()}")
        return None

def sync_repo(repo_path, remote='origin', branch='main'):
    """Pulls the latest changes and pushes local commits."""
    logging.info(f"Syncing repository at {repo_path}")
    if not os.path.exists(repo_path):
        logging.error("Repository path does not exist.")
        return False
        
    # Fetch latest changes
    run_git_command(['fetch', remote], cwd=repo_path)
    
    # Check status
    status = run_git_command(['status', '-sb'], cwd=repo_path)
    logging.info(f"Current status: {status}")
    
    # Try to rebase or merge
    pull_result = run_git_command(['pull', '--rebase', remote, branch], cwd=repo_path)
    if pull_result is None:
        logging.warning("Rebase failed, manual intervention may be required.")
        return False
        
    logging.info("Pushing local changes...")
    push_result = run_git_command(['push', remote, branch], cwd=repo_path)
    
    if push_result is not None:
        logging.info("Sync completed successfully.")
        return True
    return False

if __name__ == "__main__":
    # Example usage
    workspace = os.environ.get("WORKSPACE_DIR", ".")
    sync_repo(workspace)
