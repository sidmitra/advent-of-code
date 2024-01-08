import math
import sys
import networkx as nx
import matplotlib.pyplot as plt

def first(lines, stoer_wagner=False):
    G = nx.Graph() # non directional graph
    for line in lines:
        src, dests = line.strip().split(":")
        dests = dests.strip().split(" ")

        for dest in dests:
            G.add_edge(src, dest)

    if not stoer_wagner:
        edges_to_cut = nx.minimum_edge_cut(G)
        G.remove_edges_from(edges_to_cut)

        # nx.draw(G, with_labels=True)
        # plt.show()
        # After removing the edges, we need to count the connected components and multiply them
        components = nx.connected_components(G)
        print(math.prod([len(c) for c in components]))

    if stoer_wagner:
        # can also be done with with stoer wagner
        cut_value, partition = nx.stoer_wagner(G)
        print("Prod: ", math.prod([len(p) for p in partition]))



# python main.py input.txt
if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, "r") as infile:
        lines = infile.read().splitlines()

    first(lines, stoer_wagner=True)

    # second(lines)
