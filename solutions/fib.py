n = 36
k = 4

fib_map = {1: 1, 2: 1}


def fib(n):
    if n in fib_map.keys():
        return fib_map[n]
    result = fib(n - 1) + k * fib(n - 2)
    fib_map[n] = result
    return result


print(fib(n))
