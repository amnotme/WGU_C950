from typing import List, Union, Any
from datetime import datetime, time

from constants import (
    DISTANCES_DATA_FILE,
    PACKAGES_DATA_FILE,
    MAX_NUMBER_OF_TRUCKS_TO_DISPATCH,
    MAX_NUMBER_OF_PACKAGES_TO_DELIVER,
    MAX_TRUCK_CAPACITY,
    AT_HUB_TEXT,
    TRUCK_ONE_PACKAGES,
    TRUCK_TWO_PACKAGES,
    TRUCK_THREE_PACKAGES,
    DELIVERY_DATE
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

    def load_truck_with_packages(self, truck_id: int) -> None:

        truck_to_load: Truck
        packages_to_load: List[int]

        if truck_id == 1:
            packages_to_load = TRUCK_ONE_PACKAGES
        if truck_id == 2:
            packages_to_load = TRUCK_TWO_PACKAGES
        if truck_id == 3:
            packages_to_load = TRUCK_THREE_PACKAGES


        for truck in self.trucks:
            if truck.truck_id == truck_id:
                truck_to_load = truck
                break

        if isinstance(truck_to_load, Truck):
            for package_number in packages_to_load:
                package: Package = self.indexed_packages.get(key=package_number)
                truck_to_load.load_truck(package=package)


    def begin_delivery(self, truck, begin_time=time(8, 0), end_time=time(17, 0)):
        """
        Simulates a truck route delivering the loaded packages.  Returns the earlier of: time the route
        completes or the specified end_time.

        The truck starts at the hub location, then drives to each address to deliver packages, in order
        by the delivery deadline.  Uses a greedy algorithm to determine the next nearest address. The
        truck returns to the hub when all packages have been delivered.

        :param truck: the truck to drive the route
        :type truck: Truck
        :param begin_time: optional time to begin route
        :type begin_time: datetime.datetime
        :param end_time: optional time to end the route (default: EOD)
        :type end_time: datetime.datetime
        :return: earlier of: the time the route completes, or the optional specified end_time
        :rtype: datetime.datetime
        """
        truck.status = "Out on deliveries"
        # Check if there are any packages to deliver.
        if len(truck.packages) == 0:
            return begin_time

        # Sort the packages by delivery deadline.
        truck.packages = sorted(truck.packages, key=lambda package: package.delivery_time)

        hubs_to_deliver: List[Hub] = [
            self.graph.get_hub_by_address(
                hub_address=package.address
            ) for package in truck.packages
        ]
        # Initialize the current location and time.
        start_loc: Hub = next(iter(self.graph.adjacency_list))
        current_location: Hub = start_loc
        current_time: time = begin_time

        # Initialize the remaining time.
        remaining_time = self.time_difference(
            start_time=begin_time,
            end_time=end_time
        )

        # Initialize the list of visited locations.
        visited_locations: List[Hub] = []

        # While there are still packages to deliver and there is still time remaining:
        while len(hubs_to_deliver) > 0 and remaining_time > 0:
            # Find the next package to deliver.
            # package = packages.pop(0)

            # next_hub: Hub = self.graph.get_hub_by_address(hub_address=package.address)
            # Calculate the distance to the next package.
            # TODO we could probably sort by all packages distances to get the one with the smallest distances
            next_hub, distance = self.next_nearest_hub(
                current_hub=current_location,
                unvisited_queue=hubs_to_deliver
            )

            # If there is enough time remaining to deliver the next package:
            seconds_to_drive_to_next_hub: float = distance / truck.speed
            if remaining_time >= seconds_to_drive_to_next_hub:
                # Drive to the next package.
                truck.update_miles_driven(miles_traveled=distance)

                current_time, elapsed_time = truck.update_truck_clock(
                    distance_traveled=distance,
                    current_clock=current_time
                )

                remaining_time -= elapsed_time

                # Deliver the next package.
                for package in truck.packages:
                    temp_hub: Hub = self.graph.get_hub_by_address(
                        hub_address=package.address
                    )
                    if temp_hub.address == next_hub.address:
                        truck.deliver_package(package=package)


                # Update the current location and time.
                current_location = next_hub
                # current_time = current_time + datetime.timedelta(seconds=distance / 18 * 60)

                # Add the current location to the list of visited locations.
                visited_locations.append(current_location)

            # Otherwise, return the current time.
            else:
                truck.status = AT_HUB_TEXT
                return current_time

        # Return the time when the route is completed.
        truck.status = AT_HUB_TEXT
        return current_time


    def time_difference(self, start_time: time, end_time: time):
        start_date: datetime = datetime.combine(DELIVERY_DATE, start_time)
        end_date: datetime = datetime.combine(DELIVERY_DATE, end_time)

        return ((end_date - start_date).seconds)

    def next_nearest_hub(self, current_hub: Hub, unvisited_queue: List[Hub]):
        smallest_distance_index: int = 0
        initial_shortest_distance: float = self.graph.distance.get(
            (current_hub, unvisited_queue[smallest_distance_index])
        )
        for i in range(1, unvisited_queue.__len__()):
            next_shortest_distance: float = self.graph.distance.get(
                (current_hub, unvisited_queue[i])
            )
            if (
                next_shortest_distance is not None and
                next_shortest_distance < initial_shortest_distance
            ):
                initial_shortest_distance = next_shortest_distance
                smallest_distance_index = i

        distance_to_travel: float = self.graph.distance.get(
                (current_hub, unvisited_queue[smallest_distance_index])
            )
        if distance_to_travel is None:
            # We are at the last delivery stop so we will deliver it here.
            return unvisited_queue.pop(smallest_distance_index), 0
        else:
            return unvisited_queue.pop(smallest_distance_index), distance_to_travel


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

    def end_delivery_report(self):

        total_distance: float = 0.0
        truck_times: List[datetime] = []
        self.indexed_packages.display_package_status()
        for truck in self.trucks:
            truck_times.append(truck.truck_clock)
            print(f"Status: [{truck.status}]. Truck {truck.truck_id} traveled: {round(truck.miles, 2)} miles.")
            total_distance += round(truck.miles, 2)

        print(f"Total distance traveled: {round(total_distance, 2)} miles.")
        print(f"All packages have been delivered as of {max(truck_times)}")



