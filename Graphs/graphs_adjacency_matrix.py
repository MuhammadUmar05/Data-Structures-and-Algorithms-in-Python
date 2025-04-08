class Graph:
    def __init__(self, V, directed=False):
        self.V = V
        self.directed = directed
        self.adj = [[0 for _ in range(V)] for _ in range(V)]

    def addEdge(self, u, v):
        self.adj[u][v] = 1
        if not self.directed:
            self.adj[v][u] = 1

    def printGraph(self):
        for i in range(self.V):
            print(i, end=" -> ")
            for j in range(self.V):
                print(self.adj[i][j], end=" ")
            print()


# Undirected Graph
print("Undirected Graph:")
g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 4)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.printGraph()

# Directed Graph
print("\nDirected Graph:")
dg = Graph(5, directed=True)
dg.addEdge(0, 1)
dg.addEdge(0, 3)
dg.addEdge(0, 4)
dg.addEdge(1, 2)
dg.addEdge(3, 2)
dg.addEdge(4, 3)
dg.printGraph()
