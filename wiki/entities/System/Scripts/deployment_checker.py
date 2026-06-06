import sys
import logging
import requests
from typing import List, Dict

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DeploymentChecker:
    """Verifies deployment status and endpoint health."""
    def __init__(self, endpoints: List[Dict[str, str]]):
        self.endpoints = endpoints

    def check_all(self) -> bool:
        """Checks all configured endpoints. Returns True if all are healthy."""
        all_healthy = True
        
        for endpoint in self.endpoints:
            url = endpoint.get('url')
            expected_status = endpoint.get('expected_status', 200)
            
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == expected_status:
                    logger.info(f"SUCCESS: {url} returned {response.status_code}")
                else:
                    logger.error(f"FAILURE: {url} returned {response.status_code}, expected {expected_status}")
                    all_healthy = False
            except requests.RequestException as e:
                logger.error(f"ERROR: Failed to connect to {url}: {e}")
                all_healthy = False

        return all_healthy

if __name__ == "__main__":
    test_endpoints = [
        {"url": "http://localhost:8080/health", "expected_status": 200},
        {"url": "http://localhost:8080/api/v1/status", "expected_status": 200}
    ]
    checker = DeploymentChecker(test_endpoints)
    success = checker.check_all()
    sys.exit(0 if success else 1)
