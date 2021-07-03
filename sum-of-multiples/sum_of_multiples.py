def sum_of_multiples(limit, multiples):
    s=list()
    for i in range(limit):
        for j in multiples:
            try:
                if i % j == 0:
                    s.append(i)
                    break
            except:
                break

    return sum(s)
