import re
import logging
from collections import Counter
from pathlib import Path
from typing import Dict, List

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class LogAnalyzer:
    """Analyzes system logs for errors and warnings."""
    def __init__(self, log_dir: str):
        self.log_dir = Path(log_dir)
        self.error_pattern = re.compile(r'(?i)(error|exception|fail|fatal)')

    def analyze(self) -> Dict[str, int]:
        """Analyzes logs and returns a summary of errors."""
        summary = Counter()
        
        if not self.log_dir.exists():
            logger.warning(f"Log directory {self.log_dir} not found.")
            return dict(summary)

        for log_file in self.log_dir.rglob('*.log'):
            try:
                with open(log_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        if self.error_pattern.search(line):
                            summary['total_errors'] += 1
                            if 'exception' in line.lower():
                                summary['exceptions'] += 1
            except Exception as e:
                logger.error(f"Error reading {log_file}: {e}")

        logger.info(f"Analysis complete: {dict(summary)}")
        return dict(summary)

if __name__ == "__main__":
    analyzer = LogAnalyzer("./logs")
    analyzer.analyze()
