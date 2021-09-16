"""
Set Task: Given series (String) and length (int), output all the contiguous substrings of length in series.
Method: Going through each slice of size length, the resulting slice is appended to res (list).
Example: slices("159765",4) -> ["1597","5976","9765"]
"""

def slices(series, length):
    if length < 1 or length > len(series):
        raise ValueError("Bad boy.")
    res=list()
    for i in range(len(series)+1-length):
        res.append(series[i:i+length])
    return res