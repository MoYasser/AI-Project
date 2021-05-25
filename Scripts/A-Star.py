class Vertex:
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

    def add_neighbor(self, neighbor, h=999, cost=999):
        self.heuristic[neighbor] = h
        self.adjacent[neighbor] = cost
        self.fx[neighbor] = h + cost

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

    def add_edge(self, frm, to, cost):
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], self.vert_dict[to].heur, cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], self.vert_dict[to].heur, cost)


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

    def A_star_search(self, node):
        flag = True
        path = []
        path.append(node)
        while not self.vert_dict[node].isGoal:
            next_vertex = min(self.vert_dict[node].fx, key=self.vert_dict[node].fx.get)
            node = next_vertex.id
            path.append(node)
        print(path)

    def A_star_yasser(self, node):
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

g = Graph()
g.add_vertex(0, None)
g.add_vertex(1, 9)
g.add_vertex(2, 5)
g.add_vertex(3, 6)
g.add_vertex(4, 4)
g.add_vertex(5, 4)
g.add_vertex(6, 0)
g.add_vertex(7, 2)
g.add_edge(0, 1, 3)
g.add_edge(0, 3, 2)
g.add_edge(1, 4, 4)
g.add_edge(2, 4, 1)
g.add_edge(3, 2, 1)
g.add_edge(3, 5, 4)
g.add_edge(5, 2, 1)
g.add_edge(5, 6, 6)
g.add_edge(4, 7, 2)
g.add_edge(4, 6, 7)
g.add_edge(7, 6, 3)
g.set_start(0)
g.set_goal(6)
print(g.get_vertices())
print(g.vert_dict[0].get_connections())
g.A_star_search(0)
g.A_star_yasser(0)