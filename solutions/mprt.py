import re

import requests

base_url = "https://rest.uniprot.org/uniprotkb/"
options = "?fields=sequence"
headers = {"Accept": "application/json"}

with open("./datasets/rosalind_mprt.txt") as f:
    ids = [id.strip() for id in f.readlines()]


def get_sequence(id):
    try:
        return requests.get(
            base_url + id + options, headers, allow_redirects=True
        ).json()["sequence"]["value"]
    except KeyError:
        # Must be removed from Uniprotkb, so search in Uniparc
        upi = requests.get(
            f"https://rest.uniprot.org/uniparc/search?query=%28{id}%29", headers
        ).json()["results"][0]["uniParcId"]
        return requests.get(
            "https://rest.uniprot.org/uniparc/" + upi + options, headers
        ).json()["sequence"]["value"]


motif_pattern = re.compile("N[^P][ST][^P]")

for id in ids:
    seq = get_sequence(id.split("_")[0])
    match_positions = []
    for match in motif_pattern.finditer(seq):
        match_positions.append(str(match.start() + 1))
    if len(match_positions) != 0:
        print(id)
        print(" ".join(match_positions))

# Note: This might show up as "Wrong Answer" since lots of the proteins have actually changed since
# the problem was originally added
