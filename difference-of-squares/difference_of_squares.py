"""
Set task: Find the difference between the square of the sum and the sum of the squares of the first number (int) natural numbers.
Method: Both the square of the sum of the first number natural numbers and the sum of the squares of the first number natural numbers are calculated and substracted from each other.
Example: difference_of_squares(10) (-> (1+2+3+...+10)^2 = 55^2 = 3025 -> (1^2+2^2+...+10^2) = 385) -> 2640
"""

def square_of_sum(number):
    return pow(sum(range(number+1)),2)

def sum_of_squares(number):
    res=0
    for i in range(number+1):
        res+=pow(i,2)
    return res

def difference_of_squares(number):
    return abs(square_of_sum(number)-sum_of_squares(number))
