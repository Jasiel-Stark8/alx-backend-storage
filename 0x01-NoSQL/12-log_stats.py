#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient


methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

def log_stats(logs, nginx):
    """show logs
    param1: database name
    param2: collection name
    return: status | all logs OR None
    """
    if logs is None:
        return None

    log_collection = logs[nginx].find({})
    num_logs = 0
    method_count = {method: 0 for method in methods}

    for log in log_collection:
        num_logs += 1
        if 'method' in log:
            if log['method'] in methods:
                method_count[log['method']] += 1
    print(f"{num_logs} logs")
    for method in methods:
        print(f"Methods: \n method {method}: {method_count[method]}")
