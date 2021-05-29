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

    def get_heuristic(self, neighbor):
        return  self.heuristic[neighbor]

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

    def BFS(self, node):
        ref_path = [self.vert_dict[node]]
        path = [node]
        while not self.vert_dict[node].isGoal:
            self.fringe = self.vert_dict[node].fx
            for i in ref_path:
                if i in self.fringe.keys():
                    self.fringe.pop(i)
            next_vertex = min(self.fringe, key=self.fringe.get)
            node = next_vertex.id
            ref_path.append(next_vertex)
            path.append(node)
        print(path)
        print(ref_path)

    def DFS(self, current):

        visited = [False for i in range(self.num_vertices)]
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

    def greedy_search(self, node):
        ref_path = [self.vert_dict[node]]
        path = [node]
        cost = 0
        while not self.vert_dict[node].isGoal:
            self.fringe = self.vert_dict[node].heuristic
            for i in ref_path:
                if i in self.fringe.keys():
                    self.fringe.pop(i)
            next_vertex = min(self.fringe, key=self.fringe.get)
            cost = cost + self.vert_dict[node].adjacent[next_vertex]
            node = next_vertex.id
            ref_path.append(next_vertex)
            path.append(node)
        print(path)
        print(ref_path)
        print(cost)

    def A_star(self, node):
        ref_path = [self.vert_dict[node]]
        path = [node]
        cost = 0
        while not self.vert_dict[node].isGoal:
            self.fringe = self.vert_dict[node].fx
            for i in ref_path:
                if i in self.fringe.keys():
                    self.fringe.pop(i)
            next_vertex = min(self.fringe, key=self.fringe.get)
            cost = cost + self.vert_dict[node].adjacent[next_vertex]
            node = next_vertex.id
            ref_path.append(next_vertex)
            path.append(node)
        print(path)
        print(ref_path)
        print(cost)
        return path


g = Graph()
g.add_vertex(0, 100)
g.add_vertex(1, 9)
g.add_vertex(2, 5)
g.add_vertex(3, 6)
g.add_vertex(4, 4)
g.add_vertex(5, 4)
g.add_vertex(6, 0)
g.add_edge(0, 1, 3)
g.add_edge(0, 3, 2)
g.add_edge(1, 4, 4)
g.add_edge(2, 4, 1)
g.add_edge(3, 2, 1)
g.add_edge(3, 5, 4)
g.add_edge(5, 2, 1)
g.add_vertex(7, 2)
g.add_edge(5, 6, 6)
g.add_edge(4, 7, 2)
g.add_edge(4, 6, 7)
g.add_edge(7, 6, 3)
g.set_start(0)
g.set_goal(6)
print('DFS')
g.DFS(0)
print('BFS')
g.BFS(0)
print('Greedy')
g.greedy_search(0)
print('A*')
g.A_star(0)