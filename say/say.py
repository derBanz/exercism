def ones(number):
    nums=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    if number < 0:
        raise ValueError
    try:
        return nums[number]
    except:
        return

def tens(number):
    nums=["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if number < 10:
        return ones(number)
    elif number < 20:
        return nums[number-10]
    else:
        if number%10==0:
            return nums[8+int(number/10)]
        return nums[8+int(number/10)]+"-"+ones(number%10)

def hundreds(number):
    hun=ones(int(number/100))
    if number < 100:
        return tens(number)
    elif number%100==0:
        return hun+" hundred"
    return hun+ " hundred "+tens(number%100)

def say(number):
    if number > 999999999999 or number < 0:
        raise ValueError("Number is outside the allowed limits 0-999,999,999,999")
    numstring=str(number)
    numlist=list()
    sizes=["thousand", "million", "billion", "trillion", "quadrillion"]
    res=""
    while len(numstring)>0:
        numlist.append(int(numstring[-3::]))
        numstring=numstring[:-3:]
    numlist.reverse()
    for i in range(len(numlist)-1):
        if numlist[i]!=0:
            res+=hundreds(numlist[i])+" "+sizes[len(numlist)-i-2]+" "
    if numlist[-1]!=0 or number==0:
        res+=hundreds(numlist[-1])

    return res.strip()