"""
Set task:
* A function to encrypt a plain_text (String) using the Atbash cipher, replacing each character with the opposite character in the alphabet and grouping them into chunks of five.
* A function to decrypt a ciphered_text (String) using the same Atbash cipher.
Method:
* Create a function replacer, that takes c (String) and returns the opposite character in the alphabet. If c is a number it returns the same number.
* The encoder function skips punctuation and spaces, manually inserts a space after every five characters and calls the replacer function to replace each character.
* The decoder function skips spaces and calls the replacer function to replace each character.
Example:
* encode("Testing,1 2 3, testing.") (-> "testing123testing") -> "gvhgr mt123 gvhgr mt"
* decode("gvhgr mt123 gvhgr mt") (-> "gvhgrmt123gvhgrmt") -> "testing123testing"
"""

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
        if c == " ":
            continue
        res += replacer(c)
    return res