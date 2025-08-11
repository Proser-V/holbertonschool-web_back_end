#!/usr/bin/env python3
"""
A module for a function that provides some stats about Nginx logs stored in
MongoDB.
"""
from pymongo import MongoClient

def nginx_logs():
    """
    Provides some stats about Nginx logs stored in MongoDB.
    """
    client = MongoClient()
    db = client["logs"]
    collection = db["nginx"]

    total_logs = collection.count_documents({})
    print (f'{total_logs} logs')

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({ "method": method })
        print(f'\tmethod {method}: {count}')

    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    nginx_logs()
