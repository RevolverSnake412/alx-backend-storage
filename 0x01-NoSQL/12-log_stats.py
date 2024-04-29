#!/usr/bin/env python3
'''
TASK 12
'''


from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    total = logs.count_documents({})
    print(f"{total} logs")
    
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = logs.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    count = logs.count_documents({"method": "GET", "path": "/status"})
    print(f"{count} status check")
