def decode(string):
    res=""
    count=""
    for s in string:
        try:
            int(s)
            count+=s
        except:
            if count=="":
                res+=s
            else:
                res+=int(count)*s
            count=""
    return res


def encode(string):
    count=0
    char=""
    res=""
    for s in string:
        if s!=char and char!="":
            if count==1:
                res+=char
            else:
                res+=(str(count)+char)
            char=s
            count=1
        else:
            char=s
            count+=1
    if count==1:
        return res+char
    elif count>1:
        return res+str(count)+char
    return ""