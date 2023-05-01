from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.distance = {}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2, distance):
        if node1 is not node2:
            self.adjacency_list[node1].append((node2, distance))
            self.adjacency_list[node2].append((node1, distance))

    def get_distance(self, start_node, end_node):
        if not self.adjacency_list[start_node] or end_node not in self.adjacency_list:
            return float('inf')
        else:
            for adj_node in self.adjacency_list[start_node]:
                if adj_node[0] == end_node:
                    return adj_node[1]
            return float('inf')

    def a_star_shortest_path(self, start_node, end_node = None):
        # Initialize the unvisited queue
        unvisited_queue = deque([(start_node, 0)])

        # Initialize the distance to each node
        for node in self.adjacency_list:
            self.distance[node] = float('inf')

        # Set the distance to the start node to 0
        self.distance[start_node] = 0

        # Visit each location, then remove it from unvisited queue
        while len(unvisited_queue) > 0:
            # Visit location at min distance
            curr_node, curr_dist = unvisited_queue.popleft()

            if end_node is not None and curr_node == end_node:
                break

            # Check path lengths at new location
            for adj_node in self.adjacency_list[curr_node]:
                dist = self.get_distance(curr_node, adj_node[0])
                if dist == float('inf'):
                    alt_path_dist = curr_dist + adj_node[1]
                else:
                    alt_path_dist = dist + adj_node[1]

                if alt_path_dist < self.distance[adj_node[0]]:
                    self.distance[adj_node[0]] = alt_path_dist
                    if adj_node[0] not in self.distance:
                        unvisited_queue.append((adj_node[0], alt_path_dist))

        # Return the distance to the end_node
        if end_node is None:
            return self.distance
        else:
            return self.distance[end_node]
