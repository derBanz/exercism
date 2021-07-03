def primes(limit):
    p=list()
    nums=[x for x in range(2,limit+1)]
    while True:
        try:
            n=nums[0]
            p.append(n)
            for i in range(len(nums)+1):
                try:
                    nums.remove(i*n)
                except:
                    pass                    
        except:
            break
    return p