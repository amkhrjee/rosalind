import itertools
import math

n = 3

print(math.factorial(n))

perms = list(itertools.permutations(list(range(1, n + 1))))

for p in perms:
    print(" ".join([str(x) for x in p]))
