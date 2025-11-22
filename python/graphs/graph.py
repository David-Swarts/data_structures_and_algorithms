#!/usr/bin/env python3

# import graph_pkg

class adj_matrix:
  def __init__(self):
    self.matrix = []

    def add_node(self):
      # Add node and then append each existing node with an aditional null edge
      num_nodes = len(self.matrix) + 1
      self.matrix.append([0]*n)

graph = adj_matrix()
print(graph)
graph.add_node()