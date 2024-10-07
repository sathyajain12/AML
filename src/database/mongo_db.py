# src/database/mongo_db.py

from pymongo import MongoClient

class MongoDBClient:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)  # Connect to the MongoDB server
        self.db = self.client[db_name]   # Select the database

    def get_collection(self, collection_name):
        """Return a collection from the database."""
        return self.db[collection_name]

    def close(self):
        """Close the connection to the MongoDB server."""
        self.client.close()
