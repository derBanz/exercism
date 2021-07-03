def distance(strand_a, strand_b):
    if(len(strand_a)!=len(strand_b)):
        raise ValueError("Only compare strands of the same length.")
    else:
        ham=0
        for r in range(len(strand_a)):
            ham+=(strand_a[r]!=strand_b[r])
    return ham