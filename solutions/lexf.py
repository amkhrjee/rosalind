import itertools

seq_string = "A B C D E F G H I J"
seq = "".join(seq_string.split(" "))

n = 2

result = sorted(list(itertools.permutations(seq, 2)) + [(x, x) for x in seq])

for bases in result:
    print("".join(bases))
