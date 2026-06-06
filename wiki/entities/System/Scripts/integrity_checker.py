import hashlib
import json
import logging
from pathlib import Path
from typing import Dict

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class IntegrityChecker:
    """Verifies file integrity using SHA-256 hashes."""
    def __init__(self, target_dir: str, hash_file: str = "hashes.json"):
        self.target_dir = Path(target_dir)
        self.hash_file = Path(hash_file)

    def calculate_hash(self, file_path: Path) -> str:
        sha256_hash = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except Exception as e:
            logger.error(f"Error reading file {file_path}: {e}")
            return ""

    def generate_hashes(self):
        """Generates and saves hashes for all files in target_dir."""
        hashes: Dict[str, str] = {}
        if not self.target_dir.exists():
            logger.error("Target directory does not exist.")
            return

        for file_path in self.target_dir.rglob('*'):
            if file_path.is_file():
                rel_path = str(file_path.relative_to(self.target_dir))
                hashes[rel_path] = self.calculate_hash(file_path)

        with open(self.hash_file, 'w') as f:
            json.dump(hashes, f, indent=4)
        logger.info(f"Hashes saved to {self.hash_file}")

if __name__ == "__main__":
    checker = IntegrityChecker("./src")
    checker.generate_hashes()
