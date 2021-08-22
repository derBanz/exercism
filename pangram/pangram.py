"""
Set task: Determine if a sentence (String) is a pangram. A pangram is a sentence using every letter of the alphabet at least once.
Method:
* helper (list) is defined with 26 entries of "0".
* allowed (String) is defined as a string containing the whole alphabet.
* Each character in sentence is checked for its position in allowed. The corresponding entry in helper is incremented by 1.
* In the end we check that the smallest entry in helper is greater than zero.
Example: is_pangram('"Five quacking Zephyrs jolt my wax bed."') (-> helper = [2, 1, 1, 1, 3, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1]) -> True
"""

def is_pangram(sentence):
    helper=[0 for x in range(26)]
    allowed="abcdefghijklmnopqrstuvwxyz"
    for s in sentence.lower():
        if s in allowed:
            helper[allowed.find(s)]+=1
    return sorted(helper)[0]>0