from datetime import datetime, time, timedelta
from typing import List, Optional, Tuple
import copy
from constants import (
    AT_HUB_TEXT, BR_DELAYED_UNTIL_NINE_FIVE,
    BR_MUST_BE_DELIVERED, BR_MUST_BE_DELIVERED_WITH_ONE,
    BR_MUST_BE_DELIVERED_WITH_THREE,
    BR_MUST_BE_DELIVERED_WITH_TWO, BR_ONLY_IN_TRUCK_TWO,
    BR_RIGHT_ADDRESS,
    BR_TIME_FOR_NEW_ADDRESS_FOR_PACKAGE_NINE,
    BR_WRONG_ADDRESS, DEFAULT_DELIVERY_END_TIME,
    DEFAULT_DELIVERY_START_TIME,
    DEFAULT_MAXIMUM_NUMBER_OF_PACKAGES, DELAYED_START_TIME,
    DELIVERY_DATE,
    MAX_NUMBER_OF_TRUCKS_TO_DISPATCH, MAX_TRUCK_CAPACITY,
    TRUCK_ONE_PACKAGES,
    TRUCK_THREE_PACKAGES, TRUCK_TWO_PACKAGES
)

from models.hub import Hub
from models.package import Package
from models.truck import Truck
from src.data_loader import Loader
from src.graph import Graph
from src.hash_map import HashMap
from src.parser import Parser


class Dispatcher:
    graph: Graph
    hubs: List[Hub]
    indexed_packages: HashMap
    trucks: List[Truck]
    business_rules: HashMap

    def __init__(self):
        """
        Initializes a Dispatcher object.

        This method initializes the Dispatcher object by parsing and loading the hubs,
        parsing and indexing the packages, loading the graph, and preparing trucks for dispatch.

        Args:
            self: The current instance of the class.

        Returns:
            None.
        """

        self.hubs = self._parse_hubs()
        self.indexed_packages = self._parse_packages()
        self.graph = self._load_graph()
        self.trucks = self.prep_trucks_for_dispatch()
        self.business_rules = self._provide_logistical_rules_to_dispatch()

    def _parse_hubs(self):
        """
        Parses and loads the hubs.

        This method initializes a hubs parser, loads the hubs from the data file,
        and returns the loaded hubs.

        Args:
            self: The current instance of the class.

        Returns:
            The loaded hubs.
        """

        # Initialize a hubs parser
        hubs_parser: Parser = Parser()

        # Load the hubs from the data file
        return Loader.load_hubs_from_csv(hubs_parser=hubs_parser)

    def _parse_packages(self):
        """
        Parses and indexes the packages.

        This method initializes a packages parser, loads the packages from the data file,
        and indexes them using a hash map.

        Args:
            self: The current instance of the class.

        Returns:
            The indexed packages stored in a hash map.
        """

        # Initialize a packages parser
        packages_parser: Parser = Parser()

        # Load the packages from the data file
        packages: List[Package] = Loader.load_packages_from_csv(packages_parser=packages_parser)

        # Initialize a hash map to index the packages
        indexed_packages: HashMap = HashMap(
            size=DEFAULT_MAXIMUM_NUMBER_OF_PACKAGES
        )

        # Index each package using its package ID
        for package in packages:
            indexed_packages.add(
                key=package.package_id, value=package
            )

        # Return the indexed packages stored in the hash map
        return indexed_packages

    def _load_graph(self):
        """
        Loads the graph with hubs and distances.

        This method initializes a graph object, loads the hubs into the graph,
        and loads the distances between the hubs from the distances data file.

        Args:
            self: The current instance of the class.

        Returns:
            The loaded graph object.
        """

        # Initialize a new graph object
        graph = Graph()

        # Load the hubs into the graph
        graph = Loader.load_graph_hubs(graph=graph, hubs=self.hubs)

        # Load the distances between the hubs from the distances data file
        distances_parser: Parser = Parser()
        return Loader.load_graph_distances_from_csv(
            graph=graph,
            hubs=self.hubs
        )

    def _provide_logistical_rules_to_dispatch(self) -> HashMap:
        """
        Provides logistical rules to dispatch based on package notes.

        Returns:
            HashMap: A HashMap object containing package IDs as keys and associated notes as values.
        """
        # Initialize a HashMap to store the business rules
        business_rules = HashMap(
            DEFAULT_MAXIMUM_NUMBER_OF_PACKAGES
        )

        # Iterate over all packages in the indexed_packages
        for package in self.indexed_packages.get_all_elements():
            # Add package ID as key and associated notes as value to the business_rules HashMap
            business_rules.add(key=package[1].package_id, value=package[1].notes)

        # Return the populated business_rules HashMap
        return business_rules

    def prep_trucks_for_dispatch(
            self,
            trucks_to_dispatch: int = MAX_NUMBER_OF_TRUCKS_TO_DISPATCH
    ) -> List[Truck]:
        """
        Prepares trucks for dispatch.

        This method prepares the specified number of trucks for dispatch by creating
        truck objects and adding them to the list of trucks.

        Args:
            self: The current instance of the class.
            trucks_to_dispatch: The number of trucks to prepare for dispatch (default: MAX_NUMBER_OF_TRUCKS_TO_DISPATCH).

        Returns:
            List of Truck objects.
        """
        trucks: List[Truck] = []
        for truck_id in range(1, trucks_to_dispatch + 1):
            # Create a new truck object with the specified truck ID
            trucks.append(
                Truck(truck_id=truck_id)
            )

        return trucks

    def load_truck_with_packages(self, truck_id: int) -> None:
        """
        Loads packages onto a specific truck.

        This method takes a truck ID as input and loads the corresponding packages onto
        the truck. The packages to load are determined based on the provided truck ID.

        Args:
            self: The current instance of the class.
            truck_id: The ID of the truck to load.

        Returns:
            None.
        """

        truck_to_load: Optional[Truck] = None
        packages_to_load: List[int] = []

        # Determine the packages to load based on the truck ID
        if truck_id == 1:
            packages_to_load = TRUCK_ONE_PACKAGES
        if truck_id == 2:
            packages_to_load = TRUCK_TWO_PACKAGES
        if truck_id == 3:
            packages_to_load = TRUCK_THREE_PACKAGES

        # Find the truck to load based on the truck ID
        for truck in self.trucks:
            if truck.truck_id == truck_id:
                truck_to_load = truck
                break

        # Load the packages onto the truck
        if isinstance(truck_to_load, Truck):
            for package_number in packages_to_load:
                package: Package = self.indexed_packages.get(key=package_number)
                package.status = f"En route for delivery on truck no. {truck_to_load.truck_id}"
                truck_to_load.load_truck(package=package)

    def begin_delivery(
            self,
            truck: Truck,
            begin_time=DEFAULT_DELIVERY_START_TIME,
            end_time=DEFAULT_DELIVERY_END_TIME
    ):
        """
        Begins the delivery process for a truck.

        This method takes a truck, a begin time, and an end time as input and starts
        the delivery process for the truck. It sorts the packages by delivery deadline,
        determines the route to deliver the packages, and updates the truck's status,
        location, and time during the delivery process.

        Args:
            self: The current instance of the class.
            truck: The truck to begin delivery.
            begin_time: The begin time for delivery (default: 8:00 AM).
            end_time: The end time for delivery (default: 5:00 PM).

        Returns:
            The current time when the truck is at the hub or the end time if the delivery is complete.
        """

        # Update the truck status to "Out on deliveries"
        truck.status = "Out on deliveries"

        # Check if there are any packages to deliver
        if len(truck.packages) == 0:
            return begin_time

        # Sort the packages by delivery deadline
        truck.packages = sorted(truck.packages, key=lambda package: package.delivery_time)

        # Get the hubs to deliver the packages
        hubs_to_deliver: List[Hub] = [
            self.graph.get_hub_by_address(
                hub_address=package.address
            ) for package in truck.packages
        ]

        # Initialize the current location and time
        start_loc: Hub = next(iter(self.graph.adjacency_list))
        current_location: Hub = start_loc
        current_time: time = begin_time
        retry_hubs: List[Hub] = []
        packages_delivered: List[Package] = []
        # Initialize the remaining time
        remaining_time = self.calculate_remaining_time(
            start_time=begin_time,
            end_time=end_time
        )

        # While there are still packages to deliver and there is still time remaining
        validation_passes: bool = True
        while hubs_to_deliver and remaining_time > 0:
            # Find the next nearest hub to deliver a package
            next_hub, distance = self.next_nearest_hub(
                current_hub=current_location,
                unvisited_queue=hubs_to_deliver
            )

            # If there is enough time remaining to deliver the next package
            seconds_to_drive_to_next_hub: float = distance / truck.speed
            if remaining_time >= seconds_to_drive_to_next_hub:
                # Deliver the next package
                for package in truck.packages:
                    temp_hub: Hub = self.graph.get_hub_by_address(
                        hub_address=package.address
                    )
                    if (temp_hub.address == next_hub.address):
                        # Drive to the next package
                        if self._is_package_deliverable(
                                package=package,
                                truck=truck,
                                packages_delivered=packages_delivered,
                                time_to_get_to_destination=int(seconds_to_drive_to_next_hub)
                        ):
                            truck.update_miles_driven(miles_traveled=distance)
                            current_time, elapsed_time = truck.update_truck_clock(
                                distance_traveled=distance,
                                current_clock=current_time
                            )
                            remaining_time -= elapsed_time
                            truck.deliver_package(
                                package=package,
                                packages_delivered=packages_delivered
                            )
                            # Distance must be reset in case we have to drop off multiple
                            # packages at the same location.
                            distance = 0
                        else:
                            validation_passes = False

                # Update the current location and time
                if validation_passes:
                    current_location = next_hub
                else:
                    # When validation fails, we want to add the hub to the end of the queue.
                    retry_hubs.append(next_hub)
                    validation_passes = True

                if retry_hubs and not hubs_to_deliver:
                    # Our current queue has been exhausted but if there are hubs to retry
                    # We will add them here to give the driver an opportunity to pass by again.
                    while retry_hubs:
                        hubs_to_deliver.append(retry_hubs.pop(0))
            else:
                truck.status = AT_HUB_TEXT
                return current_time

        # Return the time when the route is completed
        truck.status = AT_HUB_TEXT
        packages_delivered.clear()
        return current_time

    def calculate_remaining_time(self, start_time: time, end_time: time) -> float:
        """
        Calculates the time difference between two time values.

        This method takes the start time and end time as input and calculates
        the time difference between them in seconds.

        Args:
            self: The current instance of the class.
            start_time: The start time.
            end_time: The end time.

        Returns:
            The time difference between the start time and end time in seconds.
        """

        # Combine the delivery date with the start and end times
        start_date: datetime = datetime.combine(DELIVERY_DATE, start_time)
        end_date: datetime = datetime.combine(DELIVERY_DATE, end_time)

        # Calculate the time difference in seconds
        time_diff: timedelta = end_date - start_date
        return time_diff.total_seconds()

    def next_nearest_hub(
            self,
            current_hub: Hub,
            unvisited_queue: List[Hub]
    ) -> Tuple[Hub, float]:
        """
        Finds the next nearest hub.

        This method takes the current hub and a list of unvisited hubs as input
        and returns the next nearest hub and the distance to travel to reach it.
        The next nearest hub is determined by comparing the distances between the
        current hub and all the unvisited hubs.

        Args:
            self: The current instance of the class.
            current_hub: The current hub.
            unvisited_queue: A list of unvisited hubs.

        Returns:
            A tuple containing the next nearest hub and the distance to travel to reach it.
        """

        # Initialize variables
        smallest_distance_index: int = 0
        initial_shortest_distance: float = self.graph.distance.get(
            (current_hub, unvisited_queue[smallest_distance_index])
        )

        # Find the next nearest hub
        for i, next_hub in enumerate(unvisited_queue[1:], start=1):
            next_shortest_distance: float = self.graph.distance.get(
                (current_hub, next_hub)
            )
            if initial_shortest_distance is None:
                print(initial_shortest_distance)
            if (
                    next_shortest_distance is not None and
                    next_shortest_distance < initial_shortest_distance
            ):
                initial_shortest_distance = next_shortest_distance
                smallest_distance_index = i

        # Get the distance to travel to the next nearest hub
        distance_to_travel: float = self.graph.distance.get(
            (current_hub, unvisited_queue[smallest_distance_index])
        )

        if distance_to_travel is None:
            # We are at the last delivery stop, so we will deliver it here.
            return unvisited_queue.pop(smallest_distance_index), 0
        else:
            return unvisited_queue.pop(smallest_distance_index), distance_to_travel

    def _add_shortest_paths_to_graph(self) -> None:
        """
        Adds shortest paths to the graph.

        This method iterates over each hub in the graph's adjacency list and
        computes the shortest paths using Dijkstra's algorithm from the current hub
        to all other hubs in the graph. The shortest paths are added to the graph.

        Args:
            self: The current instance of the class.

        Returns:
            None
        """

        # Iterate over hubs in the graph's adjacency list
        for hub in self.graph.adjacency_list:
            # Compute the shortest paths using Dijkstra's algorithm from the current hub
            self.graph.dijkstra_shortest_path(start_hub=hub)

    def clear_out_trucks(self):
        """
        Clears out the trucks.

        This method clears out each truck by performing the following actions:
        - Clears the packages associated with the truck
        - Resets the truck status to "At Hub"
        - Sets the truck speed to 0.0
        - Resets the truck miles traveled to 0.0
        - Resets the truck capacity to the maximum truck capacity

        Args:
            self: The current instance of the class.

        Returns:
            None
        """

        # Iterate over trucks
        for truck in self.trucks:
            # Clear the packages associated with the truck
            truck.packages.clear()

            # Reset truck status to "At Hub"
            truck.status = AT_HUB_TEXT

            # Set truck speed to 0.0
            truck.speed = 0.0

            # Reset truck miles traveled to 0.0
            truck.miles = 0.0

            # Reset truck capacity to the maximum truck capacity
            truck.capacity = MAX_TRUCK_CAPACITY

    def clear_package_warehouse(self):
        """
        Clears the package warehouse.

        This method clears the package warehouse by removing all the packages
        stored in the indexed package hashmap.

        Args:
            self: The current instance of the class.

        Returns:
            None
        """

        # Clear the indexed package dictionary
        self.indexed_packages.clear()

    def end_delivery_report(self, end_time: Optional[time] = None):
        """
        Generates and displays the end of delivery report.

        This method calculates and prints the total distance traveled
        by each truck, displays the status of all packages,
        and determines the latest completion time
        of all trucks for package delivery.

        Args:
            self: The current instance of the class.
        Returns:
            None
        """

        # Initialize variables
        total_distance: float = 0.0
        truck_times: List[datetime] = []

        # Display package status
        self.indexed_packages.display_package_status()

        # Iterate over trucks
        for truck in self.trucks:
            # Track truck clock times
            if not isinstance(truck.truck_clock, datetime) and end_time is not None:
                truck_times.append(datetime.combine(truck.truck_clock.today(), end_time))
            else:
                truck_times.append(truck.truck_clock)

            # Print truck status and traveled distance
            print(f"Status: [{truck.status}]. Truck {truck.truck_id} traveled: {round(truck.miles, 2)} miles.")

            # Update total distance
            total_distance += round(truck.miles, 2)

        # Print total distance traveled by all trucks
        print(f"Total distance traveled: {round(total_distance, 2)} miles.")

        # Print the latest truck time as the delivery completion time
        print(f"All delivery procedures have ended as of {max(truck_times)}")

    def _is_package_deliverable(
            self,
            package: Package,
            truck: Truck,
            packages_delivered: List[Package],
            time_to_get_to_destination: int
    ) -> bool:
        """
        Checks if a package is deliverable based on business rules.

        This method checks if a package is deliverable based on the business rules defined
        for the package. It takes into account the package, the truck, the list of packages
        already delivered, and the time it takes to get to the destination.

        Args:
            self: The current instance of the class.
            package: The package to be checked for deliverability.
            truck: The truck carrying the package.
            packages_delivered: The list of packages already delivered.
            time_to_get_to_destination: The time it takes to get to the destination in seconds.

        Returns:
            bool: True if the package is deliverable, False otherwise.
        """

        rule: str = self.business_rules.get(package.package_id)

        # There are no special notes. We can deliver this.
        if not rule:
            return True

        # Package has been delayed until 9:05 am.  We cannot deliver until after
        # that time.
        if rule == BR_DELAYED_UNTIL_NINE_FIVE:
            if truck.truck_clock.time() >= DELAYED_START_TIME:
                return True
            return False

        # A package that has been given a wrong address and only at 10:20 am can
        # this new address be communicated from dispatch to the truck, so
        # it can deliver the package.
        if rule == BR_WRONG_ADDRESS:
            added_time_time_to_get_to_destination: time = time(
                minute=(time_to_get_to_destination // 60) % 60,
                second=(time_to_get_to_destination % 60)
            )
            estimated_time_of_arrival: datetime = (
                    datetime.combine(date=DELIVERY_DATE, time=added_time_time_to_get_to_destination)
                    + timedelta(
                hours=truck.truck_clock.time().hour,
                minutes=truck.truck_clock.time().minute,
                seconds=truck.truck_clock.time().second
            )
            )
            if estimated_time_of_arrival.time() >= BR_TIME_FOR_NEW_ADDRESS_FOR_PACKAGE_NINE:
                package.address = BR_RIGHT_ADDRESS
                return True
            return False

        # A package that can only be delivered in truck number 2.
        if rule == BR_ONLY_IN_TRUCK_TWO:
            if truck.truck_id == 2:
                return True
            return False

        # Series of rules where packages need to be delivered along with other
        # similar packages.  These packages need to be in the same truck
        br_packages_count: int = 0
        if rule in BR_MUST_BE_DELIVERED:
            if rule == BR_MUST_BE_DELIVERED_WITH_ONE:
                for package in truck.packages:
                    if package.package_id == 13 or package.package_id == 15:
                        br_packages_count += 1
                for package in packages_delivered:
                    if package.package_id == 13 or package.package_id == 15:
                        br_packages_count += 1
                return br_packages_count == 2
            elif rule == BR_MUST_BE_DELIVERED_WITH_TWO:
                for package in truck.packages:
                    if package.package_id == 13 or package.package_id == 19:
                        br_packages_count += 1
                for package in packages_delivered:
                    if package.package_id == 13 or package.package_id == 19:
                        br_packages_count += 1
                return br_packages_count == 2
            elif rule == BR_MUST_BE_DELIVERED_WITH_THREE:
                for package in truck.packages:
                    if package.package_id == 19 or package.package_id == 15:
                        br_packages_count += 1
                for package in packages_delivered:
                    if package.package_id == 19 or package.package_id == 15:
                        br_packages_count += 1
                return br_packages_count == 2

    def _graph_visualize(self) -> None:
        """
        Visualizes the graph.

        This method visualizes the graph by calling a function to visualize it.

        Args:
            self: The current instance of the class.

        Returns:
            None.
        """

        visualize_graph(self.graph)
