#!/usr/bin/env python3
"""Writing strings to Redis"""

import redis
import uuid
from typing import Union


class Cache:
    """Parent Cache Class"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, int]) -> str:
        if data:
            key = str(uuid.uuid4())
            self._redis.set(key, data)
            return key
