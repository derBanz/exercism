"""
Set Task: Given number (int) between 0 and 999,999,999,999, spell out that number in English.
Method:
* The main function say calls on three anxilliary functions ones, tens and hundreds.
** ones returns the writeout of numbers between 0 and 9.
** tens returns the writeout of numbers between 0 and 99, calling on ones.
** hundreds returns the writeout of numbers between 0 and 999, calling on tens.
* say breaks up number into chunks of three digits starting at the end and appends those to numlist (list).
* numlist then gets reversed. The length of numlist defines the dimension of the first and each following list item.
* Each individual list item gets called with hundreds and its respective dimension drawn from sizes (list).
Example: say(1224936597) (-> [597,936,224,1] -> [1,224,936,597]) -> "one billion two hundred twenty-four million nine hundred thirty-six thousand five hundred ninety-seven"
"""

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

print(say(1224936597))