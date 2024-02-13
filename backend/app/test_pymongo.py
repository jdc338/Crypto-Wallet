from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test
print("Connected to MongoDB:", db.name)
