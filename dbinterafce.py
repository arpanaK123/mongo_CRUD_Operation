#!/usr/bin/python3
import connect as connections
import random
import time
client_num = 5
su_bal = 100000
conn = connections.connect()
policies = {1: "Individual", 2: "Group", 3: "Default"}
public_key = [1111111111, 2222222222, 3333333333, 44444444444, 5555555555]


def metaDBTokenList(token_title, tokendb_name):
    if conn is not None:
        metadb = conn["metadb"]["tokenlist"]
        result = metadb.insert_one(
            {"token_title": token_title, "tokendb": tokendb_name})
        if result:
                return True
        else:
                return False
    else:
             return "Connection failed"


def createDataBase(tokendb_name, token_title):
    if conn is not None:
        tokendb = conn[tokendb_name]
        transactionsdb = tokendb["transactions"]
        clientdb = tokendb['clientdata']
        metaDBTokenList(token_title, tokendb_name, 1000)
        initClientDB(clientdb, token_title)
    else:
            return "Connection failed"


def initClientDB(clientdb, token_title):
    if conn is not None:
        data = {"_id": 100, "balance": su_bal, "public_key": "1234567890",
                "policy": 1, "auth": True, "time_stamp": time.time()}
        su_result = clientdb.insert_one(data)
        if su_result:
                for i in range(client_num):
                        policies_id = random.randint(1, 3)
                        policy = policies[policies_id]
                        data = {"_id": i, "balance": 0, "public_key": public_key[i] ,
                                "policy": policy, "auth": False, "time_stamp": time.time()}
                        result = clientdb.insert_one(data)
                        print(result)
                        if result is None:
                                return False
        else:
                return False
    else:
            return "Connection failed"


def getClientDB(token_title):
    if conn is not None:
        metadb = conn["metadb"]["tokenlist"]
        token = metadb.find_one({"token_title":token_title})
        tokendb = token["tokendb"]
        clientdb = conn[tokendb]["clientdata"]
        return clientdb
    else:
        return None


def getTxnDB(token_title):
    if conn is not None:
        metadb = conn["metadb"]["tokenlist"]
        token = metadb.find_one({"token_title":token_title})
        tokendb = token["tokendb"]
        clientdb = getClientDB(token_title)
        clientdb = conn[tokendb]["transactions"]
        return clientdb
    else:
        return None


def getClientDetails(client_id, token_title):
        clientdb = getClientDB(token_title)
        if client_id is not None:
                c_details = clientdb.find_one({"_id": client_id})
                if c_details:
                        return c_details
                else:
                        return False
        else:
            print("Connection Failed")


def getBalance(client_id, token_title):
    if conn is not None:
        clientdb = getClientDB(token_title)
        clientdata = {"_id": client_id}
        result = clientdb.find_one(clientdata)
        if result:
                return result["balance"]
        else:
                return False
    else:
        return "Connection Failed"


def getPublicKeySU():
    if conn is not None:
        metadb = conn["metadb"]["tokenlist"]
        token = metadb.find_one()
        tokendb = token["tokendb"]
        clientdb = conn[tokendb]["clientdata"]
        details = clientdb.find_one({"auth": True})
        if details:
                return details["public_key"]
        else:
                return False
    else:
        return "Connection Failed"


def getPublicKey(client_id):
    if conn is not None:
        metadb = conn["metadb"]["tokenlist"]
        token = metadb.find_one()
        tokendb = token["tokendb"]
        clientdb = conn[tokendb]["clientdata"]
        details = clientdb.find_one({"_id": client_id})
        if details:
                return details["public_key"]
        else:
                return False
    else:
        return "Connection Failed"

def updateAmountDB(txn_id, sender_id, receiver_id, send_bal, recev_bal, time_stamp, token_title):
    if conn is not None:
        clientdb = getClientDB(token_title)
        transactionsdb = getTxnDB(token_title)
        s_result = clientdb.update({"_id": sender_id}, {
                        "$set": {"balance": send_bal, "time_stamp": time_stamp}})
        r_result = clientdb.update({"_id": receiver_id}, {
                        "$set": {"balance": recev_bal, "time_stamp": time_stamp}})

        t_result = transactionsdb.insert_one(
            {"txn_id": txn_id, "from": sender_id, "to": receiver_id, "from_bal": send_bal, "to_bal": recev_bal, "time_stamp": time_stamp, "type": "t"})
        if s_result and r_result and t_result:
                return True
        else:
                return False
    else:
        return "Connection Failed"

def getTotalSupply(token_title):
    if conn is not None:
        clientdb = getClientDB(token_title)
        details = clientdb.find_one({"auth": True})
        if details:
                return details["balance"]
        else:
                return False
    else:
        return "Connection Failed"

def tokenUpdate(token_title, amount):
    if conn is not None:
        clientdb = getClientDB(token_title)
        result = clientdb.update({"auth": True}, {"$set": {"balance": amount}})
        if result:
                return True
        else:
                return False
    else:
        return "Connection Failed"


def updateDBReqApr(req_id, session_id, sender_id, receiver_id, amount, time_stamp, token_title):
    if conn is not None:
        clientdb = getClientDB(token_title)
        transactionsdb = getTxnDB(token_title)
        result = transactionsdb.insert_one(
            {"req_id": req_id, "session_id": session_id, "from": sender_id, "to": receiver_id, "amount": amount, "time_stamp": time_stamp, "type": "e"})
        if result:
                return True
        else:
                return False
    else:
        return "Connection Failed"

