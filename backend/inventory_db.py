from pymongo import MongoClient
from datetime import datetime, timedelta

client = MongoClient("mongodb://localhost:27017/")
db = client["prexpiro"]
inventory_collection = db["inventory"]

def add_item(user_id, name, days_left):
    expiry_date = datetime.now() + timedelta(days=days_left)

    item = {
        "user_id": user_id,
        "name": name.lower(),
        "expiry_date": expiry_date,
        "created_at": datetime.now()
    }

    inventory_collection.insert_one(item)


def get_inventory(user_id):
    items = inventory_collection.find({"user_id": user_id})
    result = []

    for item in items:
        days_left = (item["expiry_date"] - datetime.now()).days
        result.append({
            "name": item["name"],
            "days_left": max(days_left, 1)
        })

    return result
