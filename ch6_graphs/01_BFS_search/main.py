from Graph import Vertex, Graph
from Queue import Queue
from graphviz import Digraph
import matplotlib.pyplot as plt
import networkx as nx

# Breadth-first search function
def breadth_first_search(graph, start_vertex):
    discovered_set = []
    frontier_queue = Queue()
    start_vertex.distance = 0              # start_vertex has a distance of 0 from itself

    frontier_queue.push(start_vertex)      # Push start_vertex to frontier_queue
    discovered_set.append(start_vertex)    # Add start_vertex to discovered_set

    while (frontier_queue.list.head != None):
        current_vertex = frontier_queue.pop()  # current_vertex is currently visited
        for adjacent_vertex in graph.adjacency_list[current_vertex]:
            if(discovered_set.count(adjacent_vertex) == 0):
                frontier_queue.push(adjacent_vertex)
                discovered_set.append(adjacent_vertex)
                # Distance of adjacent_vertex is 1 more than current_vertex
                adjacent_vertex.distance = current_vertex.distance + 1
    return discovered_set


# Main program
g = Graph()
vertex_a = Vertex('Joe')
vertex_b = Vertex('Eva')
vertex_c = Vertex('Taj')
vertex_d = Vertex('Chen')
vertex_e = Vertex('Lily')
vertex_f = Vertex('Jun')
vertex_g = Vertex('Ken')
vertices = [vertex_a, vertex_b, vertex_c, vertex_d, vertex_e, vertex_f, vertex_g]

g.add_vertex(vertex_a)
g.add_vertex(vertex_b)
g.add_vertex(vertex_c)
g.add_vertex(vertex_d)
g.add_vertex(vertex_e)
g.add_vertex(vertex_f)
g.add_vertex(vertex_g)

# Building graph
g.add_undirected_edge(vertex_a, vertex_b)  # Edge from Joe to Eva
g.add_undirected_edge(vertex_a, vertex_c)  # Edge from Joe to Taj
g.add_undirected_edge(vertex_b, vertex_e)  # Edge from Eva to Lily
g.add_undirected_edge(vertex_c, vertex_d)  # Edge from Taj to Chen
g.add_undirected_edge(vertex_c, vertex_e)  # Edge from Taj to Lily
g.add_undirected_edge(vertex_d, vertex_f)  # Edge from Chen to Jun
g.add_undirected_edge(vertex_e, vertex_f)  # Edge from Lily to Jun
g.add_undirected_edge(vertex_f, vertex_g)  # Edge from Jun to Ken


# create a directed multi-graph
g.graph.add_edges_from(g.edges_to_graph)

plt.figure(figsize=(8,8))
nx.draw(g.graph, connectionstyle='arc3, rad = 0.0')
plt.show()

start_name = input('Enter the starting person\'s name: ')
print()
start_vertex = None

for vertex in vertices:
    if vertex.label == start_name:
        start_vertex = vertex

if start_vertex is not None:
    discovered_set = breadth_first_search(g, start_vertex)
    print('Breadth-first search traversal')

    print('Start vertex: %s' % start_vertex.label)
    for vertex in discovered_set:
        print('%s: %d' % (vertex.label, vertex.distance))
else:
    print(f"There's no vertex with that name: [{start_name}]")
