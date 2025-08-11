#!/usr/bin/env python3
"""
A module for a function that provides some stats about Nginx logs stored in
MongoDB.
"""
from pymongo import MongoClient


if __name__ == "__main__":
    """ Make a check for all elements in a collection """
    client = MongoClient()
    collection = client.logs.nginx

    print(f"{collection.estimated_document_count()} logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        method_count = collection.count_documents({'method': method})
        print(f"\tmethod {method}: {method_count}")

    check_get = collection.count_documents({
        'method': 'GET', 'path': "/status"
    })
    print(f"{check_get} status check")
