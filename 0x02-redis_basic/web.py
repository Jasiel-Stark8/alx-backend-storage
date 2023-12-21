#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""

import requests
import redis


# Connect to local Redis instance
r = redis.StrictRedis(host='localhost', port=6379)


def get_page(url: str) -> str:
    """Track how many times a website has been visited.
    Cache the website content and expire after 10 seconds.
    """
    # Construct a Redis key using the URL
    cache_key = "cache:" + url
    count_key = "count:" + url

    # Check if the cached data is available
    if r.exists(cache_key):
        # Increment the count of visits
        r.incr(count_key)
        # Return the cached data
        return r.get(cache_key).decode('utf-8')

    # If not cached, fetch the data using 'requests'
    res = requests.get(url)
    content = res.text

    # Store the fetched data in Redis, set to expire after 10 seconds
    r.setex(cache_key, 10, content)

    # Initialize or increment the count of visits
    r.incr(count_key)

    # Return the fetched data
    return content


if __name__ == "__main__":
    url = 'http://slowwly.robertomurray.co.uk'
    content = get_page(url)
    print(content)
