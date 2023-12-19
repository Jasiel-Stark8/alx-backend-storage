#!/usr/bin/env python3
"""returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """return specific topic in school list
    param1: mongo_collection
    param2: topic
    return: None or Topic
    """

    topic = mongo_collection.find({"topic": topic})
    return topic
