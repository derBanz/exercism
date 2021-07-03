from string import whitespace

def response(hey_bob):
    hey_bob=hey_bob.strip()

    if len(hey_bob)==0:
        return "Fine. Be that way!"

    question=hey_bob[-1]=="?"
    yelling=hey_bob.isupper()

    if question:
        if yelling==True:
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
    else:
        if yelling==True:
            return "Whoa, chill out!"
        else:
            return "Whatever."