def is_isogram(string):
    result={}
    for a in "abcdefghijklmnopqrstuvwxyz":
        result.update({a: 0})
    for s in string.lower():
        try:
            result.update({s: result.get(s)+1})
        except:
            pass
    if sorted(result.values(), reverse=True)[0]>1:
        return False
    return True