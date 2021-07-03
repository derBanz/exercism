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

c = Cipher("zzz")
print(c.encode("iamapandabear"))