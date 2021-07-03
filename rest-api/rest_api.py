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