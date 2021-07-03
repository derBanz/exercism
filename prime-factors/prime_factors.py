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