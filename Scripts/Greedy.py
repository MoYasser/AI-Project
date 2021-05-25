from operator import __getitem__


class Vertex(object):
    def __init__(self, node, h):
        self.id = node
        self.adjacent = {}
        self.heuristic = {}
        self.isGoal = False
        self.isStart = False
        self.heur = h

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, h, weight):
        self.heuristic[neighbor] = h
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.heuristic

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

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node, h):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node, h)
        self.vert_dict[node] = new_vertex
        self.heur_dict[node] = h
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, weight):
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], self.vert_dict[to].heur, weight)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], self.vert_dict[frm].heur, weight)

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


g = Graph()
g.add_vertex(0, 1)
g.add_vertex(2, 2)
g.add_vertex(3, 4)
g.add_vertex(4, 8)
g.add_vertex(5, 0)
g.add_edge(2, 0, 3)
g.add_edge(2, 3, 2)
g.add_edge(4, 2, 1)
g.add_edge(4, 5, 3)
g.add_edge(5, 3, 2)
g.set_start(0)
g.set_goal(5)
print(g.get_vertices())
g.greedy_search(0)

