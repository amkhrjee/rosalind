from Bio import SeqIO

seqs = []
for record in SeqIO.parse("./datasets/rosalind_long.txt", "fasta"):
    seqs.append(record.seq)

purines = ["A", "G"]
pyrimidines = ["T", "C"]

# transition: purine -> purine and pyrimidine -> pyrimidine

n_transitions = 0
n_transversions = 0
for base_1, base_2 in zip(seqs[0], seqs[1]):
    if base_1 != base_2:
        if (base_1 in purines and base_2 in purines) or (
            base_1 in pyrimidines and base_2 in pyrimidines
        ):
            n_transitions += 1
        else:
            n_transversions += 1

print(n_transitions / n_transversions)
