def square_of_sum(number):
    return pow(sum(range(number+1)),2)

def sum_of_squares(number):
    res=0
    for i in range(number+1):
        res+=pow(i,2)
    return res

def difference_of_squares(number):
    return abs(square_of_sum(number)-sum_of_squares(number))
