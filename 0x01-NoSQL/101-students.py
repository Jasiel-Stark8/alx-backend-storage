#!/usr/bin/env python3
"""Top students"""


def top_students(mongo_collection, score):
    """return all students sorted by average score"""
    pipeline = [
        {
            "$unwind": "scores"
        },
        {
            "$group": {
                "_id": "$_id",
                "name": {"$first": "$name"},
                "scores": "{$avg: $scores.score}"
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]

    top = mongo_collection.aggregate(pipeline)
    return list(top)
