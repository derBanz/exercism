def flatten(iterable):
    res=list()
    iterlist=list()
    try:
        iterlist.append(iter(iterable))
    except:
        ValueError("Input not an iterable.")
    curr_iter=""
    while True:
        try:
            check=next(iterlist[-1])
            if check==None:
                continue
            #print(check)
            try:
                iterlist.append(iter(check))
                #print("Iterlist: ",iterlist)
                #print("Result: ",res)
            except TypeError:
                #print("Not an iterable")
                res.append(check)
                #print("Result: ",res)
        except StopIteration:
            #print("Iteration ended.")
            iterlist.pop()
            #print("Iterlist: ",iterlist)
            #print("Result: ",res)
        
        if len(iterlist)==0:
            break
    return res