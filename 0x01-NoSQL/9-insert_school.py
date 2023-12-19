#!/usr/bin/env python3
"""Insert a document in Python"""


def insert_school(mongo_collection, **kwargs):
    """Insert a document
    param1: mongo_collection 
    param2: **kwargs
    return: None
    """

    documents = mongo_collection.insert({**kwargs})
    return documents
