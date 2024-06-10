import cachetools
from datetime import timedelta

post_cache = cachetools.TTLCache(maxsize=100, ttl=timedelta(minutes=5).total_seconds())

def get_cached_posts(user_id: int):
    return post_cache.get(user_id)

def set_cached_posts(user_id: int, posts):
    post_cache[user_id] = posts
