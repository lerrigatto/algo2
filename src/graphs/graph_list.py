class GraphiList(Graph):
    """A graph implementation with adj lists"""
    def __init__(self, vertexes, edges):
        """ Initialize the graph with a set of vertexes and edges"""
        self.vertexes = []
        self.edges = []
        for vertex in vertexes:
            add_vertex(vertex)
        for edge in edges:
            add_edge(edge)

    def add_vertex(self, vertex):
        """ Add one vertex to the graph"""
        self.vertex.append(vertex)

    def add_edge(self, vertex1, vertex2):
        """ Add one edge between two vertexes"""
        curr_vertex = self.edges[vertex1]
        curre_vertex.append(vertex2)
        self.edges[vertex1] = curr_vertex


    def degree(self, vertex):
        """ The degree of the vertex"""
        pass

    def adj(self, vertex):
        """ Return the set of vertexs adjacent to `vertex`"""
        pass

