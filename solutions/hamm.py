with open("./datasets/rosalind_hamm.txt", "r") as f:
    s = f.readline()
    t = f.readline()

hamm = 0
for b1, b2 in zip(s, t):
    if b1 != b2:
        hamm += 1

print(hamm)
