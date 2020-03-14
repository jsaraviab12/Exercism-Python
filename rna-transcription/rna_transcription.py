def to_rna(dna_strand):
    aux = {'A':'U', 'T': 'A', 'C': 'G', 'G':'C'}
    rna = ''

    for dna in dna_strand:
        rna += aux[dna]
    return rna
        