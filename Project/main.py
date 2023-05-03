from typing import List, Union

from constants import DISTANCES_DATA_FILE, PACKAGES_DATA_FILE

from models.hub import Hub
from models.package import Package
from models.truck import Truck
from src.data_loader import Loader
from src.graph import Graph
from src.parser import Parser
from utils.visualizer import visualize_graph

graph = Graph()

hubs_parser: Parser = Parser(file_path=DISTANCES_DATA_FILE)
hubs: List[Hub] = Loader.load_hubs(hubs_parser=hubs_parser)

packages_parser: Parser = Parser(file_path=PACKAGES_DATA_FILE)
packages: List[Package] = Loader.load_packages(packages_parser=packages_parser)

distances_parser: Parser = Parser(file_path=DISTANCES_DATA_FILE)

graph = Loader.load_graph_hubs(graph=graph, hubs=hubs)
graph = Loader.load_graph_distances(graph=graph, distances_parser=distances_parser, hubs=hubs)

for node in graph.adjacency_list:
    graph.dijkstra_shortest_path(node)

graph

# Print the shortest paths
# print("The shortest paths for all nodes in the adjacency list are:")
# for node, shortest_path in shortest_paths.items():
#     print(f"node {node} shortest_path: {shortest_path}")

# visualize_graph(graph=graph)
