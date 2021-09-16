"""
Set Task: Allow robots to be built. Once built, each robot needs a random but unique name.
Method:
* On init, each robot gets generated a random name.
** The first two characters are letters from the alphabet.
** The following three characters are digits.
** The resulting name is checked against robots (list) containing all existing robots' names. If the name already exists a new one is generated, otherwise it is kept and appended to robots.
* On reset, a new name is generated as in init. After this has been successful, the old name is removed from robots.
Example:
* R = Robot() -> RX837
* R.reset() -> AI262
"""

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