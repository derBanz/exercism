def find_anagrams(word, candidates):
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
    return res