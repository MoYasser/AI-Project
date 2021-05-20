class Vertex:
    def __init__(self,node):
        self.id=node
        self.adjacent={}
        self.isGoal = False
        self.isStart = False


    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, letter):
        if letter not in self.neighbors:
            self.neighbors.append()
            self.neighbors.sort ()

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_goal(self):
        self.isGoal = True

    def del_goal(self):
        self.isGoal = False

    def set_start(self):
        self.isStart = True

    def del_start(self):
        self.isStart = True


class Graph:
    def __init__(self, v):
        self.m_v = v
        self.m_adj = [[] for i in range(v)]

    def addEdge(self, u, v):
        self.m_adj[u].append(v)

    def DFS_rec(self, s, visited):
        visited[s] = True
        print(s)
        for u in self.m_adj[s]:
            if not visited[u]:
                self.DFS_rec(u, visited)

    def DFS_it(self, s, visited):
        S = []
        S.append(s)
        visited[s] = True
        while len(S) > 0:
            u = S[-1]
            S.pop()
            print(u)
            for v in self.m_adj[u]:
                if not visited[v]:
                    S.append(v)
                    visited[v] = True

    def DFS(self):
        visited = [False] * self.m_v
        for i in range(self.m_v):
            if not visited[i]:
                self.DFS_rec(i, visited)


G = Graph(6)
G.addEdge(0,1)
G.addEdge(0,2)
G.addEdge(1,3)
G.addEdge(2,4)
G.addEdge(2,5)
G.DFS()