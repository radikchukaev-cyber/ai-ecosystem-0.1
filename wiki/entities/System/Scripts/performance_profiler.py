import time
import cProfile
import pstats
import io
import logging
from functools import wraps

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def profile_time(func):
    """Decorator to measure execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        logger.info(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

class PerformanceProfiler:
    """Profiles code blocks using cProfile."""
    def __init__(self):
        self.profiler = cProfile.Profile()

    def start(self):
        self.profiler.enable()

    def stop(self):
        self.profiler.disable()

    def get_stats(self, sort_by: str = 'cumulative') -> str:
        s = io.StringIO()
        ps = pstats.Stats(self.profiler, stream=s).sort_stats(sort_by)
        ps.print_stats()
        return s.getvalue()

if __name__ == "__main__":
    @profile_time
    def expensive_operation():
        return sum(i * i for i in range(1000000))

    profiler = PerformanceProfiler()
    profiler.start()
    expensive_operation()
    profiler.stop()
    print(profiler.get_stats())
