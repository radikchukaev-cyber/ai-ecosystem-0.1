import os
import markdown
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MarkdownConverter:
    """Converts markdown files to HTML."""
    def __init__(self, input_dir: str, output_dir: str):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def convert_all(self):
        """Converts all markdown files in input_dir to HTML."""
        if not self.input_dir.exists():
            logger.error(f"Input directory {self.input_dir} not found.")
            return

        for md_file in self.input_dir.rglob('*.md'):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    text = f.read()
                
                html = markdown.markdown(text, extensions=['extra', 'codehilite'])
                
                rel_path = md_file.relative_to(self.input_dir)
                out_file = self.output_dir / rel_path.with_suffix('.html')
                out_file.parent.mkdir(parents=True, exist_ok=True)
                
                with open(out_file, 'w', encoding='utf-8') as f:
                    f.write(html)
                logger.info(f"Converted {md_file} to {out_file}")
            except Exception as e:
                logger.error(f"Failed to convert {md_file}: {e}")

if __name__ == "__main__":
    converter = MarkdownConverter("./docs", "./build/html")
    converter.convert_all()
