"""
Set task: Given card_num (String) determine whether or not it is valid per the Luhn formula.
Method:
* The class removes spaces on init.
* The first check is, whether card_num is at least two characters long.
* The second check is whether the sum of digits is divisible by 10, while every second digit from the right is doubled. If the doubled digit is bigger than 9, 9 is subtracted from it.
* Any non-digit characters immediately fail the check for the sequence.
Example:
* L = Luhn("055 444 285") (-> "055444285")
* L.valid() (-> "015848275" -> 40) -> True
"""

class Luhn:
    def __init__(self, card_num):
        self.card_num=card_num.replace(" ","")

    def valid(self):
        check=0
        if len(self.card_num)<2:
            return False
        for s in range(len(self.card_num)):
            try:
                num=int(self.card_num[s])
                if len(self.card_num)%2==s%2:
                    num+=num
                    if len(str(num))==2:
                        num=int(str(num)[-1])+1
                check+=num
                print(num)
            except:
                return False
        return check%10==0