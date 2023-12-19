#!/usr/bin/env python3
"""Log stats - Nginx logs analysis"""
from pymongo import MongoClient


def log_stats():
    """Function to print stats about Nginx logs"""
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    nginx_collection = db.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_count = {method: nginx_collection.count_documents({"method":\
        method}) for method in methods}
    total_logs = sum(method_count.values())
    status_check_logs = nginx_collection.count_documents({"method": "GET", "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_count[method]}")
    print(f"{status_check_logs} status check")


if __name__ == "__main__":
    log_stats()
