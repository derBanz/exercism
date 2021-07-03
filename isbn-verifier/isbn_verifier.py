def is_valid(isbn):
    isbn=isbn.replace("-","")
    result=0
    for x in range(len(isbn)):
        try:
            if isbn[x]=="X" and x==9:
                result+=(10-x)*10
            else:
                result+=(10-x)*int(isbn[x])
        except:
            return False
    return result%11==0 and len(isbn)==10

print(is_valid("3-598-21518-8"))