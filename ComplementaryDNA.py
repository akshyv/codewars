# convert A to T, T to A ,C to G and G to C in string
# %%
# my sol


import string


def DNA_strand(dna):
    for i in dna:
        if i == 'A':
            dna = dna.replace(i, 't')
        elif i == 'T':
            dna = dna.replace(i, 'a')
        elif i == 'G':
            dna = dna.replace(i, 'c')
        elif i == 'C':
            dna = dna.replace(i, 'g')
    return(dna.upper())

# %%
# sol 1


def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG", "TAGC"))
# %%
# sol 2 - best sol for me


pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}


def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])
