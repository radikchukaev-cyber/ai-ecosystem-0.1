import sys

def parse_youtube_link(url):
    """Mock parser for YouTube link extraction."""
    # Real implementation would use yt-dlp or similar
    if "youtube.com" in url or "youtu.be" in url:
        return {
            "title": "Mock Video Title",
            "url": url,
            "status": "success",
            "description": "Mock description extracted from " + url
        }
    return {"status": "error", "message": "Invalid YouTube URL"}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python youtube_parser.py <url>")
        sys.exit(1)
        
    print(parse_youtube_link(sys.argv[1]))
