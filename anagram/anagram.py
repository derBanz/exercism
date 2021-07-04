"""
Set task: A function to determine, which of the candidates (list) are a valid anagram of the word (String).
Method:
* We have word_dict (dictionary) and can_dict (list of dictionaries, one per candidate). Each dictionary is initialized with one entry per letter in the alphabet and the count "0".
* We go through the word and each candidate and increment each letter's count by "1" in the respective dictionary.
* We compare the each dictionary in can_dict with word_dict. If one is equal, the corresponding candidate is a valid acronym of the word.
Example: find_anagrams("master", ["stream", "pigeon", "maters"]) (-> {"a":1, "b":0,...,"e":1,...,"z":0}, [{"a":1,...},{"a":0,...},{...}] ) -> ["stream", "maters"]
"""

def find_anagrams(word, candidates): #
    word_dict=dict() 
    can_dict=list()
    for i in range(len(candidates)): 
        can_dict.append(dict())
    res=list()
    for i in "abcdefghijklmnopqrstuvwxyz": 
        word_dict[i]=0
        for j in range(len(candidates)):
            can_dict[j][i]=0
    for i in word.replace(" ","").lower():
        word_dict[i]+=1
    for c in range(len(candidates)):
        w=candidates[c].replace(" ","").lower()
        for i in w:
            can_dict[c][i]+=1
        if can_dict[c]==word_dict and word.lower()!=w:
            res.append(candidates[c])
    print(word_dict)
    print(can_dict)
    return res

find_anagrams("master", ["stream", "pigeon", "maters"])