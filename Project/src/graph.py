import math
from models.hub import Hub
from typing import List, Dict, Any, Union, Tuple

class Graph:
    """
    A class to represent a graph of locations and their distances.

    Attributes:
        adjacency_list (Dict[Hub, List[Hub]]): A dictionary mapping each location
            to a list of its adjacent locations.
        distance (Dict[Tuple[Hub, Hub], float]): A dictionary mapping each pair of
            locations to the distance between them.
    """

    def __init__(self) -> None:
        """Initialize the Graph with empty adjacency list and distance dictionary."""
        self.adjacency_list: Dict[Hub, List[Hub]] = {}
        self.distance: Dict[Tuple[Hub, Hub], float] = {}

    def add_node(self, hub: Hub) -> None:
        """Add a new node (location) to the graph."""
        if hub not in self.adjacency_list:
            self.adjacency_list[hub]: List[Hub] = []

    def add_edge(self, hub1: Hub, hub2: Hub, distance: float) -> None:
        """
        Add a new edge (path) to the graph between two nodes (locations).

        Args:
            hub1 (Hub): The first location.
            hub2 (Hub): The second location.
            distance (float): The distance between the two locations.
        """
        if hub1 is not hub2:
            self.adjacency_list.get(hub1).append(hub2)
            self.adjacency_list.get(hub2).append(hub1)

            self._update_hub_distance(hub1=hub1, hub2=hub2, distance=distance)


    def get_distance(self, start_hub: Hub, end_hub: Hub) -> float:
        if not self.adjacency_list[start_hub] or end_hub not in self.adjacency_list:
            return math.inf
        else:
            for adj_node in self.adjacency_list.get(start_hub):
                if adj_node == end_hub:
                    return self.distance.get((start_hub, adj_node))
            return math.inf

    def _initialize_hubs(self) -> List[Hub]:

        queue: List[Hub] = []
        for hub in self.adjacency_list:
            hub.distance = math.inf
            hub.previous_hub = None
            queue.append(hub)

        return queue

    def _get_hub_with_smallest_distance(self, unvisited_queue: List[Hub]) -> Hub:

        sm_index: int = 0
        for i in range(1, unvisited_queue.__len__()):
            if unvisited_queue[i].distance < unvisited_queue[sm_index].distance:
                sm_index = i

        return unvisited_queue.pop(sm_index)

    def _update_hub_distance(self, hub1: Hub, hub2: Hub, distance: float):
        self.distance[(hub1, hub2)]: float = distance
        self.distance[(hub2, hub1)]: float = distance


    def dijkstra_shortest_path(self, start_hub: Hub) -> None:
        """
        Applies Dijkstra's shortest path algorithm to the graph, updating distance values
        if a shorter path from the start hub to a hub is found.

        Args
            start_hub (Hub): The starting hub for the shortest path.
        """
        # Initialize all hubs as unvisited and set the distance to infinity
        unvisited_queue: List[Hub] = self._initialize_hubs()

        # Distance to starting hub is zero
        start_hub.distance = 0.0

        # Visit each hub in the graph, then remove it from the unvisited queue
        while unvisited_queue:
            # Visit the hub with the smallest distance
            current_hub: Hub = self._get_hub_with_smallest_distance(unvisited_queue=unvisited_queue)
            # Check the distance to each neighbor hub
            for neighbor_hub in self.adjacency_list.get(current_hub):
                dist: float = self.distance.get((current_hub, neighbor_hub))
                alt_path_dist: float = current_hub.distance + dist

                # Update distance and previous hub if a shorter path is found
                if alt_path_dist < neighbor_hub.distance:
                    self._update_hub_distance(hub1=start_hub, hub2=neighbor_hub, distance=alt_path_dist)
                    neighbor_hub.distance = alt_path_dist
                    neighbor_hub.previous_hub = current_hub