from random import randrange

robots = list()

class Robot:
    def __init__(self):
        self.createName()

    def createName(self):
        var = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        while True:
            name = ""
            for i in range(2):
                name += var[randrange(26)]
            for i in range(3):
                name += var[26::][randrange(10)]
            if name not in robots:
                break
        self.name = name

        robots.append(name)

    def reset(self):
        oldName = self.name
        self.createName()
        robots.remove(oldName)