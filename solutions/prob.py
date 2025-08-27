# Thanks to: https://noobest.medium.com/rosalind-introduction-to-random-strings-462219689245
import math

seq = "TCGATCCTCTTCACTTGTTAATTACTGCCACCTGAATATCCTGGAACGCTCTGTCAGGGGTTGTTACGGCTCCGGAGAATGTACGTGCGAGGTTCGCTTC"
gcc_string = "0.062 0.100 0.176 0.245 0.293 0.337 0.373 0.416 0.500 0.528 0.570 0.604 0.661 0.726 0.777 0.822 0.894 0.911"
gcc = [float(x) for x in gcc_string.split(" ")]

log_probas = []
for gc in gcc:
    probas = {"A": (1 - gc) / 2, "C": gc / 2, "G": gc / 2, "T": (1 - gc) / 2}
    log_proba = 0
    for base in seq:
        log_proba += math.log10(probas[base])
    log_probas.append(log_proba)

print(" ".join([str(round(x, 3)) for x in log_probas]))
