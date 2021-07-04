"""
Set task: Transorm an iterable (list) which may contain multiple nested lists into a simple list involving no nestings.
Method:
* iterlist (list) is defined as a helper and originally filled with iter(iterable).
* In an infinite loop we check the next value in the last entry of iterlist.
** If it is None it is ignored.
** If it can be iterated, iter(next value) is appended to the iterlist.
** Else it is appended to the result list res (list).
* If the last entry of iterlist has been iterated through completely it is removed from iterlist.
* Once iterlist is empty the result list is returned.
Example: flatten([1,2,[3,[4,5],[6,7,[8,9]]]]) -> [1,2,3,4,5,6,7,8,9]
"""

def flatten(iterable):
    res=list()
    iterlist=list()
    try:
        iterlist.append(iter(iterable))
    except:
        ValueError("Input not an iterable.")
    while True:
        try:
            check=next(iterlist[-1])
            if check==None:
                continue
            try:
                iterlist.append(iter(check))
            except TypeError:
                res.append(check)
        except StopIteration:
            iterlist.pop()
        
        if len(iterlist)==0:
            break
    return res