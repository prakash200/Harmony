from fastapi import FastAPI, Query, HTTPException
from cachetools import TTLCache
import requests
import uvicorn

app = FastAPI()


# Hacker news Base Api
BASE_URL = "https://hacker-news.firebaseio.com/v0/"

# Cache configuration: 5-minute TTL for story details
cache = TTLCache(maxsize=100, ttl=300)  

# Fetching story_is's
def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for error HTTP statuses
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data: {e}")


# Fetching the top N top_story_ids
def get_top_stories(count: int = 10):
    try:
        url = f"{BASE_URL}topstories.json"
        story_ids = fetch_data(url)[:count]
        return story_ids
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching top stories: {e}")


# Fetching story_details with corresponding story_id
def get_story_details(story_id):
    try:
        
        cached_story = cache.get(story_id)
        if cached_story:
            return cached_story
        story_details = fetch_data(f"{BASE_URL}item/{story_id}.json")
        cache[story_id] = story_details
        return story_details
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching story details: {e}")


# Api which retrives top news items
@app.get("/top-news")
async def top_news(count: int = Query(default=10, ge=1, le=50)):
    print("_________ Cahche Data Check  ____________")
    print(cache)
    try:
        story_ids = get_top_stories(count)
        stories = [get_story_details(id) for id in story_ids]
        return stories
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching top news: {e}")
    
