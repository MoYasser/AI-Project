import heapq
from math import inf

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, v1, v2, cost = 1):
        try: neighbors = self.edges[v1]
        except KeyError: neighbors = {}
        neighbors[v2] = cost
        self.edges[v1] = neighbors

    def neighbors(self, vertex):
        try: return self.edges[vertex]
        except KeyError: return []

    def cost(self, v1, v2):
        try: return self.edges[v1][v2]
        except: return inf

    def uniform_cost_search(self, start, goal):
        found, fringe, visited, came_from, cost_so_far = False, [(0, start)], set([start]), {start: None}, {start: 0}
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('{:11s} | {}'.format('-', str((0, start))))
        while not found and len(fringe):
            _, current = heapq.heappop(fringe)
            print('{:11s}'.format(current), end=' | ')
            if current == goal: found = True; break
            for node in self.neighbors(current):
                new_cost = cost_so_far[current] + self.cost(current, node)
                if node not in visited or cost_so_far[node] > new_cost:
                    visited.add(node); came_from[node] = current; cost_so_far[node] = new_cost
                    heapq.heappush(fringe, (new_cost, node))
            print(', '.join([str(n) for n in fringe]))
        if found: print(); return came_from, cost_so_far[goal]
        else: print('No path from {} to {}'.format(start, goal)); return None, inf

    @staticmethod
    def print_path(came_from, goal):
        parent = came_from[goal]
        if parent:
            Graph.print_path(came_from, parent)
        else: print(goal, end='');return
        print(' =>', goal, end='')


    def __str__(self):
        return str(self.edges)

graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 3)
graph.add_edge('B', 'D', 1)
graph.add_edge('B', 'E', 1)
graph.add_edge('C', 'G', 1)
graph.add_edge('C', 'H', 2)
graph.add_edge('D', 'F', 1)

start, goal = 'A', 'G'
traced_path, cost = graph.uniform_cost_search(start, goal)
if (traced_path): print('Path:', end=' '); Graph.print_path(traced_path, goal); print('\nCost:', cost)