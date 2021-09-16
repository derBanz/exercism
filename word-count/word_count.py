"""
Set Task: Given sentence (String), count the occurences of each word in that phrase.
Method:
* sentence is cleaned and split into s (list).
* Using regular expressions, each word in s is checked if it fits the approved schematics. If true it is added to words (dict) and, if it is there already, its value is incremented by one.
Example: count_words("\"That's the password: 'PASSWORD 123'!\", cried the Special Agent.\nSo I fled.")
(-> ['"that\'s', 'the', 'password:', "'password", '123\'!"', 'cried', 'the', 'special', 'agent.', 'so', 'i', 'fled.'])
-> ['"that\'s', 'the', 'password:', "'password", '123\'!"', 'cried', 'the', 'special', 'agent.', 'so', 'i', 'fled.']
"""

import re

def count_words(sentence):
    words=dict()
    s=sentence.lower().replace(","," ").replace("_"," ").split()
    print(s)
    c1=re.compile("[a-z]+'[a-z]+")
    c2=re.compile("[a-z]+")
    c3=re.compile("[0-9]+")

    for i in range(len(s)):
        w=s[i]
        if c1.search(w)!=None:
            r=c1.search(w).group()
        elif c2.search(w)!=None:
            r=c2.search(w).group()
        elif c3.search(w)!=None:
            r=c3.search(w).group()
        else:
            continue
        try:
            words[r]=words[r]+1
        except:
            words[r]=1

    return words