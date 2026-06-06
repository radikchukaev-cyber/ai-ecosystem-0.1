import json
import logging
import time
from typing import Dict, Any, Optional

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MockAPI:
    """A simulated API for testing interactions without network requests."""
    
    def __init__(self):
        self.data_store: Dict[str, Any] = {
            "/users": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}],
            "/status": {"health": "ok", "uptime": 99.9},
            "/config": {"theme": "dark", "notifications": True}
        }
        self.latency_ms = 100

    def get(self, endpoint: str) -> Optional[Dict[str, Any]]:
        """Simulates a GET request with artificial latency."""
        logger.info(f"GET request to {endpoint}")
        self._simulate_latency()
        
        if endpoint in self.data_store:
            return {"status": 200, "body": self.data_store[endpoint]}
        
        logger.warning(f"Endpoint {endpoint} not found.")
        return {"status": 404, "body": {"error": "Not Found"}}

    def post(self, endpoint: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Simulates a POST request."""
        logger.info(f"POST request to {endpoint} with payload {json.dumps(payload)}")
        self._simulate_latency()
        
        # Simple mock logic
        if endpoint == "/users":
            new_user = {"id": len(self.data_store["/users"]) + 1, **payload}
            self.data_store["/users"].append(new_user)
            return {"status": 201, "body": new_user}
            
        return {"status": 400, "body": {"error": "Bad Request"}}

    def _simulate_latency(self):
        if self.latency_ms > 0:
            time.sleep(self.latency_ms / 1000.0)

if __name__ == "__main__":
    api = MockAPI()
    print(api.get("/users"))
    print(api.post("/users", {"name": "Charlie"}))
    print(api.get("/users"))
