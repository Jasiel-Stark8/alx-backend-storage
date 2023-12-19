#!/usr/bin/env python3
"""Change school topics"""


def update_topics(mongo_collection, name, topics):
    """update school topic
    param1: mongo_collection
    param2: name
    param3: topics
    return None or update
    """

    documents = mongo_collection.update_many({"name": name}, {"$set" {"topics": topics}})
    return documents
