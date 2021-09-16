"""
Set Task: Given string (String), implement run-length encoding and decoding.
Method:
* Encoding:
** We go through every character of string. If it is the same as the previous character OR the first character, we save it in char (String) and increment count (int) by one.
** If the character is not the same as the previous character, the previous character and its count are added to res (String).
** At the end of the loop, the last character and its count are added and res is returned.
* Decoding:
** We go through every character of the encoded string. We try and convert the current character to int. If that is successful, we add s to count (String).
** If the current character cannot be converted to int and count is empty, we add the current character once to res (String). If there is a count, we convert it to int and add count times the current character to res.
Example:
* encode("AABCCCDEEEE") -> "2AB3CD4E"
* decode("2AB3CD4E") -> "AABCCCDEEEE"
"""

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