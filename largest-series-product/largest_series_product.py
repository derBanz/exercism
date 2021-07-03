def largest_product(series, size):
    nums=slices(series,size)
    res=0
    for i in nums:
        curr_res=1
        for j in i:
            curr_res=curr_res*int(j)
        res=max(res,curr_res)
    return res

def slices(series, length):
    if length < 0 or length > len(series):
        raise ValueError("Bad boy.")
    res=list()
    for i in range(len(series)+1-length):
        res.append(series[i:i+length])
    return res