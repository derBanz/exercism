"""
Set Task: Given limit (int), implement the Sieve of Eratosthenes algorithm.
Method:
* We start with p (list) as an empty result list and nums (list) containing all numbers between 2 and limit.
* We start an infinite loop and look at the first entry of nums. This digit is added to p. The digit and all its multiples are removed from nums.
* Once nums is empty the loop breaks and p is returned.
Example: primes(100) -> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
"""

def primes(limit):
    p=list()
    nums=[x for x in range(2,limit+1)]
    while True:
        try:
            n=nums[0]
            p.append(n)
            for i in range(int(len(nums)/n+2)):
                try:
                    nums.remove(i*n)
                except:
                    pass             
        except:
            break
    return p

print(primes(100))