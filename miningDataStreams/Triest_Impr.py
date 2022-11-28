import random
from collections import defaultdict

import numpy

from miningDataStreams.Edges import Edges


class Triest_Impr:

    def __init__(self, memory):
        # Global counter of triangles
        self.global_t = 0
        # Number of edges we track
        self.memory = memory
        # Set of edges we track
        self.reservoir = Edges()
        # Total number of edges at a certain time
        self.local_t = defaultdict(lambda: 0)

    def process_file(self, file_name):
        t = 0
        with open(file_name) as file:
            for index, line in enumerate(file):
                # Skip headers
                if index < 5:
                    continue
                u, v = tuple(sorted(map(int, line.strip().split())))
                if u == v or self.reservoir.sample.__contains__((u, v)):
                    continue
                t += 1
                self.update_counters(u, v, t)
                if self.sample_edges(t):
                    self.reservoir.add(u, v)
        return self.global_t

    def sample_edges(self, local_t):
        if local_t < self.memory:
            return True
        elif self.flip_biased_coin(local_t):
            ur, vr = random.sample(self.reservoir.sample, 1)[0]
            self.reservoir.remove(ur, vr)
            return True
        else:
            return False

    def flip_biased_coin(self, local_t):
        heads_probability = self.memory / local_t
        probability = random.random()
        return probability <= heads_probability

    def update_counters(self, u, v, t):
        if (u not in self.reservoir.neighbours.keys()) or (v not in self.reservoir.neighbours.keys()):
            return

        neighbours_intersection = set(self.reservoir.neighbours.get(u)).intersection(
            set(self.reservoir.neighbours.get(v)))
        neighbours_counter = len(neighbours_intersection)
        if neighbours_counter == 0:
            # no intersection -> no counters to update
            return

        weight = numpy.max([1, int(((t - 1) * (t - 2)) / (self.memory * (self.memory - 1)))])

        for c in neighbours_intersection:
            self.local_t[c] += weight
            self.global_t += weight
            self.local_t[u] += weight
            self.local_t[v] += weight
