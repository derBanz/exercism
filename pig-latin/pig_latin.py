def translate(text):
    vowels=["a","e","i","o","u"]
    consonants=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    res=""
    text=text.split(" ")
    for word in text:
        if word[:2:] in ["xr","yt"]:
            res+=word+"ay "
        elif word[0].lower() in consonants:
            j=0
            for i in range(len(word)):
                if word[i] in vowels or (word[i]=="y" and i > 0):
                    j=i
                    break
            if word[j-1:j+1:]=="qu":
                res+=word[j+1::]+word[:j+1:]+"ay "
            else:
                res+=word[j::]+word[:j:]+"ay "
        elif word[0].lower() in vowels:
            res+=word+"ay "

    return res.strip()

print(translate("chair"))