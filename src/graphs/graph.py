class Graph:
    """A graph interface"""
    def __init__(self, vertex, edges):
        """ Initialize the graph with a set of vertexes and edges"""

    def add_vertex(self, vertex):
        """ Add one vertex to the graph"""
        pass

    def add_edge(self, vertex1, vertex2):
        """ Add one edge between two vertexes"""
        pass

    def degree(self, vertex):
        """ The degree of the vertex"""
        pass

    def adj(self, vertex):
        """ Return the set of vertexs adjacent to `vertex`"""
        pass

