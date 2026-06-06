import os
import shutil
import logging
from datetime import datetime
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class BackupManager:
    """Manages system backups."""
    def __init__(self, source_dir: str, backup_dir: str):
        self.source_dir = Path(source_dir)
        self.backup_dir = Path(backup_dir)
        self.backup_dir.mkdir(parents=True, exist_ok=True)

    def create_backup(self) -> bool:
        """Creates a timestamped backup of the source directory."""
        if not self.source_dir.exists():
            logger.error(f"Source directory {self.source_dir} does not exist.")
            return False
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = self.backup_dir / f"backup_{timestamp}"
        
        try:
            logger.info(f"Starting backup from {self.source_dir} to {backup_path}")
            shutil.copytree(self.source_dir, backup_path)
            logger.info("Backup completed successfully.")
            return True
        except Exception as e:
            logger.error(f"Backup failed: {e}")
            return False

if __name__ == "__main__":
    manager = BackupManager("./data", "./backups")
    manager.create_backup()
