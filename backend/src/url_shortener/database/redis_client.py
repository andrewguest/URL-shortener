import os

import redis.asyncio as redis

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

redis_client_async = redis.Redis(decode_responses=True).from_url(REDIS_URL)
