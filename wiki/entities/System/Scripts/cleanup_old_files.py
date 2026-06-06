import os
import time
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class FileCleaner:
    """Cleans up old files based on retention policy."""
    def __init__(self, target_dir: str, max_age_days: int = 30):
        self.target_dir = Path(target_dir)
        self.max_age_seconds = max_age_days * 86400

    def cleanup(self) -> int:
        """Deletes files older than max_age_days. Returns number of deleted files."""
        if not self.target_dir.exists():
            logger.warning(f"Target directory {self.target_dir} not found.")
            return 0

        current_time = time.time()
        deleted_count = 0

        for file_path in self.target_dir.rglob('*'):
            if file_path.is_file():
                file_age = current_time - file_path.stat().st_mtime
                if file_age > self.max_age_seconds:
                    try:
                        file_path.unlink()
                        logger.info(f"Deleted old file: {file_path}")
                        deleted_count += 1
                    except Exception as e:
                        logger.error(f"Failed to delete {file_path}: {e}")

        logger.info(f"Cleanup completed. Deleted {deleted_count} files.")
        return deleted_count

if __name__ == "__main__":
    cleaner = FileCleaner("./logs", max_age_days=7)
    cleaner.cleanup()
