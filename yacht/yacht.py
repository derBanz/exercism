"""
Set Task: Given dice (list) and category (String), calculate the score the dice would give in a game of yacht.
Method:
* dice is sorted, and sorted_dice (list) is created to display how many dice have the same result.
* Going through the possible categories, the correct score is calculated.
Example: score([1,5,3,4,2],LITTLE_STRAIGHT) -> 30
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


# Score categories.
# Change the values as you see fit.
YACHT = "10"
ONES = "01"
TWOS = "02"
THREES = "03"
FOURS = "04"
FIVES = "05"
SIXES = "06"
FULL_HOUSE = "11"
FOUR_OF_A_KIND = "12"
LITTLE_STRAIGHT = "13"
BIG_STRAIGHT = "14"
CHOICE = "15"


def score(dice, category):
    res=0
    dice=sorted(dice)
    dice_list=[0,0,0,0,0,0]
    for d in dice:
        dice_list[d-1]+=1
    sorted_dice=sorted(dice_list,reverse=True)
    if category[0]=="0":
        x=int(category[1])
        res=x*dice_list[x-1]
    else:
        if category[1]=="0":
            res=50*(sorted_dice[0]==5)
        elif category[1]=="1":
            res=sum(dice)*(sorted_dice[0]==3 and sorted_dice[1]==2)
        elif category[1]=="2":
            try:
                res=(dice_list.index(4)+1)*4
            except:
                try:
                    res=(dice_list.index(5)+1)*4
                except:
                    pass
        elif category[1]=="3":
            res=30*(max(dice_list)==1 and dice_list[-1]==0)
        elif category[1]=="4":
            res=30*(max(dice_list)==1 and dice_list[0]==0)
        elif category[1]=="5":
            res=sum(dice)
        else:
            pass
    return res