def transform(legacy_data):
    res=dict()
    print(legacy_data)
    for k,v in legacy_data.items():
        for i in range(len(v)):
            res[v[i].lower()]=k
    return res