import psutil
import logging
import platform

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SystemHealth:
    """Monitors system resource utilization."""
    
    @staticmethod
    def get_cpu_usage() -> float:
        return psutil.cpu_percent(interval=1)

    @staticmethod
    def get_memory_usage() -> float:
        mem = psutil.virtual_memory()
        return mem.percent

    @staticmethod
    def get_disk_usage(path: str = "/") -> float:
        try:
            disk = psutil.disk_usage(path)
            return disk.percent
        except Exception as e:
            logger.error(f"Could not get disk usage for {path}: {e}")
            return 0.0

    @classmethod
    def run_diagnostics(cls):
        """Runs full system diagnostics and logs the results."""
        logger.info(f"System: {platform.system()} {platform.release()}")
        logger.info(f"CPU Usage: {cls.get_cpu_usage()}%")
        logger.info(f"Memory Usage: {cls.get_memory_usage()}%")
        
        disk_path = "C:\\" if platform.system() == "Windows" else "/"
        logger.info(f"Disk Usage ({disk_path}): {cls.get_disk_usage(disk_path)}%")

if __name__ == "__main__":
    SystemHealth.run_diagnostics()
