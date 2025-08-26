# Thanks to: http://saradoesbioinformatics.blogspot.com/2016/07/perfect-matchings-and-rna-secondary.html
import math

seq = "UAUAUAAUAUUCCGUCGGGAAAAUCAAGCGCGCAUUCCACAUGUAUCCAAGAUGUCCCGGCGUGUUAGCAUGGU"

# The trick is to think of A-U and G-C as separate complete bipartite graphs

print(math.factorial(seq.count("A")) * math.factorial(seq.count("G")))
