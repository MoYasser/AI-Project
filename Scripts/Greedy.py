class Vertex:
    def __init__(self, node, h):
        self.id = node
        self.adjacent = {}
        self.heuristic = {}
        self.isGoal = False
        self.isStart = False
        self.heur = h

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, h=0):
        self.heuristic[neighbor] = h

    def get_connections(self):
        return self.heuristic.items()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node, h):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node, h)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to):
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], self.vert_dict[to].heur)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], 999999)

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

    def greedy_search(self, node):
        flag = True
        path = []
        path.append(node)
        while not self.vert_dict[node].isGoal:
            next_vertex = min(self.vert_dict[node].heuristic, key=self.vert_dict[node].heuristic.get)
            node = next_vertex.id
            path.append(node)
        print(path)


g = Graph()
g.add_vertex(0, None)
g.add_vertex(1, 6)
g.add_vertex(2, 3)
g.add_vertex(3, 2)
g.add_vertex(4, 0)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.set_goal(4)
g.set_start(0)
print(g.get_vertices())
print(g.vert_dict[0].get_connections())
g.greedy_search(0)
