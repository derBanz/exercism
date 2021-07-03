def slices(series, length):
    if length < 1 or length > len(series):
        raise ValueError("Bad boy.")
    res=list()
    for i in range(len(series)+1-length):
        res.append(series[i:i+length])
    return res