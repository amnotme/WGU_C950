# Chapter 6

**Introduction to graphs**

Many items in the world are connected, such as computers on a network connected by wires, cities connected by roads, or people connected by friendship.

A ***graph*** is a data structure for representing connections among items, and consists of vertices connected by edges.

- A ***vertex*** (or node) represents an item in a graph.
- An ***edge*** represents a connection between two vertices in a graph.

**Adjacency and paths**

In a graph:

- Two vertices are ***adjacent*** if connected by an edge.
- A ***path*** is a sequence of edges leading from a source (starting) vertex to a destination (ending) vertex. The ***path length*** is the number of edges in the path.
- The ***distance*** between two vertices is the number of edges on the shortest path between those vertices.

# 6.2 Applications of graphs

**Geographic maps and navigation**

Graphs are often used to represent a geographic map, which can contain information about places and travel routes. Ex: Vertices in a graph can represent airports, with edges representing available flights. Edge weights in such graphs often represent the length of a travel route, either in total distance or expected time taken to navigate the route. Ex: A map service with access to real-time traffic information can assign travel times to road segments.

**Product recommendations**

A graph can be used to represent relationships between products. Vertices in the graph corresponding to a customer's purchased products have adjacent vertices representing products that can be recommended to the customer.

**Social and professional networks**

A graph may use a vertex to represent a person. An edge in such a graph represents a relationship between 2 people. In a graph representing a social network, an edge commonly represents friendship. In a graph representing a professional network, an edge commonly represents business conducted between 2 people.

# 6.3 Graph representations: Adjacency lists

**Adjacency lists**

Various approaches exist for representing a graph data structure. A common approach is an adjacency list. Recall that two vertices are ***adjacent*** if connected by an edge. In an ***adjacency list*** graph representation, each vertex has a list of adjacent vertices, each list item representing an edge.

**Advantages of adjacency lists**

A key advantage of an adjacency list graph representation is a size of O(V + E), because each vertex appears once, and each edge appears twice. V refers to the number of vertices, E the number of edges.

However, a disadvantage is that determining whether two vertices are adjacent is O(V), because one vertex's adjacency list must be traversed looking for the other vertex, and that list could have V items. However, in most applications, a vertex is only adjacent to a small fraction of the other vertices, yielding a sparse graph. A ***sparse graph*** has far fewer edges than the maximum possible. Many graphs are sparse, like those representing a computer network, flights between cities, or friendships among people (every person isn't friends with every other person). Thus, the adjacency list graph representation is very common.


# 6.4 Graph representations: Adjacency matrices

**Adjacency matrices**

Various approaches exist for representing a graph data structure. One approach is an adjacency matrix. Recall that two vertices are ***adjacent*** if connected by an edge. In an ***adjacency matrix*** graph representation, each vertex is assigned to a matrix row and column, and a matrix element is 1 if the corresponding two vertices have an edge or is 0 otherwise.

**Analysis of adjacency matrices**

Assuming the common implementation as a two-dimensional array whose elements are accessible in O(1), then an adjacency matrix's key benefit is O(1) determination of whether two vertices are adjacent: The corresponding element is just checked for 0 or 1.

A key drawback is O($V^2$) size. Ex: A graph with 1000 vertices would require a 1000 x 1000 matrix, meaning 1,000,000 elements. An adjacency matrix's large size is inefficient for a sparse graph, in which most elements would be 0's.

An adjacency matrix only represents edges among vertices; if each vertex has data, like a person's name and address, then a separate list of vertices is needed.

# 6.5 Graphs: Breadth-first search

**Graph traversal and breadth-first search**

An algorithm commonly must visit every vertex in a graph in some order, known as a ***graph traversal***. A ***breadth-first search*** (BFS) is a traversal that visits a starting vertex, then all vertices of distance 1 from that vertex, then of distance 2, and so on, without revisiting a vertex.

### Social networking friend recommender using breadth-first search.

Social networking sites like Facebook, Google+, and LinkedIn use graphs to represent "friendship" among people. For a particular user, a site may wish to recommend new friends. One approach does a breadth-first search starting from the user, recommending new friends starting at distance 2 (distance 1 people are already friends with the user).

### Application of BFS: Find closest item in a peer-to-peer network.

In a ***peer-to-peer network***, computers are connected via a network and may seek and download file copies (such as songs or movies) via intermediary computers or routers. For example, one computer may seek the movie "The Wizard of Oz", which may exist on 10 computers in a network consisting of 100,000 computers. Finding the closest computer (having the fewest intermediaries) yields a faster download. A BFS traversal of the network graph can find the closest computer with that movie. The BFS traversal can be set to immediately return if the item sought is found during a vertex visit. Below, visiting vertex G finds the movie; BFS terminates, and a download process can begin, involving a path length of 2 (so only 1 intermediary). Vertex H also has the movie, but is further from B so wasn't visited yet during BFS. (Note: Distances of vertices visited during the BFS from B are shown below for convenience).

**Breadth-first search algorithm**

An algorithm for breadth-first search pushes the starting vertex to a queue. While the queue is not empty, the algorithm pops a vertex from the queue and visits the popped vertex, pushes that vertex's adjacent vertices (if not already discovered), and repeats.

When the BFS algorithm first encounters a vertex, that vertex is said to have been ***discovered***. In the BFS algorithm, the vertices in the queue are called the ***frontier***, being vertices thus far discovered but not yet visited. Because each vertex is visited at most once, an already-discovered vertex is not pushed to the queue again.

A "visit" may mean to print the vertex, append the vertex to a list, compare vertex data to a value and return the vertex if found, etc.

# 6.6 Python: Graphs

**Building the Graph and Vertex classes**

**Building the Graph and Vertex classes**

The Graph class holds a vertex adjacency list using a dictionary that maps a Vertex object to a list of adjacent Vertex objects. The Vertex class contains a label, but can be augmented by graph algorithms to contain additional data if required.

A Graph object is initialized with an empty adjacency list. Vertex objects are created and added to the Graph using the add_vertex() method.

```python
# Vertex class
class Vertex:
    def __init__(self, label):
        self.label = label

# Graph class       
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

# Example of adding vertices to graph
# Program to create and populate a Graph object.
g = Graph()
vertex_a = Vertex("New York")
vertex_b = Vertex("Tokyo")
vertex_c = Vertex("London")

g.add_vertex(vertex_a)
g.add_vertex(vertex_b)
g.add_vertex(vertex_c)
```

**Graph edges and edge weights**

Edges are represented as vertex *pairs*, using a 2-item tuple. Ex: (vertex_a, vertex_b) is an edge that goes from vertex_a to vertex_b. Undirected edges are two symmetric vertex pairs: (vertex_a, vertex_b) and (vertex_b, vertex_a). Edges also have numeric *weights*. By default, an edge is assigned with weight 1.0. Edge weights are stored in the dictionary edge_weights where the vertex pair is the key and the edge weight is the value. Ex: The edge (vertex_a, vertex_b) is assigned with weight 3.7 by `self.edge_weights[(vertex_a, vertex_b)] = 3.7`.

The method add_directed_edge() is used to add edges to a graph. To store the edge (vertex_a, vertex_b), vertex_b is appended to self.adjacency_list[vertex_a]. The method add_undirected_edge() calls add_directed_edge() twice to add both of the edge's symmetric versions. Both add_directed_edge() and add_undirected_edge() use a default parameter for the edge's weight, assigned with 1.0 if the method is called without the last parameter.

### Graph class methods: add_directed_edge() and add_undirected_edge().

```python
class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight = 1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight = 1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)
```

### A directed graph showing water flow through a system of pumping stations and a program to create the graph.

Graph with directed edges: Vertices (1, 2, 3, 4, 5) represent water pump stations. Edges represent water flow from one station to another, with edge weights indicating the capacity of flow that is possible along that route.

```Python
g = Graph()
vertex_a = Vertex("1")
vertex_b = Vertex("2")
vertex_c = Vertex("3")
vertex_d = Vertex("4")
vertex_e = Vertex("5")
g.add_vertex(vertex_a)
g.add_vertex(vertex_b)
g.add_vertex(vertex_c)
g.add_vertex(vertex_d)
g.add_vertex(vertex_e)

g.add_directed_edge(vertex_a, vertex_b, 8)
g.add_directed_edge(vertex_a, vertex_c, 12)
g.add_directed_edge(vertex_a, vertex_d, 17)
g.add_directed_edge(vertex_b, vertex_e, 11)
g.add_directed_edge(vertex_e, vertex_c, 23)
g.add_directed_edge(vertex_c, vertex_d, 15)
g.add_directed_edge(vertex_e, vertex_d, 6)
```

### An undirected graph of flight distances between cities.

Graph with undirected edges: The vertices are cities, and the edge represent flights between the cities, with distance in miles as the edge weights

```Python
g = Graph()
vertex_a = Vertex("Tokyo")
vertex_b = Vertex("New York")
vertex_c = Vertex("London")
vertex_d = Vertex("Sydney")
g.add_vertex(vertex_a)
g.add_vertex(vertex_b)
g.add_vertex(vertex_c)
g.add_vertex(vertex_d)

g.add_undirected_edge(vertex_a, vertex_b, 6743)
g.add_undirected_edge(vertex_a, vertex_c, 5941)
g.add_undirected_edge(vertex_a, vertex_d, 4863)
g.add_undirected_edge(vertex_b, vertex_c, 3425)
g.add_undirected_edge(vertex_b, vertex_d, 9868)
g.add_undirected_edge(vertex_c, vertex_d, 10562)
```
