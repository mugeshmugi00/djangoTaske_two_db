from . import db
from bson import ObjectId


def findUser(userId):
    userObjId = ObjectId(userId)
    user = db.coll.find_one({"_id":userObjId})
    return user