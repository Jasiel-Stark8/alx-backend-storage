#!/usr/bin/env python3

import redis

redis_host = 'localhost'
redis_port = 6379

def redis_string():
    try:
        r = redis.StrictRedis(host=redis_host,
                              port=redis_port,
                              decode_responses=True)
        r.set("message", "Hello Redis!")
        msg = r.get("message")
        print(msg)
    except Exception as e:
        print(f"Error: {e}")

def redis_int():
    try:
        r = redis.StrictRedis(host=redis_host,
                              port=redis_port,
                              decode_responses=True)
        r.set("number", "100")
        orig_num = r.get("number")
        r.incr("number")
        incr_num = r.get("number")
        print(orig_num)
        print(incr_num)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    redis_string()
    redis_int()
