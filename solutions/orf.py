import re

from Bio import SeqIO

codon_table = {
    "UUU": "F",
    "UUC": "F",
    "UUA": "L",
    "UUG": "L",
    "CUU": "L",
    "CUC": "L",
    "CUA": "L",
    "CUG": "L",
    "AUU": "I",
    "AUC": "I",
    "AUA": "I",
    "AUG": "M",
    "GUU": "V",
    "GUC": "V",
    "GUA": "V",
    "GUG": "V",
    "UCU": "S",
    "UCC": "S",
    "UCA": "S",
    "UCG": "S",
    "CCU": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "ACU": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "GCU": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "UAU": "Y",
    "UAC": "Y",
    "UAA": "Stop",
    "UAG": "Stop",
    "CAU": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "AAU": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "GAU": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "UGU": "C",
    "UGC": "C",
    "UGA": "Stop",
    "UGG": "W",
    "CGU": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "AGU": "S",
    "AGC": "S",
    "AGA": "R",
    "AGG": "R",
    "GGU": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",
}


for record in SeqIO.parse("./datasets/rosalind_orf.txt", "fasta"):
    sequence = record.seq.replace("T", "U")
    comp_sequence = (
        record.seq[::-1]
        .replace("A", "t")
        .replace("T", "a")
        .replace("G", "c")
        .replace("C", "g")
        .upper()
        .replace("T", "U")
    )

start_pattern = re.compile("AUG")

proteins = set()

for seq in [sequence, comp_sequence]:
    for match in start_pattern.finditer(str(seq)):
        protein = ""
        start_idx = match.start()
        for i in range(start_idx, len(seq) - 3, 3):
            triplet = seq[i : i + 3]
            aa = codon_table[triplet]
            if aa == "Stop":
                break
            protein += aa
        proteins.add(protein)

for p in proteins:
    print(p)
