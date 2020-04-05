# Problem
# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
#
# The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
#
# Given: A DNA string s of length at most 1000 bp.
#
# Return: The reverse complement sc of s.

# Sample Dataset
# AAAACCCGGT
# Sample Output
# ACCGGGTTTT
from rosalind_utils import load_dataset


if __name__ == "__main__":
    dataset = load_dataset('./../datasets/rosalind_revc.txt')[:-1]
    complement = {"A": "T",
                  "C": "G",
                  "T": "A",
                  "G": "C"}
    comp_array = []
    for i in range(len(dataset)):
        comp_array.append(complement.get(dataset[len(dataset) - 1 - i]))
    delimiter = ''
    print(delimiter.join(comp_array))
