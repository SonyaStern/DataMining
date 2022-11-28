class Edges:

    def __init__(self):
        self.sample = set()
        self.neighbours = dict()
        self.edges_number = 0

    def add(self, u, v):
        self.add_neighbour(u, v)
        self.add_neighbour(v, u)

        self.sample.add((u, v))
        self.edges_number += 1

    def remove(self, u, v):
        if u != v:
            self.remove_neighbour(u, v)
        self.remove_neighbour(v, u)

        self.sample.remove((u, v))
        self.edges_number -= 1

    def add_neighbour(self, u, v):
        if u in self.neighbours.keys():
            self.neighbours.get(u).add(v)
        else:
            self.neighbours[u] = {v}
        sorted(self.neighbours[u])

    def remove_neighbour(self, u, v):
        self.neighbours.get(u).remove(v)
        neighbour_u = self.neighbours.get(u)
        if len(neighbour_u) == 0:
            del self.neighbours[u]
