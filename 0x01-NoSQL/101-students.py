#!/usr/bin/env python3
"""Top students"""


def top_students(mongo_collection, score):
    """return all students sorted by average score"""
    top = mongo_collection.find({"$avg": {"score": score}})
    return top
