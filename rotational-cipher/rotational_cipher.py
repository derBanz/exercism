def rotate(text, key):
    chars="abcdefghijklmnopqrstuvwxyz"
    res=""
    for s in text:
        if s in chars:
            res+=chars[(chars.index(s.lower())+key)%26]
        elif s in chars.upper():
            res+=chars[(chars.index(s.lower())+key)%26].upper()
        else:
            res+=s
    return res

print(rotate("O M G",5))