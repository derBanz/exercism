"""
Set task: Given scores (list), determine the latest score, the personal best score and the personal top three.
Method:
* To determine the latest score we return the last entry of scores.
* To determine the personal best we return the maximum of scores.
* To determine the personal top three we reverse sort the list and return a slice of the first three entries.
Example:
* latest([10,30,5,20]) -> 20
* personal_best([10,30,5,20]) -> 30
* personal_top_three([10,30,5,20]) (-> [30,20,10,5]) -> [30,20,10]
"""

def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scores.sort(reverse=True)
    return scores[0:3]
