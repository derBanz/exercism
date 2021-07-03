def total(basket):
    bookDict={}
    price=800
    total=0
    disc2=0.95*2
    disc3=0.9*3
    disc4=0.8*4
    disc5=0.75*5
    for x in sorted(basket):
        try:
            bookDict[x]+=1
        except:
            bookDict[x]=1
    books=sorted([bookDict[x] for x in bookDict.keys()])
    print(books)
    if len(books)==1:
        total=price*books[0]
    elif len(books)==2:
        total=price*(disc2*books[0]+(books[1]-books[0]))
    elif len(books)==3:
        total=price*(disc3*books[0]+disc2*(books[1]-books[0])+(books[2]-books[1]))
    elif len(books)==4:
        total=price*(disc4*books[0]+disc3*(books[1]-books[0])+disc2*(books[2]-books[1])+(books[3]-books[2]))
    elif len(books)==5:
        total=2*books[1]
        if books[0]==books[1] and books[2]>=books[1]:
            total=price*(disc5*(2*books[1]-books[2])+disc4*2*(books[2]-books[1])+disc2*(books[3]-books[2])+(books[4]-books[3]))
        else:
            total=price*(disc5*books[0]+disc4*(books[1]-books[0])+disc3*(books[2]-books[1])+disc2*(books[3]-books[2])+(books[4]-books[3]))
    return round(total)

print(total([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5]))