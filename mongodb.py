from pymongo import MongoClient
import datetime

client = MongoClient("mongodb+srv://prakash-123:Meronepal1@scrapy-mongo.qctvs5f.mongodb.net/")

db = client.scrapy

posts = db.test_collection

doc = post = {"author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.now()}

post_id = posts.insert_one(post).inserted_id

print(post_id)

