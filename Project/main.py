from typing import List, Union

from constants import DISTANCES_DATA_FILE, PACKAGES_DATA_FILE

from models.hub import Hub
from models.package import Package
from models.truck import Truck
from src.data_loader import Loader
from src.graph import Graph
from src.parser import Parser
from utils.visualizer import visualize_graph
# from src.graph_impl import Graph

# graph = Graph()
#
# hubs_parser: Parser = Parser(file_path=DISTANCES_DATA_FILE)
# hubs: List[Hub] = Loader.load_hubs(hubs_parser=hubs_parser)
#
# packages_parser: Parser = Parser(file_path=PACKAGES_DATA_FILE)
# packages: List[Package] = Loader.load_packages(packages_parser=packages_parser)
#
# distances_parser: Parser = Parser(file_path=DISTANCES_DATA_FILE)
#
# graph = Loader.load_graph_hubs(graph=graph, hubs=hubs)
# graph = Loader.load_graph_distances(graph=graph, distances_parser=distances_parser, hubs=hubs)
#

#
# graph


class Main:

    graph: Graph
    hubs: List[Hub]
    packages: List[Package]


    def __init__(self):
        self.hubs = self._parse_hubs()
        self.packages = self._parse_packages()
        self.graph = self._load_graph()

    def _parse_hubs(self):
        hubs_parser: Parser = Parser(file_path=DISTANCES_DATA_FILE)
        return Loader.load_hubs(hubs_parser=hubs_parser)

    def _parse_packages(self):
        packages_parser: Parser = Parser(file_path=PACKAGES_DATA_FILE)
        return Loader.load_packages(packages_parser=packages_parser)

    def _load_graph(self):
        graph = Graph()
        distances_parser: Parser = Parser(file_path=DISTANCES_DATA_FILE)
        graph = Loader.load_graph_hubs(graph=graph, hubs=self.hubs)
        return Loader.load_graph_distances(graph=graph, distances_parser=distances_parser, hubs=self.hubs)


    def _add_shortest_paths_to_graph(self):
        for node in self.graph.adjacency_list:
            self.graph.dijkstra_shortest_path(node)



main = Main()


# all_elements = main.graph.adjacency_list.get_all_elements()
# for node in all_elements:
#     main.graph.dijkstra_shortest_path(node)
#
# main




main