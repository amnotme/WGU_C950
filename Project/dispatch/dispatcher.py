from typing import List, Union, Any

from constants import (
    DISTANCES_DATA_FILE,
    PACKAGES_DATA_FILE,
    MAX_NUMBER_OF_TRUCKS_TO_DISPATCH,
    MAX_NUMBER_OF_PACKAGES_TO_DELIVER,
    MAX_TRUCK_CAPACITY,
    AT_HUB_TEXT,
)

from models.hub import Hub
from models.package import Package
from models.truck import Truck
from src.data_loader import Loader
from src.graph import Graph
from src.parser import Parser
from src.hash_map import HashMap
from utils.visualizer import visualize_graph

# from src.graph_impl import Graph


class Dispatcher:

    graph: Graph
    hubs: List[Hub]
    indexed_packages: HashMap
    trucks: List[Truck] = []

    def __init__(self):
        self.hubs = self._parse_hubs()
        self.indexed_packages = self._parse_packages()
        self.graph = self._load_graph()
        self.prep_trucks_for_dispatch()

    def _parse_hubs(self):
        hubs_parser: Parser = Parser(file_path=DISTANCES_DATA_FILE)
        return Loader.load_hubs(hubs_parser=hubs_parser)

    def _parse_packages(self):
        packages_parser: Parser = Parser(file_path=PACKAGES_DATA_FILE)
        packages: List[Package] = Loader.load_packages(packages_parser=packages_parser)
        indexed_packages: HashMap = HashMap(size=40)
        for package in packages:
            indexed_packages.add(
                key=package.package_id, value=package
            )
        return indexed_packages


    def _load_graph(self):
        graph = Graph()
        distances_parser: Parser = Parser(file_path=DISTANCES_DATA_FILE)
        graph = Loader.load_graph_hubs(graph=graph, hubs=self.hubs)
        return Loader.load_graph_distances(
            graph=graph,
            distances_parser=distances_parser,
            hubs=self.hubs
        )

    def prep_trucks_for_dispatch(
        self,
        trucks_to_dispatch: int = MAX_NUMBER_OF_TRUCKS_TO_DISPATCH
    ) -> None:
        for truck_id in range (1, trucks_to_dispatch + 1):
            self.trucks.append(
                Truck(truck_id=truck_id)
            )

    def _add_shortest_paths_to_graph(self):
        for hub in self.graph.adjacency_list:
            self.graph.dijkstra_shortest_path(start_hub=hub)

    # def _add_shortest_paths_to_graph(self):
    #     all_elements = self.graph.adjacency_list.get_all_elements()
    #     for node in all_elements:
    #         self.graph.dijkstra_shortest_path(node)

    def _graph_visualize(self):
        visualize_graph(self.graph)

    def clear_out_trucks(self):
        for truck in self.trucks:
            truck.packages.clear()
            truck.status = AT_HUB_TEXT
            truck.speed = 0.0
            truck.miles = 0.0
            truck.capacity = MAX_TRUCK_CAPACITY

    def clear_package_warehouse(self):
        self.indexed_packages.clear()