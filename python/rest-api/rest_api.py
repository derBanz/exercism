"""
Set Task: Implement a RESTful API for tracking IOUs.
Method:
* On init: If a database already exists it is saved as self.users (dict). Otherwise, an empty database is saved instead.
* On get:
** If a payload (json) is specified, return the specified user's balance.
** If a payload is not specified, return all users' balance.
* On post:
** if url (String) is "/add", a new user is registered in the database.
** if url (String) is "/iou", the balance of both involved users' is updated accordingly.
Examples, using the following database:
database = {
            "users": [
                {"name": "Adam", "owes": {}, "owed_by": {}, "balance": 0.0},
                {"name": "Bob", "owes": {}, "owed_by": {}, "balance": 0.0}
            ]
        }
* get({"users": "Bob"}) -> {"users": [{"name": "Bob", "owes": {}, "owed_by": {}, "balance": 0.0}]}
* post("/iou",{"lender": "Adam", "borrower": "Bob", "amount": 3.0}) -> 
        {
            "users": [
                {"name": "Adam", "owes": {}, "owed_by": {"Bob": 3.0}, "balance": 3.0},
                {"name": "Bob", "owes": {"Adam": 3.0}, "owed_by": {}, "balance": -3.0}
            ]
        }
* post("/add",{"user": "Cesar"}) -> 
        {
            "users": [
                {"name": "Adam", "owes": {}, "owed_by": {"Bob": 3.0}, "balance": 3.0},
                {"name": "Bob", "owes": {"Adam": 3.0}, "owed_by": {}, "balance": -3.0},
                {"name": "Cesar", "owes": {}, "owed_by": {}, "balance": 0.0}
            ]
        }

"""

import json

class RestAPI:
    def __init__(self, database=None):
        if database != None:
            self.users=database
        else:
            self.users={"users": list()}

    def get(self, url="/users", payload=None):
        if payload == None:
            return json.dumps(self.users)
        
        data=self.users["users"]
        key=json.loads(payload)["users"]
        data=next(item for item in data if item["name"]==key[0])
        return json.dumps({"users": [data]})

    def post(self, url, payload=None):
        if url=="/add":
            data={"name": json.loads(payload)["user"], "owes": {}, "owed_by": {}, "balance": 0.0}
            self.users["users"].append(data)
            return json.dumps(data)
        elif url=="/iou":
            data=json.loads(payload)
            res={"users": list()}
            for i in range(len(self.users["users"])):
                if self.users["users"][i]["name"]==data["lender"]:
                    amount=self.users["users"][i]["owes"].pop(data["borrower"],0)-data["amount"]
                    if amount<0:
                        self.users["users"][i]["owed_by"][data["borrower"]]=abs(amount)
                    elif amount>0:
                        self.users["users"][i]["owes"][data["borrower"]]=amount
                    self.users["users"][i]["balance"]+=data["amount"]
                    res["users"].append(self.users["users"][i])
                elif self.users["users"][i]["name"]==data["borrower"]:
                    amount=self.users["users"][i]["owed_by"].pop(data["lender"],0)-data["amount"]
                    if amount<0:
                        self.users["users"][i]["owes"][data["lender"]]=abs(amount)
                    elif amount>0:
                        self.users["users"][i]["owed_by"][data["lender"]]=amount
                    self.users["users"][i]["balance"]=self.users["users"][i]["balance"]-data["amount"]
                    res["users"].append(self.users["users"][i])
        
        return json.dumps(res)