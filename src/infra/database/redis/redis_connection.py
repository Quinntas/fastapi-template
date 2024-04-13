from src.utils.env import env
from src.utils.redis_client import RedisClient

redis_client = RedisClient(
    host=env.REDIS_HOST,
    port=env.REDIS_PORT,
)
