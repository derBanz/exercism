"""
Set Task: Given number (String), produce the pure digit phone number regardless of original format.
Method:
* Going through each character in number, if it can be converted to a digit it's added to self.number (String). This should now contain all digits of the original number.
* We make some checks that all requirements are met and define area_code, exchange_code and subscriber_number.
* In pretty() we concatanate it in the desired format.
Example:
* P = PhoneNumber("1.243-322-1337)
* P.pretty("(243)-322-1337")
"""

class PhoneNumber:
    def __init__(self, number):
        self.number = ""
        for c in number:
            try:
                int(c)
                self.number += c
            except:
                pass
        if self.number[0] == "1" and len(self.number) == 11:
            self.number = self.number[1::]
        if len(self.number) != 10 or int(self.number[0]) < 2 or int(self.number[3]) < 2:
            raise ValueError("Inapproproate input.")
        self.area_code = self.number[:3:]
        self.exchange_code = self.number[3:6:]
        self.subscriber_number = self.number[6::]

    def pretty(self):
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber_number}"