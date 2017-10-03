class MyGraph:
    def __init__(self):
        self.graph = {'A': ['B','C'],
                    'B': ['C','D'],
                    'C': ['D'],
                    'D': ['C'],
                    'E': ['F'],
                    'F': ['C']}

    def arcFinder(self):
        arcs = []
        for vertex, neighbors in self.graph:
            for n in neighbors:
                print vertex, n

        return arcs