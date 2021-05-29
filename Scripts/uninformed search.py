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

    def DFS(self, current, goal):
        index = 0
        visited = [False for i in range(self.m_V)]
        stack = [current]
        while len(stack) > 0:
            current = stack[index]
            stack.pop()
            index -= 1
            if not visited[current]:
                print(current)
                visited[current] = True
            if current == goal:
                return
            for vertex in self.m_adj[current]:
                if not visited[vertex]:
                    stack.append(vertex)
                    index += 1


g = Graph(10)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.DFS(0, 3)
