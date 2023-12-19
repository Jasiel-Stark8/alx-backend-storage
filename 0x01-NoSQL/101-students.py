#!/usr/bin/env python3
"""Top students"""


def top_students(mongo_collection):
    """Return all students sorted by average score"""
    pipeline = [
        {
            "$unwind": "$scores"
        },
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    top = mongo_collection.aggregate(pipeline)
    return top
