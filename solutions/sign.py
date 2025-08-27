import itertools

dataset = 3

seq = list(range(1, dataset + 1))

abs_perms = itertools.permutations(seq)

perms = []
for p in abs_perms:
    for signs in itertools.product([1, -1], repeat=dataset):
        signed = [a * s for a, s in zip(p, signs)]
        perms.append(signed)

print(len(perms))
for each in perms:
    print(" ".join(map(str, each)))
