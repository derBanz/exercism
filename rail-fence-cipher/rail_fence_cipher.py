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
