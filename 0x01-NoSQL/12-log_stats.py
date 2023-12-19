#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient


def log_stats():
    """Show logs
    param1: database name
    param2: collection name
    return: status | all logs OR None
    """
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    nginx_collection = db.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_count = {method: nginx_collection.count_documents({"method": method}) for method in methods}

    log_total = sum(method_count.values())
    check_log_status = nginx_collection.count_documents({"method": "GET", "path": "/status"})

    print(f"{log_total} logs")
    print("Methods:")
    for method in methods:
        print(f"method {method}: {method_count[method]}")
    print(f"{check_log_status} status check")

if __name__ == "__main__":
    log_stats()
