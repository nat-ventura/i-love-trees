class MyGraph:
    def __init__(self):
        self.graph = {'A': ['B','C'],
                    'B': ['C','D'],
                    'C': ['D'],
                    'D': ['C'],
                    'E': ['F'],
                    'F': ['C']}

    def arcs(self):
        arcCount = []
        for vertex, neighbors in self.graph:
            for n in neighbors:
                print vertex, n

        return arcs