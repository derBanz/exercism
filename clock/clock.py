"""Set task:
* Create a Clock class that stores time in 24h format. On init, it is given hour (int) and minute (int).
* The clock should be represented in the format "hh:mm".
* Two clocks storing the same time should be equal to each other.
* Adding a clock and minutes (int) should add minutes to the clock's time.
* Substracting minutes (int) from a clock should substract the minutes from the clock's time.
Method:
* On init, hour and minute are stored as minutes in self.time (int).
* On calling, self.time gets transformed to hours (int) and minutes (int) and returnd as hours":"minutes.
* On comparing, self.time of both clocks are compared.
* On adding and substracting, minutes (int) are added to/substracted from self.time
Example:
* C = Clock(8,0) (-> 480)
* C + 40 (-> 520) -> 08:40
* C = Clock(8,40) -> True
* C - 600 (-> -80 -> 1360) -> 22:40
"""

class Clock:
    def __init__(self, hour, minute):
        self.time=(hour*60+minute)%(60*24)

    def __repr__(self):
        hours=int(self.time/60)
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
        return self.getTime()==other.getTime()

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

    @property
    def getTime(self):
        return self.time