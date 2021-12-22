"""
Set Task: Given number (int), return the roman numeral version of that number.
Method:
* We have two lists, ones (list) containing the roman numerals depicting powers of 10, fives (list) containing the remaining roman numerals.
* number is converted to a string and reversed, so that we start with the last digit.
* Going through each digit of number, four cases are checked to find the correct combination of letters from ones and fives.
* The resulting string is once again reversed to get the result.
Example: roman(134) (-> num="431" -> i=4, reversedRes="VI" -> i=3, reversedRes="VIXXX" -> i=1, reversedRes = "VIXXXC") -> CXXXIV
"""

def roman(number):
    ones=["I","X","C","M"]
    fives=["V","L","D"]
    reversedRes=list()
    res=""
    num=str(number)[::-1]
    for i in range(len(num)):
        if int(num[i]) == 4:
            reversedRes.append(ones[i]+fives[i])
        elif int(num[i]) == 9:
            reversedRes.append(ones[i]+ones[i+1])
        elif int(num[i]) >= 5:
            reversedRes.append(fives[i]+(int(num[i]) % 5)*ones[i])
        elif int(num[i]) > 0:
            reversedRes.append(int(num[i])*ones[i])
    for r in reversedRes[::-1]:
        res+=r
    return res