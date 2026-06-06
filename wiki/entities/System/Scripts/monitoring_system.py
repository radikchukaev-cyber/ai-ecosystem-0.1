import time
import logging
from threading import Thread
from typing import Callable, List

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MonitoringSystem:
    """A simple threaded monitoring system that runs periodic checks."""
    def __init__(self, interval_seconds: int = 60):
        self.interval = interval_seconds
        self.tasks: List[Callable] = []
        self._running = False
        self._thread = None

    def add_task(self, task_func: Callable):
        self.tasks.append(task_func)

    def start(self):
        if self._running:
            return
        self._running = True
        self._thread = Thread(target=self._run_loop, daemon=True)
        self._thread.start()
        logger.info(f"Monitoring started with {self.interval}s interval.")

    def stop(self):
        self._running = False
        if self._thread:
            self._thread.join(timeout=5)
        logger.info("Monitoring stopped.")

    def _run_loop(self):
        while self._running:
            for task in self.tasks:
                try:
                    task()
                except Exception as e:
                    logger.error(f"Error in monitoring task {task.__name__}: {e}")
            time.sleep(self.interval)

if __name__ == "__main__":
    def sample_check():
        logger.info("Performing routine system check...")

    monitor = MonitoringSystem(interval_seconds=5)
    monitor.add_task(sample_check)
    monitor.start()
    time.sleep(15)
    monitor.stop()
