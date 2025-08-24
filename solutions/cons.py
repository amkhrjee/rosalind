from Bio import SeqIO

seqs = []
for record in SeqIO.parse("./datasets/rosalind_cons.txt", "fasta"):
    seqs.append(list(record.seq))

n_bases = len(seqs[0])
profile = {
    "A": [0] * n_bases,
    "C": [0] * n_bases,
    "G": [0] * n_bases,
    "T": [0] * n_bases,
}

for seq in seqs:
    for i, base in enumerate(seq):
        profile[base][i] += 1

cons = ""
for i in range(n_bases):
    cons += max([(k, v[i]) for k, v in profile.items()], key=lambda x: x[1])[0]

print(cons)

for k, v in profile.items():
    print(f"{k}: {' '.join([str(x) for x in v])}")
