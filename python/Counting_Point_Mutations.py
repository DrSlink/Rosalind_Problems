# Problem
#
# Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t.
#
# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
#
# Return: The Hamming distance dH(s,t).
#
# Sample Dataset
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT
# Sample Output
# 7
import numpy as np
from rosalind_utils import load_dataset


def hamm(first, second):
    diff_count = 0
    for i in range(len(first)):
        if first[i] != second[i]:
            diff_count += 1
    return diff_count


if __name__ == "__main__":
    dataset = load_dataset('./../datasets/rosalind_hamm.txt').split('\n')
    print(hamm(dataset[0], dataset[1]))
