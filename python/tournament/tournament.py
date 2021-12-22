"""
Set Task: Given rows (list) which is a list of matchups including the winner, generate a scoreboard.
Method:
* Going through rows, we check if the two teams are already in teams (dict). If no, a new team is created.
* On init, a team's name is set and all attributes (wins, ties, loss, points, matches) set to 0.
* On __add__, matches is increased by 1 and, depending on result, all other attributes are updated.
* Going through rows, each team of a row is added with the result.
* After having parsed all rows, we have a dictionary of teams, which all have stored the relevant information. This then gets put into a nice output format.
Example:
* results = [
            "Allegoric Alaskans;Blithering Badgers;win",
            "Courageous Californians;Blithering Badgers;win",
            "Allegoric Alaskans;Courageous Californians;draw",
        ]
* tally(results)
    (-> teams={'Allegoric Alaskans': <__main__.Team object>, 'Blithering Badgers': <__main__.Team object>, 'Courageous Californians': <__main__.Team object>})
    (-> teams["Allegoric Alaskans"] -> "Allegoric Alaskans             |  2 |  1 |  1 |  0 |  4")
    -> [
        'Team                           | MP |  W |  D |  L |  P',
        'Allegoric Alaskans             |  2 |  1 |  1 |  0 |  4',
        'Courageous Californians        |  2 |  1 |  1 |  0 |  4',
        'Blithering Badgers             |  2 |  0 |  0 |  2 |  0'
    ]
"""

class Team:
    def __init__(self,name):
        self.name=name
        self.wins=0
        self.ties=0
        self.loss=0
        self.points=0
        self.matches=0

    def __str__(self):
        delimiter=" |  "
        return self.name+" "*(30-len(self.name))+delimiter+str(self.matches)+delimiter+str(self.wins)+delimiter+str(self.ties)+delimiter+str(self.loss)+delimiter+str(self.points)

    def __add__(self,result):
        self.matches+=1
        if result=="win":
            self.wins+=1
            self.points+=3
        elif result=="draw":
            self.ties+=1
            self.points+=1
        else:
            self.loss+=1
        return self

    def getPoints(self):
        return self.points

    def getName(self):
        return self.name

def tally(rows):
    teams=dict()
    delimiter=" | "
    output=["Team"+" "*26+delimiter+"MP"+delimiter+" W"+delimiter+" D"+delimiter+" L"+delimiter+" P"]
    for r in rows:
        result=r.split(";")
        res=result[2]
        try:
            teams[result[0]]+res
        except:
            teams[result[0]]=Team(result[0])
            teams[result[0]]+res
        if result[2]=="win":
            res="loss"
        elif result[2]=="loss":
            res="win"
        else:
            res=result[2]
        try:
            teams[result[1]]+res
        except:
            teams[result[1]]=Team(result[1])
            teams[result[1]]+res
    print(teams["Allegoric Alaskans"])
    teamsSorted={k: v.getPoints() for k,v in teams.items()}
    outputHelper=[x[0] for x in sorted(teamsSorted.items(),key = lambda kv: (-kv[1],kv[0]))]
    [output.append(str(teams[x])) for x in outputHelper]
    return output

results = [
            "Allegoric Alaskans;Blithering Badgers;win",
            "Courageous Californians;Blithering Badgers;win",
            "Allegoric Alaskans;Courageous Californians;draw",
        ]
print(tally(results))