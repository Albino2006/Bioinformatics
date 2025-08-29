import dna; 

def base_counter(dna):
    a = 0
    t = 0
    g = 0
    c = 0
    n = 0

    for base in dna: 
        if base == 'G': 
            g += 1
        elif base == 'T':
            t += 1
        elif base == 'C':
            c += 1
        elif base == 'A':
            a += 1
        elif base == 'N':
            a += 1
    return f"Die Anzahl der Einzelnen Basen beläuft sich auf A: {a}, T: {t}, G: {g}, C: {c}, N: {n}"

def gc_counter(dna): 
    
    gc_count = 0; 
    for base in dna: 
        if base == 'G' or base == 'C': 
            gc_count += 1
    return gc_count/len(dna) * 100

def dna_rna_conv(dna): 
    return dna.replace('T', 'U')


def reverse_dna(dna): 
    complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C', 'N':'N'}
    reverse = [complement[base] for base in reversed(dna)]

    return ''.join(reverse)

