#!/usr/bin/env python3
"""
A module for a function that inserts a new document in a collection
based on kwargs (MongoDB).
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
