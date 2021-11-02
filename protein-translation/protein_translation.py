"""
Set Task: Given strand (String), translate it to the containing proteins.
Method:
* acids (dict) contains all proteins as keys with the respective codons contained in a tuple as the corresponding values.
* Going through slices of 3 we compare to find the correct acid and attach it to prot (list).
* Once we ran through strand or encounted a "Stop" codon we return prot.
Example: proteins("AUGUUUUCUUAAAUG") -> ['Methionine', 'Phenylalanine', 'Serine']
"""

acids = {
    "Methionine": ("AUG"),
    "Phenylalanine": ("UUU","UUC"),
    "Leucine": ("UUA","UUG"),
    "Serine": ("UCU","UCC","UCA","UCG"),
    "Tyrosine": ("UAU","UAC"),
    "Cysteine": ("UGU","UGC"),
    "Tryptophan": ("UGG"),
    "Stop": ("UAA","UAG","UGA")
}

def proteins(strand):
    prot = list()
    stop = False
    while len(strand) > 2 and not stop:
        codon = strand[:3:]
        strand = strand[3::]
        for k,v in acids.items():
            if codon in v:
                if k == "Stop":
                    stop = not stop
                else:
                    prot.append(k)
                break

    return prot