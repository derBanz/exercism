def is_pangram(sentence):
    helper=[0 for x in range(26)]
    allowed="abcdefghijklmnopqrstuvwxyz"
    for s in sentence.lower():
        if s in allowed:
            helper[allowed.find(s)]+=1
    return sorted(helper)[0]>0

print(is_pangram('"Five quacking Zephyrs jolt my wax bed."'))