import shutil
import logging
from pathlib import Path
from typing import Optional

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class RollbackManager:
    """Automates rolling back to a previous backup version."""
    def __init__(self, target_dir: str, backup_dir: str):
        self.target_dir = Path(target_dir)
        self.backup_dir = Path(backup_dir)

    def find_latest_backup(self) -> Optional[Path]:
        """Finds the most recent backup directory."""
        if not self.backup_dir.exists():
            return None
            
        backups = [d for d in self.backup_dir.iterdir() if d.is_dir() and d.name.startswith("backup_")]
        if not backups:
            return None
            
        # Sort by name assuming timestamp format backup_YYYYMMDD_HHMMSS
        return sorted(backups, key=lambda x: x.name)[-1]

    def execute_rollback(self) -> bool:
        """Restores the target directory from the latest backup."""
        latest_backup = self.find_latest_backup()
        if not latest_backup:
            logger.error("No valid backup found for rollback.")
            return False

        logger.info(f"Initiating rollback from {latest_backup} to {self.target_dir}")
        try:
            if self.target_dir.exists():
                logger.info(f"Removing current target directory: {self.target_dir}")
                shutil.rmtree(self.target_dir)
                
            shutil.copytree(latest_backup, self.target_dir)
            logger.info("Rollback completed successfully.")
            return True
        except Exception as e:
            logger.error(f"Rollback failed: {e}")
            return False

if __name__ == "__main__":
    manager = RollbackManager("./app_data", "./backups")
    manager.execute_rollback()
