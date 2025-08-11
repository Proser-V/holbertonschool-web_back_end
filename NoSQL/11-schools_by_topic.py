#!/usr/bin/env python3
"""
A module for a function that returns the list of school having a specific
topic (MongoDB).
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic.
    """
    result = mongo_collection.find(
        { "topic": topic }
    )
    return list(result)
