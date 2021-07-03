def abbreviate(words):
    acronym=""
    words=words.split()
    print(words)
    for w in words:
        print(w)
        if "-" in w and len(w)>1:
            acronym+=w[0].upper()
            acronym+=w[w.find("-")+1].upper()
            continue
        for i in range(len(w)):
            print(w[i])

            if w[i].lower() in "abcdefghifjklmnopqrstuvwxyz":
                acronym+=w[i].upper()
                break
    return acronym

print(abbreviate("Hello World"))