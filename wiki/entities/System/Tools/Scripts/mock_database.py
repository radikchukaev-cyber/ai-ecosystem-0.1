import sqlite3
import logging
from pathlib import Path
from typing import List, Tuple, Any

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MockDatabase:
    """An in-memory SQLite database for testing data operations."""
    
    def __init__(self, db_path: str = ":memory:"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self._initialize_schema()

    def _initialize_schema(self):
        """Sets up the initial tables."""
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                name TEXT NOT NULL,
                value REAL NOT NULL
            )
        """)
        self.conn.commit()
        logger.info("Mock database schema initialized.")

    def insert_metric(self, name: str, value: float) -> int:
        """Inserts a new metric and returns its ID."""
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO metrics (name, value) VALUES (?, ?)", (name, value))
        self.conn.commit()
        logger.info(f"Inserted metric: {name}={value}")
        return cursor.lastrowid

    def get_metrics(self, limit: int = 10) -> List[Tuple[Any, ...]]:
        """Retrieves recent metrics."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM metrics ORDER BY timestamp DESC LIMIT ?", (limit,))
        return cursor.fetchall()

    def close(self):
        self.conn.close()
        logger.info("Database connection closed.")

if __name__ == "__main__":
    db = MockDatabase()
    db.insert_metric("cpu_usage", 45.2)
    db.insert_metric("memory_usage", 60.1)
    
    for row in db.get_metrics():
        print(row)
        
    db.close()
