"""
Set Task: Given list_one (list) and list_two (list), determine if list_one is contained within list_two, if list_two is cointained within list_one, if both are equal or if none is true.
Method:
* An if/else check determines whether the lists are equal and if not, which list is bigger than the other.
* Using that information we loop through the bigger list and compare each slice of the size of the smaller list with the smaller list.
* If we do not find a match there the lists are unequal.
Example: sublist([1,3,5],[1,2,3,4,5]) -> "Unequal"
"""

"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "Sublist"
SUPERLIST = "Superlist"
EQUAL = "Equal"
UNEQUAL = "Unequal"


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif len(list_one) > len(list_two):
        bigger = list_one
        smaller = list_two
    else:
        bigger = list_two
        smaller = list_one
    for i in range(len(bigger)):
        if bigger[i:i + len(smaller)] == smaller and bigger == list_one:
            return SUPERLIST
        elif bigger[i:i + len(smaller)] == smaller and bigger == list_two:
            return SUBLIST
    return UNEQUAL