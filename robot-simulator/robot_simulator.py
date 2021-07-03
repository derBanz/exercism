# Globals for the directions
# Change the values as you see fit
EAST = 2
NORTH = 1
WEST = 0
SOUTH = 3


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.coordinates=(x,y)
        self.direction=direction

    def move(self,command):
        for c in command:
            if c == "L":
                self.direction=(self.direction-1)%4
            elif c == "R":
                self.direction=(self.direction+1)%4
            elif c == "A":
                x=(self.direction-1)*(self.direction%2==0)
                y=(2-self.direction)*(self.direction%2==1)
                self.coordinates=(self.coordinates[0]+x,self.coordinates[1]+y)
            else:
                raise ValueError("Invalid command.")