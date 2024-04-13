import redis


class RedisClient:
    def __init__(self, host: str, port: int):
        self.redis = redis.StrictRedis(
            host=host,
            port=port,
            decode_responses=True,
        )

    def get(self, key):
        return self.redis.get(key)

    def set(self, key, value: str, ex: int = 3600):
        self.redis.set(key, value, ex)

    def delete(self, key):
        self.redis.delete(key)
