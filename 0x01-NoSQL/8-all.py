#!/usr/bin/env python3
"""List all documents in Python"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """list all documents in collection
    param: mongo_collection
    return: None or List
    """
    if mongo_collection is None:
        return None

    documents = mongo_collection.find()
    for document in documents:
        return document
