import math

k = 7
N = 31

population = 2**k

p = 4 / 16
q = 1 - p

proba = sum(
    [
        math.comb(population, i) * (p ** (i)) * (q ** (population - i))
        for i in range(N, population + 1)
    ]
)

print(proba)
