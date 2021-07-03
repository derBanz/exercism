def replacer(c):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    if c in alphabet:
        return alphabet[::-1][alphabet.index(c)]
    return c

def encode(plain_text):
    res = ""
    i = 0
    for c in plain_text.lower():
        if c in "., ":
            continue
        if i % 5 == 0 and i > 0:
            res += " "
        i += 1
        res += replacer(c)
    return res


def decode(ciphered_text):
    res=""
    for c in ciphered_text.lower():
        if c in "., ":
            continue
        res += replacer(c)
    return res