class Vertex(object):
    def __init__(self, node, h):
        self.id = node
        self.adjacent = {}
        self.heuristic = {}
        self.fx = {}
        self.isGoal = False
        self.isStart = False
        self.heur = h

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, h, weight):
        self.heuristic[neighbor] = h
        self.adjacent[neighbor] = weight
        self.fx[neighbor] = h + weight

    def get_connections(self):
        return self.adjacent

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0
        self.heur_dict = {}
        self.fringe = {}
        self.m_adj = [[]]
        self.old_list = []
        self.cost = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node, h):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node, h)
        self.vert_dict[node] = new_vertex
        self.heur_dict[node] = h
        new_list = [[] for i in range(self.num_vertices)]
        self.old_list = self.m_adj
        self.m_adj = self.old_list + new_list
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, weight):
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], self.vert_dict[to].heur, weight)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], self.vert_dict[frm].heur, weight)
        self.m_adj[frm].append(to)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_goal(self, node):
        self.vert_dict[node].isGoal = True

    def del_goal(self, node):
        self.vert_dict[node].isGoal = False

    def set_start(self, node):
        self.vert_dict[node].isStart = True

    def del_start(self, node):
        self.vert_dict[node].isStart = False

    def BFS(self, s, goal):
        Q = []
        path = [s]
        visited = [False] * self.num_vertices
        Q.append(s)
        visited[s] = True
        while len(Q) > 0:
            v = Q.pop(0)
            path.append(v)
            if v == goal:
                return path
            for u in self.m_adj[v]:
                if not visited[u]:
                    Q.append(u)
                    visited[u] = True

    def DFS(self, current, goal):
        index = 0
        visited = [False for i in range(self.num_vertices)]
        stack = [current]
        path = []
        while len(stack) > 0:
            current = stack[index]
            stack.pop()
            index -= 1
            path.append(current)
            if not visited[current]:
                print(current)
                visited[current] = True
            if current == goal:
                return path
            for vertex in self.m_adj[current]:
                if not visited[vertex]:
                    stack.append(vertex)
                    index += 1

    def greedy_search(self, node):
        ref_path = [self.vert_dict[node]]
        path = [node]
        self.cost = 0
        while not self.vert_dict[node].isGoal:
            self.fringe = self.vert_dict[node].heuristic
            for i in ref_path:
                if i in self.fringe.keys():
                    self.fringe.pop(i)
            next_vertex = min(self.fringe, key=self.fringe.get)
            self.cost = self.cost + self.vert_dict[node].adjacent[next_vertex]
            node = next_vertex.id
            ref_path.append(next_vertex)
            path.append(node)
        print(path)
        print(ref_path)
        print(self.cost)
        return path

    def A_star(self, node):
        ref_path = [self.vert_dict[node]]
        path = [node]
        self.cost = 0
        while not self.vert_dict[node].isGoal:
            self.fringe = self.vert_dict[node].fx
            for i in ref_path:
                if i in self.fringe.keys():
                    self.fringe.pop(i)
            next_vertex = min(self.fringe, key=self.fringe.get)
            self.cost = self.cost + self.vert_dict[node].adjacent[next_vertex]
            node = next_vertex.id
            ref_path.append(next_vertex)
            path.append(node)
        print(path)
        print(ref_path)
        print(self.cost)
        return path

g = Graph()
g.add_vertex(0, 0)
g.add_vertex(1, 0)
g.add_vertex(2, 0)
g.add_vertex(3, 0)
g.add_vertex(4, 0)
g.add_vertex(5, 0)
g.add_vertex(6, 0)
g.add_edge(0,1,0)
g.add_edge(0,2,0)
g.add_edge(1,3,0)
g.add_edge(2,4 , 0)
g.add_edge(4, 6 , 0)
g.add_edge(3, 5, 0)
print(g.DFS(0,3))
