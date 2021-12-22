"""
Set task: Determine if string (String) is an isogram, meaning no letter of the alphabet is used more than once.
Method:
* We create letters (dict) of all letters being set as zero initially.
* We iterate through string and update the appropriate letter's value in letters.
* We return, whether or not the maximum value in letters.values is smaller or equal to one.
Example: is_isogram("hello") (-> {"a":0, "b":0,...,"e":1,...,"h":1,...,"l":2,...,"o":1} -> 2) -> False
"""

def is_isogram(string):
    letters={}
    for a in "abcdefghijklmnopqrstuvwxyz":
        letters.update({a: 0})
    for s in string.lower():
        try:
            letters.update({s: letters.get(s)+1})
        except:
            pass
    return max(letters.values()) <= 1