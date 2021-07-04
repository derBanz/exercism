"""
Set task: Given a series (String), calculate the largest product for a contiguous substring of digits of length size (int).
Method: 
* If the substringsize is either negative or larger than the series itself, an exception is raised.
* Iterating through series we save each possible substring into nums (list).
* Iterating through nums we save the product of each substring's digits if it is bigger than the current save.
Example: largest_product("1027839564",3) (-> ["102","027","278","783","839","395","956","564"]) -> 270
"""

def largest_product(series, size):
    if size < 0 or size > len(series):
        raise ValueError("Bad boy.")
    nums=list()
    for i in range(len(series)+1-size):
        nums.append(series[i:i+size])
    res=0
    for i in nums:
        curr_res=1
        for j in i:
            curr_res=curr_res*int(j)
        res=max(res,curr_res)
    return res