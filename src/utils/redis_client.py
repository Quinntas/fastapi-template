import redis


class RedisClient:
    """
    Initialize a RedisClient object.

    :param host: str - The host of the Redis server.
    :param port: int - The port of the Redis server.
    """

    def __init__(self, host: str, port: int):
        self.redis = redis.StrictRedis(
            host=host,
            port=port,
            decode_responses=True,
        )

    def get(self, key):
        """
        Get the value stored in Redis for the given key.

        :param key: The key for which the value needs to be retrieved from Redis.
        :return: The value stored in Redis for the given key.
        """
        return self.redis.get(key)

    def set(self, key, value: str, ex: int = 3600):
        """
        :param key: the key to set in the Redis database
        :param value: the value to set for the given key
        :param ex: the expiration time in seconds for the key-value pair (default is 3600 seconds)
        :return: None

        Set the given key-value pair in the Redis database with an optional expiration time.
        If the ex parameter is not provided, the key-value pair will expire after 3600 seconds by default.
        """
        self.redis.set(key, value, ex)

    def delete(self, key):
        """
        Delete a key-value pair from Redis.

        :param key: The key to delete.
        :return: None.
        """
        self.redis.delete(key)
