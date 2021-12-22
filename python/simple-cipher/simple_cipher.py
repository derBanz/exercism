"""
Set Task: Implement a simple cipher including an optional key (String). If no key is provided use a random key.
Method:
* On init, if no key was provided a random 100 character key is generated.
* On encode and decode, each character is shifted by the appropriate key's character position in self.dict (dict).
Example:
* C = Cipher("abcd")
* C.encode("iamapandabear") -> "ibodpbpgacgdr"
* C.decode("ibodpbpgacgdr") -> "iamapandabear"
"""

from random import randrange

class Cipher:
    def __init__(self, key=None):
        self.dict = "abcdefghijklmnopqrstuvwxyz"
        if key == None:
            self.key = ""
            for i in range(100):
                self.key += self.dict[randrange(26)]
        else:
            self.key = key

    def encode(self, text):
        res = ""
        i = 0
        j = 0
        while i < len(text):
            try:
                res += self.dict[self.dict.find(text[i]) + self.dict.find(self.key[j])]
            except:
                res += self.dict[self.dict.find(text[i]) + self.dict.find(self.key[j]) - 26]
            j = (j + 1) % len(self.key)
            i += 1
        return res

    def decode(self, text):
        res = ""
        i = 0
        j = 0
        while i < len(text):
            try:
                res += self.dict[self.dict.find(text[i]) - self.dict.find(self.key[j])]
            except:
                res += self.dict[self.dict.find(text[i]) - self.dict.find(self.key[j]) + 26]
            j = (j + 1) % len(self.key)
            i += 1
        return res