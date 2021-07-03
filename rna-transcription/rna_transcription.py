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
