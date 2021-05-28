class Graph:
    def __init__(self, v):
        self.m_V = v
        self.m_adj = [[] for i in range(v)]

    def addEdge(self, u, v):
        self.m_adj[u].append(v)

    def BFS(self, s):
        Q = []
        visited = [False] * self.m_V
        Q.append(s)
        visited[s] = True
        while len(Q) > 0:
            v = Q.pop(0)
            print(f'{v} ')
            for u in self.m_adj[v]:
                if not visited[u]:
                    Q.append(u)
                    visited[u] = True

    def DFS(self, current):

        visited = [False for i in range(self.m_V)]
        stack = []
        stack.append(current)
        while len(stack) > 0:
            current = stack[-1]
            stack.pop()
            if not visited[current]:
                print(current)
                visited[current] = True

            for vertex in self.m_adj[current]:
                if not visited[vertex]:
                    stack.append(vertex)


G = Graph(6)
G.addEdge(0, 1)
G.addEdge(0, 2)
G.addEdge(1, 3)
G.addEdge(2, 4)
G.addEdge(3, 4)
G.addEdge(4, 5)
print('DFS')
G.DFS(0)
print('BFS')
G.BFS(1)