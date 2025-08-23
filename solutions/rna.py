with open("./datasets/rosalind_rna.txt", "r") as f:
    seq = f.readline()

print(seq.replace("T", "U"))
