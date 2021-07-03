import re

def count_words(sentence):
    words=dict()
    s=sentence.lower().replace(","," ").replace("_"," ").split()
    print(s)
    c1=re.compile("[a-z]+'[a-z]+")
    c2=re.compile("[a-z]+")
    c3=re.compile("[0-9]+")

    for i in range(len(s)):
        print(i)
        w=s[i]
        print(w)
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

print(count_words("\"That's the password: 'PASSWORD 123'!\", cried the Special Agent.\nSo I fled."))