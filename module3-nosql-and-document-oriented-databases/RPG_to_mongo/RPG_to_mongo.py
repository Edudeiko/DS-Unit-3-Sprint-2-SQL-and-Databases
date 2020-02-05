import pymongo
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()
DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")
connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)
client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)
print("----------------")
print("COLLECTIONS:")
db = client.RPG
collection = db.rpg_db
print(db.list_collection_names())

# Commented it out after first execute,
# to prevent creating the duplicate with the different id

# collection.insert_one({
#     "model": "charactercreator.character",
#     "pk": 1,
#     "fields": {"name": "Aliquid iste optio reiciendi", "level": 0,
#     "exp": 0,
#     "hp": 10,
#     "strength": 1,
#     "intelligence": 1,
#     "dexterity": 1,
#     "wisdom": 1,
#     "inventory": [20, 58, 85],
# }})
# print("DOCS:", collection.count_documents({}))
# print(collection.count_documents({"pk": 1}))

new_objects = [
    {"model": "charactercreator.character",
    "pk": 2,
    "fields": {"name": "Optio dolorem ex a",
    "level": 0,
    "exp": 0,
    "hp": 10,
    "strength": 1,
    "intelligence": 1,
    "dexterity": 1,
    "wisdom": 1,
    "inventory": [93, 115, 133]}},
    {"model": "charactercreator.character",
    "pk": 3,
    "fields": {"name": "Minus c",
    "level": 0,
    "exp": 0,
    "hp": 10,
    "strength": 1,
    "intelligence": 1,
    "dexterity": 1,
    "wisdom": 1,
    "inventory": [8, 43]}},
    {"model": "charactercreator.character",
    "pk": 4,
    "fields": {"name": "Sit ut repr",
    "level": 0,
    "exp": 0,
    "hp": 10,
    "strength": 1,
    "intelligence": 1,
    "dexterity": 1,
    "wisdom": 1,
    "inventory": [21, 82, 85, 135]}}
]
collection.insert_many(new_objects)
print("DOCS:", collection.count_documents({}))