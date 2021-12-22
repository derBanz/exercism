"""
Set task: Program specific responses depending on hey_bob (String) being a question and/or yelled.
Method: Check hey_bob for being empty. Check, if the last character is a question mark, and check if hey_bob is in all-caps.
Example:
* response("HEY.") (-> question == False, yelling == True) -> "Whoa, chill out!"
* response("How you doing?") (-> question == True, yelling == False) -> "Sure."
"""

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