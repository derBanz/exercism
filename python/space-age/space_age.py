"""
Set Task: Given an age in seconds (int), calculate the age someone would be depending on a planet.
Method: On init, the current age is calculated relative to the Earth. On each method called it gets divided with the appropriate multiplier.
Example:
* S = SpaceAge(932342500)
* S.on_earth() = 29.54
* S.on_uranus() = 0.35
"""

class SpaceAge:
    def __init__(self, seconds):
        self.earth=seconds/60/60/24/365.25

    def on_earth(self):
        return round(self.earth,2)

    def on_mercury(self):
        return round(self.earth/0.2408467,2)

    def on_venus(self):
        return round(self.earth/0.61519726,2)

    def on_mars(self):
        return round(self.earth/1.8808158,2)

    def on_jupiter(self):
        return round(self.earth/11.862615,2)

    def on_saturn(self):
        return round(self.earth/29.447498,2)

    def on_uranus(self):
        return round(self.earth/84.016846,2)

    def on_neptune(self):
        return round(self.earth/164.79132,2) 