from src.parser import Parser
from src.graph import Graph
from typing import List, Union
from models.truck import Truck
from models.hub import Hub
from models.package import (
    Package
)
from src.data_loader import Loader
from constants import (
    DISTANCES_DATA_FILE,
    PACKAGES_DATA_FILE
)

graph = Graph()

hubs_parser: Parser = Parser(file_path=DISTANCES_DATA_FILE)
hubs: List[Hub] = Loader.load_hubs(hubs_parser=hubs_parser)

packages_parser: Parser = Parser(file_path=PACKAGES_DATA_FILE)
packages: List[Package] = Loader.load_packages(packages_parser=packages_parser)

distances_parser: Parser = Parser(file_path=DISTANCES_DATA_FILE)

graph = Loader.load_graph_hubs(graph=graph, hubs=hubs)
graph = Loader.load_graph_distances(graph=graph, distances_parser=distances_parser, hubs=hubs)

shortest_paths = {}
for node in graph.adjacency_list:
    shortest_paths[node] = graph.a_star_shortest_path(node)

# Print the shortest paths
print("The shortest paths for all nodes in the adjacency list are:")
for node, shortest_path in shortest_paths.items():
    print("The shortest path from node to {} is: {}".format(node, shortest_path))