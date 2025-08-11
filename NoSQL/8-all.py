#!/usr/bin/env python3
"""
A module for a function that lists all documents in a collection (MongoDB).
"""


def list_all(mongo_collection):
    """
    The method to list all documents in a collection
    Args:
        mongo_collection: The collection
    """
    return list(mongo_collection.find())