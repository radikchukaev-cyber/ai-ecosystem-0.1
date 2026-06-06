import subprocess
import logging
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class GitHubSyncer:
    """Synchronizes local repository with GitHub."""
    def __init__(self, repo_dir: str, branch: str = "main"):
        self.repo_dir = Path(repo_dir)
        self.branch = branch

    def run_command(self, cmd: list) -> bool:
        try:
            result = subprocess.run(
                cmd, 
                cwd=self.repo_dir, 
                check=True, 
                capture_output=True, 
                text=True
            )
            logger.info(result.stdout.strip())
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"Command {' '.join(cmd)} failed: {e.stderr.strip()}")
            return False

    def sync(self) -> bool:
        """Pulls latest changes, commits local changes, and pushes to GitHub."""
        if not (self.repo_dir / ".git").exists():
            logger.error(f"{self.repo_dir} is not a valid git repository.")
            return False

        logger.info(f"Starting sync for branch {self.branch} in {self.repo_dir}")
        
        # Pull latest
        if not self.run_command(["git", "pull", "origin", self.branch]):
            return False

        # Add all changes
        if not self.run_command(["git", "add", "."]):
            return False

        # Check if there are changes to commit
        status = subprocess.run(["git", "status", "--porcelain"], cwd=self.repo_dir, capture_output=True, text=True)
        if not status.stdout.strip():
            logger.info("No changes to commit. Sync complete.")
            return True

        # Commit
        commit_msg = "Auto-sync changes"
        if not self.run_command(["git", "commit", "-m", commit_msg]):
            return False

        # Push
        if not self.run_command(["git", "push", "origin", self.branch]):
            return False

        logger.info("Sync completed successfully.")
        return True

if __name__ == "__main__":
    syncer = GitHubSyncer(".")
    syncer.sync()
