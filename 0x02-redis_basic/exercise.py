#!/usr/bin/env python3
"""Redis caching"""

import functools
import redis
import uuid
from typing import Callable, Union, Optional


def count_calls(method: Callable) -> Callable:
    """Increment the count for every call to the cached method"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Parent Cache Class"""

    def __init__(self):
        """Initialize Redis and flush the database."""
        self._redis = redis.Redis(host='localhost', port=6379)
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the data in Redis using a random key and return the key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """Retrieve data by key and convert it using the callable `fn`."""
        value = self._redis.get(key)
        if value is not None and fn:
            return fn(value)
        return value


    def get_str(self, key: str) -> Optional[str]:
        """Retrieve a string value by key."""
        return self.get(key, lambda d: d.decode("utf-8"))


    def get_int(self, key: str) -> Optional[int]:
        """Retrieve an integer value by key."""
        value = self.get(key)
        return int(value) if value is not None else None
