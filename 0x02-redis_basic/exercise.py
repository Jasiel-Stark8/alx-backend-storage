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


def call_history(method: Callable) -> Callable:
    """Store the history of inputs and outputs for a particular function."""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = "{}:inputs".format(method.__qualname__)
        output_key = "{}:outputs".format(method.__qualname__)
        # Store the input arguments (as a string) in the ":inputs" list
        self._redis.rpush(input_key, str(args))
        # Execute the wrapped function and store the output
        result = method(self, *args, **kwargs)
        # Store the output in the ":outputs" list
        self._redis.rpush(output_key, str(result))

        return result
    return wrapper


def replay(method: Callable):
    """Function to display the history of calls of a particular function."""
    self = method.__self__  # Get the instance (Cache) from the method
    method_name = method.__qualname__
    inputs_key = "{}:inputs".format(method_name)
    outputs_key = "{}:outputs".format(method_name)

    # Get the number of times the method was called
    count = self._redis.get(method_name).decode("utf-8")

    # Retrieve the history of inputs and outputs
    inputs = self._redis.lrange(inputs_key, 0, -1)
    outputs = self._redis.lrange(outputs_key, 0, -1)

    print(f"{method_name} was called {count} times:")

    # Loop over inputs and outputs and print them
    for input_val, output_val in zip(inputs, outputs):
        input_str = input_val.decode("utf-8")
        output_str = output_val.decode("utf-8")
        print(f"{method_name}(*{input_str}) -> {output_str}")



class Cache:
    """Parent Cache Class"""

    def __init__(self):
        """Initialize Redis and flush the database."""
        self._redis = redis.Redis(host='localhost', port=6379)
        self._redis.flushdb()

    @count_calls
    @call_history
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
