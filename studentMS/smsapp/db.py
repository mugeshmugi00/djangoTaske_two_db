from pymongo import MongoClient
# local connect
Local_link = MongoClient("mongodb://localhost:27017/")
# data base
db = Local_link.studentMS
# collection
admins = db.admins
# students coll
studentcoll = db.students
# cours coll
courscoll = db.course

