from math import log

def prime(number):
    if number < 1:
        raise ValueError("Index out of range")
    elif number < 6:
        p = 12
    else:
        p = int(number * log(number) + number * log(log(number)))
    print(p)
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