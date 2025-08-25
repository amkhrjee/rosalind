from Bio import SeqIO

seqs = []
for record in SeqIO.parse("./datasets/rosalind_lcsm.txt", "fasta"):
    seqs.append(record.seq)

shortest = min(seqs, key=lambda x: len(x))

rest_of_seqs = [x for x in seqs if x != shortest]


for i in reversed(range(len(shortest) + 1)):
    for j in range(len(shortest) - i + 1):
        not_found = False
        pattern = shortest[j : j + i]
        for seq in rest_of_seqs:
            if seq.find(pattern) == -1:
                not_found = True
                break
        if not_found:
            continue
        else:
            print(pattern)
            exit(1)
