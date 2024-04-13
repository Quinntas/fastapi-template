import redis

from src.utils.env import env


class RedisClient:
    def __init__(self):
        self.redis = redis.StrictRedis(
            host=env.REDIS_HOST,
            port=env.REDIS_PORT,
            decode_responses=True,
        )

    def get(self, key):
        return self.redis.get(key)

    def set(self, key, value: str, ex: int = 3600):
        self.redis.set(key, value, ex)

    def delete(self, key):
        self.redis.delete(key)


redis_client = RedisClient()
