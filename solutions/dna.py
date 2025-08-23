with open("./datasets/rosalind_dna.txt", "r") as f:
    seq = f.readline()

n_A = 0
n_C = 0
n_G = 0
n_T = 0

for b in seq:
    if b == "A":
        n_A += 1
    elif b == "C":
        n_C += 1
    elif b == "G":
        n_G += 1
    elif b == "T":
        n_T += 1

print(f"{n_A} {n_C} {n_G} {n_T}")
