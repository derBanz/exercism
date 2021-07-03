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