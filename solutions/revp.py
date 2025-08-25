from Bio import SeqIO

for record in SeqIO.parse("./datasets/rosalind_revp.txt", "fasta"):
    seq = record.seq
    break

complements = {"A": "T", "T": "A", "G": "C", "C": "G"}


def reverse_palindrome(seq):
    return ("".join([complements[x] for x in seq]))[::-1]


for i in range(4, 12 + 1):
    for j in range(len(seq) - i + 1):
        subseq = seq[j : j + i]
        if subseq == reverse_palindrome(subseq):
            print(f"{j + 1} {i}")
