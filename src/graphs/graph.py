class Graph:
    """A graph interface"""
    def __init__(self, nodes, archs):
        """ Initialize the graph with a set of nodes and archs"""
        pass

    def addNode(self, node):
        """ Add one node to the graph"""
        pass

    def addArch(self, node1, node2):
        """ Add one arch between two nodes"""
        pass

    def degree(self, node):
        """ The degree of the node"""
        pass

    def adj(self, node):
        """ Return the set of nodes adjacent to `node`"""
        pass

