# database.py
from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
db = client["blockchainDB"]
collection = db["blocks"]

def save_block_to_db(block):
    collection.insert_one({
        "index": block.index,
        "data": block.data,
        "timestamp": block.timestamp,
        "hash": block.hash,
        "previous_hash": block.previous_hash
    })
