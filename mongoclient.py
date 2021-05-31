import os
import pymongo
client = pymongo.MongoClient(f"mongodb+srv://adl212:{os.environ.get('db_key', os.getenv('db_key'))}@cluster0.q3r5v.mongodb.net/test?retryWrites=true&w=majority")
class DBClient:
    def __init__(self):
        self.client = client
        self.db = self.client.botting
    def create_doc(self, collection, data):
        collection.insert_one(data)
    def close(self):
        self.client.close()