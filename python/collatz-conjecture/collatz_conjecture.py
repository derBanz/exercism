"""
Set task: Given number (int), return the numbers of steps required to reach '1'
    following the steps of the Collatz Conjecture.
Method:
* Number is checked to be a positive integer.
* In an infinite loop, number is checked to be even or odd.
* Once number == 1 the amount of steps is returned.
Example: steps(12) -> 9
"""


def steps(number):
    steps = 0
    if type(number) != int or number < 1:
        raise ValueError("Input has to be a positive integer.")
    while True:
        if number == 1:
            return steps
        if number % 2:
            number = 3 * number + 1
        else:
            number = number / 2
        steps += 1
