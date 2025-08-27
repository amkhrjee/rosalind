from Bio import SeqIO

seqs = []
for record in SeqIO.parse("./datasets/rosalind_sseq.txt", "fasta"):
    seqs.append(record.seq)

seq = seqs[0]
sseq = seqs[1]

idxs = [0]

for base_1 in sseq:
    for i, base_2 in enumerate(seq[idxs[-1] :]):
        if base_1 == base_2:
            idxs.append(i + 1 + idxs[-1])
            break

print(" ".join([str(x) for x in idxs[1:]]))
