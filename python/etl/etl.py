"""
Set task: Transform legacy_data (dict, each key is an int, each value a list of letters) to a new datastructure (dict, each key should be a letter, each value the corresponding int).
Method: We loop through legacy_data and nest a loop through the value list, saving each combination of key,value as value,key in the new dictionary.
Example: transform({1:["A","B"],2:["C","E"],3:["D"]}) -> {"a": 1, "b": 1, "c": 2, "d": 3, "e": 2}
"""

def transform(legacy_data):
    res=dict()
    for k,v in legacy_data.items():
        for i in range(len(v)):
            res[v[i].lower()]=k
    return res