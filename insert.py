#!/usr/bin/python3
import connect as con
import time
N = 10
cli = con.connect()
samples = list()
if cli is not None:
    db = cli["ledger"]
    coll = db["transactions"]
    mydict = { "t_id":1,"total_supply": 1000 }
    x = coll.insert_one(mydict)
    # start = time.time()
    # insert = coll.insert_many(samples)
    # end = time.time() - start
    # print("Time Taken",end)
    # print(insert.inserted_ids)

