"""
Set Task: Implement encoding and decoding for the rail fence cipher.
Method:
* When encoding we create ls (list) with as many entries as there are rails (int).
* down (bool) controls whether we got up or down the rails at any given moment.
* We go through each character of message (String) and add it to ls on the index (int) of the corresponding rail. Index gets increased/decreased according to down.
* When we hit an outer rail, down gets reversed and the index starts decreasing/increasing accordingly.
* When decoding, we first establish the fence setup. The same algorithm is used as for encoding, instead of concatanating string ls_count (list) is filled with integers in each position to indicate the number of characters there will be.
* encoded_message (String) is split according to the character numbers determined in the previous step.
* The same algorithm is repeated in reverse to put together the original message.
Example:
* encode("We are discovered - flee at once!",3) (-> ['Wrivdf o!', 'eaedsoee  lea ne', '  cr-etc']) -> "Wrivdf o!eaedsoee  lea ne  cr-etc"
* decode("Wrivdf o!eaedsoee  lea ne  cr-etc",3) (-> [9, 16, 8] -> ['Wrivdf o!', 'eaedsoee  lea ne', '  cr-etc']) -> "We are discovered - flee at once!"
"""

def encode(message, rails):
    ls = list()
    down = False
    index = 0
    for i in range(rails):
        ls.append("")
    for i in range(len(message)):
        ls[index] += message[i]
        if index == 0 or index == rails - 1:
            down = not down
        if down:
            index += 1
        else:
            index -= 1
    res = ""
    for i in ls:
        res += i

    return res


def decode(encoded_message, rails):
    ls_count = list()
    ls = list()
    down = False
    index = 0
    message_length = len(encoded_message)
    for i in range(rails):
        ls_count.append(0)
    for i in range(message_length):
        ls_count[index] += 1
        if index == 0 or index == rails - 1:
            down = not down
        if down:
            index += 1
        else:
            index -= 1
    for i in range(rails):
        ls.append(encoded_message[:ls_count[i]:])
        encoded_message = encoded_message[ls_count[i]::]
    res = ""
    down = False
    index = 0
    for i in range(message_length):
        res += ls[index][0]
        ls[index] = ls[index][1::]
        if index == 0 or index == rails - 1:
            down = not down
        if down:
            index += 1
        else:
            index -= 1
    return res