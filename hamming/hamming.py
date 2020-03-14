def distance(strand_a, strand_b):
    hm = 0
    if len(strand_a)== len(strand_b):
        for i in range(len(strand_a)):
            if strand_a[i] != strand_b[i]:
                hm += 1
            i+=1
        return hm
    else:
        raise ValueError("The lengths of the strands are different")
