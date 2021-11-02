"""
Set task: Determine if a triangle is equilateral, isosceles, or scalene.
Method:
* Check unique values in sides (list) using set() to eliminate duplicates.
* Separate validation function to make sure the sides form a triangle.
Example: equilateral([2,3,2]) (-> {2,3} -> 2 != 1) -> False
"""


def equilateral(sides):
    return len(set(sides)) == 1 and validation(sides)


def isosceles(sides):
    return len(set(sides)) < 3 and validation(sides)


def scalene(sides):
    return len(set(sides)) == 3 and validation(sides)


def validation(sides):
    sides = sorted(sides)
    return sides[0] + sides[1] >= sides[2] and sides[0] > 0
