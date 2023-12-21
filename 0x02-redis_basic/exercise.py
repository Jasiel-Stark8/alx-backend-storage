#!/usr/bin/env python3
"""Writing strings to Redis"""

from typing import Union
import uuid
import redis


class Cache:
    """Parent Cache Class"""

    def __init__(self):
        """Initialize redis connection and flush db at start"""
        self._redis = redis.Redis(host='localhost', port=6379)
        self._redis.flushdb()

    def store(self, data: Union[str, int, bytes, float]) -> str:
        """Generate uuid and store string data"""
        if data:
            key = str(uuid.uuid4())
            self._redis.set(key, data)
            return key
