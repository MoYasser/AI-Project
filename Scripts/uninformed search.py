class Graph:
    def __init__(self, v):
        self.m_V = v
        self.m_adj = [[] for i in range(v)]

    def add_edge(self, u, v):
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


g = Graph(10)
g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_edge(1, 4)
g.add_edge(2, 4)
g.add_edge(3, 2)
g.add_edge(3, 5)
g.add_edge(5, 2)
g.add_edge(5, 6)
g.add_edge(4, 7)
g.add_edge(4, 6)
g.add_edge(7, 6)
print('DFS')
g.DFS(0)
print('BFS')
g.BFS(1)
