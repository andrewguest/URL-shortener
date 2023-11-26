import redis.asyncio as redis

redis_client_async = redis.Redis(decode_responses=True)
