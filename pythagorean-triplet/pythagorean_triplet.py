def triplets_with_sum(number):
    res = list()
    for a in range(1,int(number / 3)):
        for b in range(a, int((number - a) / 2)+1):
            c = number - a - b
            if a ** 2 + b ** 2 == c ** 2:
                res.append([a, b, c])
    return res