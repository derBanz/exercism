"""
Set task: Calculate the hamming distance of two strands of equal length.
Method: We iterate through the strand length and compare each position with the appropriate position in the other strand and increment res (int) each time a difference is found.
Example: distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") -> 7
"""

def distance(strand_a, strand_b):
    if(len(strand_a)!=len(strand_b)):
        raise ValueError("Only compare strands of the same length.")
    else:
        res=0
        for r in range(len(strand_a)):
            res+=(strand_a[r]!=strand_b[r])
    return res