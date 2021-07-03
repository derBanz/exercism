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
            except:
                return False
        return check%10==0