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

    teamsSorted={k: v.getPoints() for k,v in teams.items()}
    outputHelper=[x[0] for x in sorted(teamsSorted.items(),key = lambda kv: (-kv[1],kv[0]))]
    [output.append(str(teams[x])) for x in outputHelper]
    return output

results = [
            "Courageous Californians;Devastating Donkeys;win",
            "Allegoric Alaskans;Blithering Badgers;win",
            "Devastating Donkeys;Allegoric Alaskans;loss",
            "Courageous Californians;Blithering Badgers;win",
            "Blithering Badgers;Devastating Donkeys;draw",
            "Allegoric Alaskans;Courageous Californians;draw",
        ]

print(tally(results))