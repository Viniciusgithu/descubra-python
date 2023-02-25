#pip install pymongo

import pymongo
from pymongo import MongoClient

def manipulation():
    client = pymongo.MongoClient('')
    db = client.restaurant
    for i in range(1,10):
        objDic = {'Código': 1}
        db.requests_restaurant.insert_one(objDic)

    db.requests_restaurant.update_one({'código: 2'}, {"$set: {'new attribute': 789}"})
    db.requests_restaurant.delete_one({'código: 1'})

    resultQuery = db.requests_restaurant.find({})
    for doc in resultQuery:
        print(doc) 


manipulation()              