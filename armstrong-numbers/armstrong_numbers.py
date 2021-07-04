"""
Set task: A function which checks, whether a number (int) is an armstrong number (An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.)
Method:
* Go through each character of the number, raise it to the power of the length and sum them up.
* Return whether the sum is equal to the number.
Example: is_armstrong_number(153) (-> 1^3 + 5^3 + 3^3 = 153) -> True
"""

def is_armstrong_number(number):
    check=0
    number=str(number)
    for s in range(len(number)):
        check+=pow(int(number[int(s)]),len(number))
    return check==int(number)