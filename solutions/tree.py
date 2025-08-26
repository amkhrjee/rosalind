with open("./datasets/rosalind_tree.txt", "r") as f:
    n = int(f.readline())
    adj_list = {}
    for line in f.readlines():
        key, value = tuple(line.strip().split(" "))
        if key in adj_list.keys():
            adj_list[key].append(int(value))
        else:
            adj_list[key] = [int(value)]


# find out the number of edges and the number of nodes
n_edges = sum(len(v) for v in adj_list.values())

print(n - 1 - n_edges)
