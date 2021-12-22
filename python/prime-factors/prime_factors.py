"""
Set Task: Compute the prime factors of a given natural number.
Method:
* We check for every number between i (int) and value (int), whether it is a factor of value, starting with i=2.
* Once a factor is found, it is saved in i. value is divided by i and we look for another factor, starting with i.
* The loop ends once i > value.
Example: factors(128) -> [2,2,2,2,2,2,2]
"""

def factors(value):
    res=list()
    i=2
    while i<=value:
        for j in range(i,value+1):
            if value%j==0:
                i=j
                res.append(j)
                value=int(value/j)
                break
    return res