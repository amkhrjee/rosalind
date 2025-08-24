from Bio import SeqIO

seqs = {}
for record in SeqIO.parse("./datasets/rosalind_gc.txt", "fasta"):
    seqs[record.id] = record.seq


def gc(seq):
    total = len(seq)
    seq_list = list(seq)
    gs = seq_list.count("G")
    cs = seq_list.count("C")
    return ((gs + cs) / total) * 100


print(max([(gc(seq), id) for id, seq in seqs.items()], key=lambda x: x[0]))
