# Problem
# After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.
#
# Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.
#
# Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)
#
# Sample Dataset
# >Rosalind_10
# ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
# >Rosalind_12
# ATCGGTCGAA
# >Rosalind_15
# ATCGGTCGAGCGTGT
# Sample Output
# MVYIADKQHVASREAYGHMFKVCA
from rosalind_utils import load_dataset
DNA_CODON_TABLE = {
    'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V',
    'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V',
    'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V',
    'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V',
    'TCT': 'S', 'CCT': 'P', 'ACT': 'T', 'GCT': 'A',
    'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D',
    'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'TAA': '-', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'TAG': '-', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G',
    'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'TGA': '-', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}


def result(lines):
    result = ''

    # lines = s.split()
    dna = lines[0]
    introns = lines[1:]

    for intron in introns:
        dna = dna.replace(intron, '')

    for i in range(0, len(dna), 3):
        codon = dna[i:i + 3]

        protein = None
        if codon in DNA_CODON_TABLE:
            protein = DNA_CODON_TABLE[codon]

        if protein == '-':
            break

        if protein:
            result += protein

    return ''.join(list(result))


if __name__ == "__main__":
    # small_dataset = """
    #                 ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
    #                 ATCGGTCGAA
    #                 ATCGGTCGAGCGTGT
    #                 """
    # large_dataset = open('datasets/rosalind_splc.txt').read().strip()
    dataset = load_dataset('./../datasets/rosalind_splc.txt')[1:-1].split('>')
    new_dataset = []
    for elem in dataset:
        new_dataset.append(''.join(elem.split()[1:]))
    print(result(new_dataset))