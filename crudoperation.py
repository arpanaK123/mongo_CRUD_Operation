#!/usr/bin/python3
import connect as connections
con = connections.connect()


def create():
    if con is not None:
        db = con["docs"]
        collection = db["arpana"]
        collection.insert_one(
            {"_id": 777, "Name": "Arpana", "City": "Bangalore"})
        collection.insert_many(
            [{"_id": 111, "Name": "Ankit", "City": "Bangalore", "Designation": "Software Engg"},
             {"_id": 222, "Name": "Riya", "City": "Bangalore",
                 "Designation": "Software Engg"},
                {"_id": 333, "Name": "Monika", "City": "Bangalore", "Designation": "Software Engg"}])


def readData(id):
    if con is not None:
        db = con["docs"]
        collection = db["arpana"]
        data = collection.find_one({"_id": id})
        if data:
            return print(data["Name"], data["City"])
        else:
            return False


def update(id):
    if con is not None:
        db = con["docs"]
        collection = db["arpana"]
        dataUpdate = collection.update({"_id": id}, {"$set": {"City": "AARA"}})
        dataUpdate = collection.update_many(
            {"_id": id}, {"$set": {"City": "Bangalore", "Name": "Riya"}})
        if dataUpdate:
            return True
        else:
            return False


def deleteData(id):
    if con is not None:
        db = con["docs"]
        collection = db["arpana"]
        deleteddata = collection.delete_one({"_id":id})
        deleteMany=collection.delete_many()

def deleteMany():
    if con is not None:
        db = con["docs"]
        collection = db["arpana"]
        deleteMany=collection.delete_many({"Name": {"$in":["Arpana","Ankit"]}})



# create()
# # readData(222)
# # update(222)
# deleteData(333)
deleteMany()
