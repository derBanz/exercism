"""
Set task: Check a given isbn (String) whether or not it fulfills the standard isbn format.
Method:
* The isbn's hyphens are removed.
* Iterating through the isbn, each number is multiplied with an index-depending factor and added to res (int).
* If a character is an "X" and it is in the tenth position of the isbn, it is treated as a 10.
* If a character is not a number and does not fulfill the previous criterium, the isbn is rejected.
* After all characters have been checked the result is True only if res is divisible by eleven and the isbn has 10 characters.
Example: is_valid("3-598-21518-8") -> False
"""

def is_valid(isbn):
    isbn=isbn.replace("-","")
    res=0
    for x in range(len(isbn)):
        try:
            if isbn[x]=="X" and x==9:
                res+=(10-x)*10
            else:
                res+=(10-x)*int(isbn[x])
        except:
            return False
    return res%11==0 and len(isbn)==10