# Implement DFS algorithm

import networkx as nx
import random

def bfs(G,u):
    """ Breath First Search """
    visited = []
    visited_edges = []
    walk = []
    visited.append(u)
    walk.insert(0,u)

    while len(walk) > 0:
        v = walk.pop()
        adj = G.successors(v)
        print(f"v:{v}, adj:{list(G.successors(v))}")
        if adj:
            for w in adj:
                if w not in visited:
                    visited.append(w)
                    visited_edges.append((v,w))
                    walk.insert(0,w)

        else:
            print(f"else")
            walk.pop()
    return visited_edges
def main():

    nodes = [0, 1, 2, 3]
    edges = [(0, 1), (1, 0), (0, 2), (2, 1), (3, 0), (3, 1)]
    #G = nx.DiGraph(edges)
    # Generate random complete graph
    G = nx.gn_graph(100)
    root = random.randint(0,100)

    my_visit = bfs(G, root)
    good_visit = list(nx.bfs_edges(G,source=root))
    print(f"My visit: {my_visit}")
    print(f"Good visit: {good_visit}")

main()
