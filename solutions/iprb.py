import math

k = 19  # homo dom (XX)
m = 16  # hetero (Xx)
n = 23  # homo rec (xx)

total = k + m + n


def get_pairs_count(n):
    return math.factorial(n) / (2 * math.factorial(n - 2))


possible_pairs = get_pairs_count(total)
homodom_pairs = get_pairs_count(k)
hetero_pairs = get_pairs_count(m)  # 3/4 have dom allele
homodom_rec_pairs = get_pairs_count(k + n) - get_pairs_count(n)  # all have dom allele
homodom_hetero_pairs = get_pairs_count(k + m) - hetero_pairs  # all have dom allele
pure_hetero_homorec_pairs = (
    get_pairs_count(m + n) - get_pairs_count(n) - hetero_pairs
)  # 1/2 have dom allele


proba = (
    (homodom_rec_pairs + homodom_hetero_pairs - homodom_pairs)
    + (hetero_pairs * 3 / 4)
    + (pure_hetero_homorec_pairs * 1 / 2)
) / possible_pairs

print(proba)
