"""
Set task: Given a number n (int), determine what the nth prime is.
Method: 
* First, an upper boundary is approximated using n*ln(n)+n*ln(ln(n)) > pn, with pn being the nth-prime (see https://math.stackexchange.com/questions/1257/is-there-a-known-mathematical-equation-to-find-the-nth-prime).
* For n < 6 this formula is not valid and the upper boundary is set to 12.
* Using the "Sieve of Eratosthenes" algorithm, the primes in the range of 1 < p < n*ln(n)+n*ln(ln(n)) are determined and stored in primes (list).
* The nth prime is returned from primes.
Example: prime(13) (-> p = 45 -> primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]) -> 41
"""

from math import log

def prime(number):
    if number < 1:
        raise ValueError("Index out of range")
    elif number < 6:
        p = 12
    else:
        p = int(number * log(number) + number * log(log(number)))
    nums = [x for x in range(2,p)]
    primes = list()
    while len(nums) > 0:
        num = nums[0]
        primes.append(num)
        j = 0
        while j < len(nums):
            if nums[j] % num == 0:
                nums.pop(j)
            else:
                j += 1
    try:
        return primes[number-1]
    except:
        raise ValueError("Index out of range")