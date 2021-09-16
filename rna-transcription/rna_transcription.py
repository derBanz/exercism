"""
Set Task: Given dna_strand (String), return the corresponding rna_strand (String).
Method: Each character is checked individually and the correctly corresponding RNA-character added to rna_strand.
Example: to_rna("ACGTGGTCTTAA") -> "UGCACCAGAAUU"
"""

def to_rna(dna_strand):
    rna_strand=""
    for x in dna_strand:
        if x=="G":
            rna_strand+="C"
        elif x=="C":
            rna_strand+="G"
        elif x=="T":
            rna_strand+="A"
        elif x=="A":
            rna_strand+="U"
        else:
            rna_strand+=x
    return rna_strand
