with open("./datasets/rosalind_revc.txt", "r") as f:
    seq = f.readline()

print(
    seq[::-1]
    .replace("A", "t")
    .replace("T", "a")
    .replace("G", "c")
    .replace("C", "g")
    .upper()
)
