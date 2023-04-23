import matplotlib.pyplot as plt
import networkx as nx

class Vertex:
    def __init__(self, label):
        self.label = label
        self.distance = float("inf")   # Distance to graph's start vertex
        self.next = None

class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}
        # Create a graph to plot
        self.graph = nx.MultiDiGraph()
        # We will add all of the edges here
        self.edges_to_graph = []

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight = 1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)
        self.edges_to_graph.append((from_vertex.label, to_vertex.label))

    def add_undirected_edge(self, vertex_a, vertex_b, weight = 1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)
