#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""

import requests
import redis

# Connect to local Redis instance
r = redis.StrictRedis(host='localhost', port=6379)

def count_requests(method):
    """Decorator to count how many times a URL has been requested"""
    def wrapper(url):
        # Increment coutn for url
        r.incr(f'count: {url}')
        return method(url)
    return wrapper


def cache_page(method):
    """Decorator to cache pages and set an expiration time"""
    def wrapper(url):
        # cehck if page has been cached
        cached_content = r.get(f'cached: {url}')
        if cached_content:
            return cached_content.decode('utf-8')

        # Fetch content and cache if not cached
        content = method(url)
        r.setex(f'cached: {url}', 10, content)
        return content
    return wrapper


@count_requests
@cache_page
def get_page(url: str) -> str:
    """Obtain the HTML content of a particular URL and return it"""
    res = requests.get(url)
    return res.text


if __name__ == "__main__":
    url = 'http://slowwly.robertomurray.co.uk'
    content = get_page(url)
    print(content)
