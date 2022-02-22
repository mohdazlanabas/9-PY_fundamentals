# 2. Use Class


class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    # Get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())

    def edges(self):
        return self.findedges()

    # 3. Find the distinct lits of edges
    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict(vrtx):
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nextvrtx})


# 1. Create the dictionary with graph elements
graph_elements = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"],
}

# Display Graph Vertices
g = graph(graph_elements)
print(g.getVertices())

# Add Vertex 
# Add Edge