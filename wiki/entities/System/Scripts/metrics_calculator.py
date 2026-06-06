import math
import logging
from typing import List, Dict

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MetricsCalculator:
    """Calculates various statistical metrics from data arrays."""
    
    @staticmethod
    def calculate_mean(data: List[float]) -> float:
        if not data:
            return 0.0
        return sum(data) / len(data)

    @staticmethod
    def calculate_variance(data: List[float], sample: bool = True) -> float:
        if not data or len(data) < 2:
            return 0.0
        mean = MetricsCalculator.calculate_mean(data)
        variance_sum = sum((x - mean) ** 2 for x in data)
        return variance_sum / (len(data) - (1 if sample else 0))

    @staticmethod
    def calculate_std_dev(data: List[float], sample: bool = True) -> float:
        return math.sqrt(MetricsCalculator.calculate_variance(data, sample))

    @classmethod
    def get_summary(cls, data: List[float]) -> Dict[str, float]:
        """Returns a comprehensive statistical summary."""
        if not data:
            return {}
        
        return {
            "count": len(data),
            "min": min(data),
            "max": max(data),
            "mean": cls.calculate_mean(data),
            "std_dev": cls.calculate_std_dev(data)
        }

if __name__ == "__main__":
    sample_data = [10.5, 12.0, 11.2, 13.5, 9.8, 10.1]
    logger.info(f"Metrics Summary: {MetricsCalculator.get_summary(sample_data)}")
