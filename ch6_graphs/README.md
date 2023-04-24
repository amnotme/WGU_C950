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

# 6.8 Graphs: Depth-first search

**Graph traversal and depth-first search**

An algorithm commonly must visit every vertex in a graph in some order, known as a ***graph traversal***. A ***depth-first search*** (DFS) is a traversal that visits a starting vertex, then visits every vertex along each path starting from that vertex to the path's end before backtracking.

**Depth-first search algorithm**

An algorithm for depth-first search pushes the starting vertex to a stack. While the stack is not empty, the algorithm pops the vertex from the top of the stack. If the vertex has not already been visited, the algorithm visits the vertex and pushes the adjacent vertices to the stack.

```Python
DFS(startV) {
   Push startV to stack

   while ( stack is not empty ) {
      currentV = Pop stack
      if ( currentV is not in visitedSet ) {
         "Visit" currentV
         Add currentV to visitedSet
         for each vertex adjV adjacent to currentV
            Push adjV to stack
      }
   }
}
```

**Recursive DFS algorithm**

A recursive DFS can be implemented using the program stack instead of an explicit stack. The recursive DFS algorithm is first called with the starting vertex. If the vertex has not already been visited, the recursive algorithm visits the vertex and performs a recursive DFS call for each adjacent vertex.

```Python

RecursiveDFS(currentV) {
   if ( currentV is not in visitedSet ) {
      Add currentV to visitedSet
      "Visit" currentV
      for each vertex adjV adjacent to currentV
         RecursiveDFS(adjV)
   }
}
```

# 6.9 Directed graphs

**Directed graphs**

A ***directed graph***, or ***digraph***, consists of vertices connected by directed edges. A ***directed edge*** is a connection between a starting vertex and a terminating vertex. In a directed graph, a vertex Y is ***adjacent*** to a vertex X, if there is an edge from X to Y.

Many graphs are directed, like those representing links between web pages, maps for navigation, or college course prerequisites.

**Paths and cycles**

In a directed graph:

- A ***path*** is a sequence of directed edges leading from a source (starting) vertex to a destination (ending) vertex.
- A ***cycle*** is path that starts and ends at the same vertex. A directed graph is ***cyclic*** if the graph contains a cycle, and ***acyclic*** if the graph does not contain a cycle.

### Cycles in directed graphs: Kidney transplants

A patient needing a kidney transplant may have a family member willing to donate a kidney but is incompatible. That family member is willing to donate a kidney to someone else, as long as their family member also receives a kidney donation. Suppose Gregory needs a kidney. Gregory's wife, Eleanor, is willing to donate a kidney but is not compatible with Gregory. However, Eleanor is compatible with another patient Joanna, and Joanna's husband Darrell is compatible with Gregory. So, Eleanor donates a kidney to Joanna, and Darrell donates a kidney to Gregory, which is an example of a 2-way kidney transplant. In 2015, a 9-way kidney transplant involving 18 patients was performed within 36 hours (Source: [SF Gate](http://www.sfgate.com/health/article/9-way-kidney-swap-involving-18-surgeries-at-2-6307975.php)). Multiple-patient kidney transplants can be represented as cycles within a directed graph.

![https://zytools.zybooks.com/zyAuthor/DataStructures/46/IMAGES/embedded_image_1_cd899718-f11d-49cb-a55b-5fab6177ba01_uvarMp7wYIBBdZ54B4kq.png](https://zytools.zybooks.com/zyAuthor/DataStructures/46/IMAGES/embedded_image_1_cd899718-f11d-49cb-a55b-5fab6177ba01_uvarMp7wYIBBdZ54B4kq.png)

In this graph, vertices represent patients, and edges represent compatibility between a patient's family member (shown in parentheses) and another patient. An N-way kidney transplant is represented as a cycle with N edges. Due the complexity of coordinating multiple simultaneous surgeries, hospitals and doctors typically try to find the shortest possible cycle.


# 6.10 Weighted graphs

**Weighted graphs**

A ***weighted graph*** associates a weight with each edge. A graph edge's ***weight***, or ***cost***, represents some numerical value between vertex items, such as flight cost between airports, connection speed between computers, or travel time between cities. A weighted graph may be directed or undirected.

**Path length in weighted graphs**

In a weighted graph, the ***path length*** is the sum of the edge weights in the path.

**Negative edge weight cycles**

The ***cycle length*** is the sum of the edge weights in a cycle. A ***negative edge weight cycle*** has a cycle length less than 0. A shortest path does not exist in a graph with a negative edge weight cycle, because each loop around the negative edge weight cycle further decreases the cycle length, so no minimum exists.

# 6.11 Algorithm: Dijkstra's shortest path

**Dijkstra's shortest path algorithm**

Finding the shortest path between vertices in a graph has many applications. Ex: Finding the shortest driving route between two intersections can be solved by finding the shortest path in a directed graph where vertices are intersections and edge weights are distances. If edge weights instead are expected travel times (possibly based on real-time traffic data), finding the shortest path will provide the fastest driving route.

***Dijkstra's shortest path algorithm***, created by Edsger Dijkstra, determines the shortest path from a start vertex to each vertex in a graph. For each vertex, Dijkstra's algorithm determines the vertex's distance and predecessor pointer. A vertex's ***distance*** is the shortest path distance from the start vertex. A vertex's ***predecessor pointer*** points to the previous vertex along the shortest path from the start vertex.

Dijkstra's algorithm initializes all vertices' distances to infinity (∞), initializes all vertices' predecessors to 0, and pushes all vertices to a queue of unvisited vertices. The algorithm then assigns the start vertex's distance with 0. While the queue is not empty, the algorithm pops the vertex with the shortest distance from the queue. For each adjacent vertex, the algorithm computes the distance of the path from the start vertex to the current vertex and continuing on to the adjacent vertex. If that path's distance is shorter than the adjacent vertex's current distance, a shorter path has been found. The adjacent vertex's current distance is updated to the distance of the newly found shorter path's distance, and vertex's predecessor pointer is pointed to the current vertex.

```python

DijkstraShortestPath(startV) {
   for each vertex currentV in graph {
      currentV->distance = Infinity
      currentV->predV = 0
      Push currentV to unvisitedQueue
   }

   // startV has a distance of 0 from itself
   startV->distance = 0

   while (unvisitedQueue is not empty) {
      // Visit vertex with minimum distance from startV
      currentV = PopMin unvisitedQueue

      for each vertex adjV adjacent to currentV {
         edgeWeight = weight of edge from currentV to adjV
         alternativePathDistance = currentV->distance + edgeWeight

         // If shorter path from startV to adjV is found,
         // update adjV's distance and predecessor
         if (alternativePathDistance < adjV->distance) {
            adjV->distance = alternativePathDistance
            adjV->predV = currentV
         }
      }
   }
}
```

**Finding shortest path from start vertex to destination vertex**

After running Dijkstra's algorithm, the shortest path from the start vertex to a destination vertex can be determined using the vertices' predecessor pointers. If the destination vertex's predecessor pointer is not 0, the shortest path is traversed in reverse by following the predecessor pointers until the start vertex is reached. If the destination vertex's predecessor pointer is 0, then a path from the start vertex to the destination vertex does not exist.

**Algorithm efficiency**

If the unvisited vertex queue is implemented using a list, the runtime for Dijkstra's shortest path algorithm is O(V2). The outer loop executes V times to visit all vertices. In each outer loop execution, popping the vertex from the queue requires searching all vertices in the list, which has a runtime of O(V). For each vertex, the algorithm follows the subset of edges to adjacent vertices; following a total of E edges across all loop executions. Given E < V2, the runtime is O(V*V + E) = O(V2 + E) = O(V2). Implementing the queue using a fast heap data structure reduces the runtime to O(E + V log V).

**Negative edge weights**

Dijkstra's shortest path algorithm can be used for unweighted graphs (using a uniform edge weight of 1) and weighted graphs with non-negative edges weights. For a directed graph with negative edge weights, Dijkstra's algorithm may not find the shortest path for some vertices, so the algorithm should not be used if a negative edge weight exists.


# 6.12 Python: Dijkstra's shortest path

**Dijkstra's shortest path**

Dijkstra's algorithm computes the shortest path from a given starting vertex to all other vertices in the graph.

To perform Dijjkstra's algorithm, the Graph and Vertex classes are used. The Vertex class is extended to include two additional data members:

- distance - The total sum of the edge weights on a path from some start vertex to the vertex.
- pred_vertex - A reference to the vertex that occurs immediately before the vertex, on a path from some start vertex to the vertex.


### Dijkstra's shortest path algorithm.

```python
def dijkstra_shortest_path(g, start_vertex):
    # Put all vertices in an unvisited queue.
    unvisited_queue = []
    for current_vertex in g.adjacency_list:
        unvisited_queue.append(current_vertex)

    # start_vertex has a distance of 0 from itself
    start_vertex.distance = 0

    # One vertex is removed with each iteration; repeat until the list is
    # empty.
    while len(unvisited_queue) > 0:

        # Visit vertex with minimum distance from start_vertex
        smallest_index = 0
        for i in range(1, len(unvisited_queue)):
            if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
                smallest_index = i
        current_vertex = unvisited_queue.pop(smallest_index)

        # Check potential path lengths from the current vertex to all neighbors.
        for adj_vertex in g.adjacency_list[current_vertex]:
            edge_weight = g.edge_weights[(current_vertex, adj_vertex)]
            alternative_path_distance = current_vertex.distance + edge_weight

            # If shorter path from start_vertex to adj_vertex is found,
            # update adj_vertex's distance and predecessor
            if alternative_path_distance < adj_vertex.distance:
                adj_vertex.distance = alternative_path_distance
                adj_vertex.pred_vertex = current_vertex
```

After calling the dijkstra_shortest_path() function, the shortest path from the starting vertex to any other given vertex can be built by following the pred_vertex *backwards*
from the destination vertex to the starting vertex.

### Getting the shortest path and distance between two vertices

```python
def get_shortest_path(start_vertex, end_vertex):
    # Start from end_vertex and build the path backwards.
    path = ''
    current_vertex = end_vertex
    while current_vertex is not start_vertex:
        path = ' -> ' + str(current_vertex.label) + path
        current_vertex = current_vertex.pred_vertex
    path = start_vertex.label + path
    return path
```
