import math

class Clock:
    def __init__(self, hour, minute):
        self.time=(hour*60+minute)%(60*24)

    def __repr__(self):
        hours=math.floor(self.time/60)
        if hours<10:
            hours="0"+str(hours)
        else:
            hours=str(hours)
        minutes=self.time%60
        if minutes<10:
            minutes="0"+str(minutes)
        else:
            minutes=str(minutes)
        return hours+":"+minutes

    def __eq__(self, other):
        return self.time==other.time

    def __add__(self, minutes):
        self.time+=minutes%(24*60)
        if self.time > 24*60:
            self.time-=24*60
        return self

    def __sub__(self, minutes):
        self.time-=minutes%(24*60)
        if self.time < 0:
            self.time+=24*60
        return self

c=Clock(2,-60)
d=Clock(0,1441)
print(c,d)
print(c==d)