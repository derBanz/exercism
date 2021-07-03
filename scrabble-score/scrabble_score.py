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