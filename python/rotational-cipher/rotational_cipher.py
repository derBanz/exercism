"""
Set Task: Given text (String) and key (int), create an implementation of the rotational cipher.
Method: Going through each char from text, it is moved by key amount of letters. The new char is appended to res (String).
Example: rotate("Hello World",6) -> "Nkrru Cuxrj"
"""

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