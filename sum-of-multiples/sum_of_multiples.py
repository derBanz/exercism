"""
Set Task: Given limit (int) and multiples (list), sum up all numbers between 0 and limit that are multiples of multiples.
Method: Two nested for loops go through all numbers below limit and compare them with all multiples.
Example: sum_of_multiples(20,[3,4]) (-> [3,4,6,8,9,12,15,16,18]) -> 91
"""

def sum_of_multiples(limit, multiples):
    s=list()
    for i in range(limit):
        for j in multiples:
            try:
                if i % j == 0:
                    s.append(i)
                    break
            except:
                break

    return sum(s)