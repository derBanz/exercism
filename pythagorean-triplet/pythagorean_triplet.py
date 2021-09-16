"""
Set Task: Given N (int), find all triplets for which a + b + c = N.
Method:
* We check for every combination of a, b, c (int) if a^2+b^2=c^2.
* if that is the case, [a,b,c] is appended to res (list).
Example: triplets_with_sum(1000) -> [[200, 375, 425]]
"""

def triplets_with_sum(number):
    res = list()
    for a in range(1,int(number / 3)):
        for b in range(a, int((number - a) / 2)+1):
            c = number - a - b
            if a ** 2 + b ** 2 == c ** 2:
                res.append([a, b, c])
    return res

print(triplets_with_sum(1000))