"""
Set task: Given binary_str (String) convert it to the appropriate sequence of
          events for a secret handshake.
Method: Looping through binary_str in reverse, when encountering a 1 append the
        appropriate command to res (list).
        After the loop the first character is checked, and the list reversed if
        required.
Example: commands('10101') -> ['close your eyes', 'wink']
"""


def commands(binary_str):
    res = list()
    command = [
        "wink",
        "double blink",
        "close your eyes",
        "jump",
    ]
    for i in range(4):
        if int(binary_str[4 - i]):
            res.append(command[i])
    else:
        if int(binary_str[0]):
            res.reverse()
    return res
