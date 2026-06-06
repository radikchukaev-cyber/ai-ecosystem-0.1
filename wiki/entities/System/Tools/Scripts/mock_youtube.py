import random
import logging
from typing import List, Dict, Any

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MockYouTubeClient:
    """Mocks interactions with the YouTube API for testing content fetching."""
    
    def __init__(self, api_key: str = "mock_key"):
        self.api_key = api_key
        logger.info(f"Initialized Mock YouTube Client with key {self.api_key[:4]}...")

    def search_videos(self, query: str, max_results: int = 5) -> List[Dict[str, Any]]:
        """Simulates searching for videos."""
        logger.info(f"Searching YouTube for: '{query}' (max {max_results} results)")
        
        results = []
        for i in range(max_results):
            video_id = f"mockVid{random.randint(1000, 9999)}"
            results.append({
                "id": video_id,
                "title": f"Result {i+1} for {query}",
                "description": f"This is a mock description for video {video_id}.",
                "url": f"https://youtube.com/watch?v={video_id}",
                "views": random.randint(100, 1000000)
            })
            
        return results

    def get_video_details(self, video_id: str) -> Dict[str, Any]:
        """Simulates fetching specific video details."""
        logger.info(f"Fetching details for video ID: {video_id}")
        
        return {
            "id": video_id,
            "title": "A Very Interesting Mock Video",
            "author": "Mock Creator",
            "duration": "10:30",
            "likes": random.randint(10, 50000),
            "tags": ["mock", "testing", "api"]
        }

if __name__ == "__main__":
    yt = MockYouTubeClient()
    
    search_res = yt.search_videos("AI development tutorials", max_results=3)
    for res in search_res:
        print(f"Title: {res['title']} | URL: {res['url']}")
        
    details = yt.get_video_details(search_res[0]["id"])
    print(f"Details: {details}")
