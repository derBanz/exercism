"""
Set Task: Given number (int), determine if it is perfect, abundant, or deficient based on Nicomachus' classification scheme for positive integers.
Method:
* We validate number to make sure it is of type "int" and is greater than zero.
* We loop through all numbers until number and check, whether it is a factor of number. If true, it gets appended to factors (list).
* We remove number from factors, as it is not considered for the aliquot sum and compare the sum of factors with the number to determine the result.
Example: classify(28) (-> [1,2,4,7,14] -> 28) -> perfect
"""

def classify(number):
    if type(number) != int or number <= 0:
        raise ValueError("Only positive integers are allowed.")
    factors = list()
    for i in range(1,number+1):
        if number % i == 0 and i not in factors:
            factors.append(i)
    factors.remove(number)
    if sum(factors) > number:
        return "abundant"
    elif sum(factors) == number:
        return "perfect"
    return "deficient"