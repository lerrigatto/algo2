# Return the density of a graph
# A graph is dense if the number of edges is close to O(|V|^2)
# A graph is sparse if the numeber of edges is close to O(|V|)
#
#
# For undirected graphs the density is defined as:
# D = (2|E|)/(|V|(|V|-1))
# Where |E| is the count of Edges
# Where |V| is the count of vertices

# To import our graph lib
#import sys
#sys.path.append(".")
#from graphs import graph

import networkx as nx

def density(v,e):
    return (2*e)/(v*(v-1))

def main():
    vertex = [1,2,3,4,5,6,7,8,9]
    edges = [(1,2),(2,3),(2,4),(3,4),(4,5)]

    G = nx.Graph()
    G.add_nodes_from(vertex)
    G.add_edges_from(edges)

    dens = density(len(G.nodes), len(G.edges))
    print(f"Density of G = {dens} ({nx.density(G)})")

main()
