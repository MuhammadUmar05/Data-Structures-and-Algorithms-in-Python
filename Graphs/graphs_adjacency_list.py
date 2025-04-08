class Graph:
    def __init__(self, V, directed=False):
        self.V = V
        self.directed = directed
        self.adj = [[] for _ in range(V)]

    def addEdge(self, u, v):
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)

    def printGraph(self):
        for i in range(self.V):
            if self.adj[i]:
                print(f"{i} -> {" ".join(map(str,self.adj[i]))}")
            else:
                print(f"{i} -> None")


# undirected graph
print("Undirected Graph: ")
g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 4)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.printGraph()

# directed graph
print("\nDirected Graph: ")
dg = Graph(5, True)
dg.addEdge(0, 1)
dg.addEdge(0, 3)
dg.addEdge(0, 4)
dg.addEdge(1, 2)
dg.addEdge(3, 2)
dg.addEdge(4, 3)
dg.printGraph()
