# Rather ingenious solution by https://github.com/mtarbit/Rosalind-Problems/blob/master/e025-long.py

from Bio import SeqIO

seqs = []
for record in SeqIO.parse("./datasets/rosalind_long.txt", "fasta"):
    seqs.append(record.seq)


def find_overlaps(arr, acc=""):
    if len(arr) == 0:
        return acc

    elif len(acc) == 0:
        acc = arr.pop(0)
        return find_overlaps(arr, acc)

    else:
        for i in range(len(arr)):
            a = arr[i]
            l = len(a)  # noqa: E741

            for p in range(l // 2):
                q = l - p

                if acc.startswith(a[p:]):
                    arr.pop(i)
                    return find_overlaps(arr, a[:p] + acc)

                if acc.endswith(a[:q]):
                    arr.pop(i)
                    return find_overlaps(arr, acc + a[q:])


print(find_overlaps(seqs))
