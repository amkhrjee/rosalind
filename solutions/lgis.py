def lis(seq):
    n = len(seq)
    dp = [1] * n  # dp[i] = length of LIS ending at i
    prev = [-1] * n  # parent pointers for reconstruction

    for i in range(n):
        for j in range(i):
            if seq[j] < seq[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    max_len = max(dp)
    idx = dp.index(max_len)

    out = []
    while idx != -1:
        out.append(seq[idx])
        idx = prev[idx]
    return out[::-1]


def lds(seq):
    n = len(seq)
    dp = [1] * n
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if seq[j] > seq[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    max_len = max(dp)
    idx = dp.index(max_len)

    out = []
    while idx != -1:
        out.append(seq[idx])
        idx = prev[idx]
    return out[::-1]


def solve(path="./datasets/rosalind_lgis.txt"):
    with open(path, "r") as f:
        _n = int(f.readline().strip())
        seq = list(map(int, f.readline().split()))

    inc = lis(seq)
    dec = lds(seq)

    print(" ".join(map(str, inc)))
    print(" ".join(map(str, dec)))


if __name__ == "__main__":
    solve()
