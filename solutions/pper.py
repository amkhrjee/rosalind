import math

n, k = 91, 9

print(math.comb(n, k) * math.factorial(k) % 10**6)
