"""
Set Task: Given word (String), compute the Scrabble score for that word.
Method:
* Going through each character of word, it is added to letters (dict) and, if it is already in letters, its value is incremented by one.
* In the end each letter is compared to values (dict) and its corresponding score multiplied with the occurences and added to word_value (int).
Example: score("banana") (-> {b:1,a:3,n:2}) -> 8
"""

def score(word):
    letters=dict()
    values={
        "a,e,i,o,u,l,n,r,s,t": 1,
        "d,g": 2,
        "b,c,m,p": 3,
        "f,h,v,w,y": 4,
        "k": 5,
        "j,x": 8,
        "q,z": 10
    }
    word_value=0
    for s in word.lower():
        try:
            letters[s]=letters[s]+1
        except:
            letters[s]=1

    for kl,vl in letters.items():
        for kv,vv in values.items():
            if kl in kv:
                word_value+=vl*vv


    return word_value