"""
Set task: Given input_string (String) verify all brackets are matches & nested.
Method:
* brackets (dict) contains opening brackets as values for the closing brackets.
* opened (list) is defined empty.
* Going through each char (String) in input_string, append opening brackets to
    opened. When encountering a closing bracket, compare with the most recent
    opening bracket in opened. If they match, carry on, otherwise return False.
* If input_string was computed successfully, make sure no opening brackets are
    left in opened.
Example: is_paired("{()]") -> False
"""


def is_paired(input_string):
    opened = list()
    brackets = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    for char in input_string:
        try:
            if char in brackets.values():
                opened.append(char)
            elif char in brackets.keys() and opened.pop() != brackets[char]:
                return False
        except:
            return False
    return len(opened) == 0
