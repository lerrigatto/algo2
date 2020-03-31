# Implement DFS algorithm

import networkx as nx

def iter_dfs(G,u):
    """ Depth First Search (DFS):
        The algorithm takes a Graph and a starting node (root).
        Returns full visit of the connected parts of the root; this visit is a tree.
        It uses two data structures: a set and a stack. The set is used to
        store the unvisited nodes. The stack is used to store the nodes visited
        from a given root. The content of the stack is also called walk.
        The output is stored in a list.
    """
    pass

def dfsr(G,u,visited,visited_edges):
    adj = G.successors(u)
    visited[u] = True
    for w in adj:
        #print(f"w:{w} - {visited}")
        if not visited[w]:
            visited_edges.append((u,w))
            #print(f"{visited_edges}")
            dfsr(G,w,visited,visited_edges)
    return visited

def dfs(G,u):
    """DFS recursive"""
    visited = [False] * (len(G.nodes))
    visited[u] = True
    visited_edges = []
    adj = G.successors(u)
    for w in adj:
        #print(f"w:{w} - {visited}")
        if not visited[w]:
            visited_edges.append((u,w))
            #print(f"{visited_edges}")
            dfsr(G,w,visited,visited_edges)
    return visited_edges

def main():
    # Generate random complete graph
    #G = nx.complete_graph(9)

    nodes = [0, 1, 2, 3]
    edges = [(0, 1), (1, 0), (0, 2), (2, 1), (3, 0), (3, 1)]
    G = nx.DiGraph(edges)
    root = 3

    my_visit = dfs(G, root)
    good_visit = list(nx.dfs_edges(G,source=root))
    #good_visit = list(nx.edge_dfs(G,source=root))
    print(f"My visit: {my_visit}")
    print(f"Good visit: {good_visit}")

main()
