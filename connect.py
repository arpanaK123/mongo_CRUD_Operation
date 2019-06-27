#!/usr/bin/python3
import pymongo
IP = "127.0.0.1"

def connect():
    try:
#        conn = pymongo.MongoClient('mongodb://root:pass@localhost:27017/')
        cli = pymongo.MongoClient("mongodb://"+IP+":27017/")
        print("Connection Successfull!!")
        return cli
    except:
        print("Connection failed....")
        return None
