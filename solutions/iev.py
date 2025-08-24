population = {
    "AA-AA": 18527,
    "AA-Aa": 17590,
    "AA-aa": 18270,
    "Aa-Aa": 17788,
    "Aa-aa": 17048,
    "aa-aa": 16341,
}

probas = {"AA-AA": 1, "AA-Aa": 1, "AA-aa": 1, "Aa-Aa": 3 / 4, "Aa-aa": 0.5, "aa-aa": 0}

expectation = 0
for pair, cpls in population.items():
    expectation += cpls * probas[pair] * 2

print(expectation)
