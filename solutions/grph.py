from Bio import SeqIO

k = 3  # overlap length
seqs = []
for record in SeqIO.parse("./datasets/rosalind_grph.txt", "fasta"):
    seqs.append((record.id, record.seq))


def does_overlap(s, t):
    if s[-k:] == t[:k]:
        return True
    return False


edges = []

for i, seq_1 in enumerate(seqs):
    for seq_2 in seqs[i + 1 :]:
        if does_overlap(seq_1[1], seq_2[1]):
            edges.append((seq_1[0], seq_2[0]))
        if does_overlap(seq_2[1], seq_1[1]):
            edges.append((seq_2[0], seq_1[0]))

for e in edges:
    print(f"{e[0]} {e[1]}")
