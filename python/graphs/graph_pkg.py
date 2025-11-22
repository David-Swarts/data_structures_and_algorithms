#!/usr/bin/env python3

# Adjacency Matrix
  #
class adj_matrix:
  def __init__(self):
    self.matrix = [0]

    def add_node(self):
      # Add node and then append each existing node with an aditional null edge
      num_nodes = len(self.matrix) + 1
      self.matrix.append([0]*n)

    # def add_edge(self, value1, value2):

    # def get_node(self, value):

graph = adj_matrix()
print(graph)


# Adjacency List
  #
#   class adj_list:
#     def __init__(self):
#       self.matrix = []

#     def add_node(self, value):

#     def add_edge(self, value1, value2):

#     def get_node(self, value):


# # Object and Pointer

#   # Node
#     class Node:
#       def __init__(self, value):
#           self.value = value
#           self.neighbors = [] # List of references to other Node objects

#       def add_neighbor(self, neighbor_node):
#           if neighbor_node not in self.neighbors:
#               self.neighbors.append(neighbor_node)
#               # For an undirected graph, add self to the neighbor's list as well
#               neighbor_node.neighbors.append(self)

#       def __repr__(self): # For easier printing of Node objects
#           return f"Node({self.value})"

#   # Graph
#     class Graph:
#         def __init__(self):
#             self.nodes = {} # Dictionary to store nodes by their value

#         def add_node(self, value):
#             if value not in self.nodes:
#                 new_node = Node(value)
#                 self.nodes[value] = new_node
#                 return new_node
#             return self.nodes[value]

#         def add_edge(self, value1, value2):
#             node1 = self.add_node(value1)
#             node2 = self.add_node(value2)
#             node1.add_neighbor(node2)

#         def get_node(self, value):
#             return self.nodes.get(value)


# # Tests