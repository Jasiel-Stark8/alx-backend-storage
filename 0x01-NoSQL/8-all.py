#!/usr/bin/env python3
"""List all documents in Python"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """Function to list MongoDB documents"""
    if mongo_collection is None:
        return None

    documents = mongo_collection.find()
    for document in documents:
        print(document)
        return document
