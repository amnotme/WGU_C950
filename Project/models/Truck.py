from dataclasses import dataclass, field
from datetime import datetime, time, timedelta
from typing import List

from constants import (
    AT_HUB_TEXT, DELIVERY_DATE, MAX_TRUCK_CAPACITY,
    MAX_TRUCK_DISTANCE_PER_SECOND
)

from models.package import Package


@dataclass
class Truck:
    """
        A dataclass used to create a truck object that will hold a
        package objects.

    Attributes:
        packages: A list of package objects.
        speed: The speed of the truck in miles per second.
        miles: The number of miles the truck has traveled.
        capacity: The maximum capacity of the truck in terms of the number
            of packages it can hold.
        status: The current status of the truck, such as
            "AT HUB" or "Out for Delivery".
        truck_clock: A truck object's internal clock for delivery confirmation
    """

    truck_id: int
    packages: List[Package] = field(default_factory=list)
    speed: float = field(default_factory=lambda: MAX_TRUCK_DISTANCE_PER_SECOND)
    miles: float = field(default_factory=lambda: 0.0)
    capacity: int = field(default_factory=lambda: MAX_TRUCK_CAPACITY)
    status: str = field(default_factory=lambda: AT_HUB_TEXT)
    truck_clock: datetime = field(default_factory=lambda: datetime.today())

    def __repr__(self):
        """
        Returns a string representation of the Truck Id .

        Returns:
            A string representation of the Truck id.
        """
        return f"{self.truck_id}"

    def load_truck(self, package: Package, starting_time: datetime = DELIVERY_DATE) -> None:
        """
        Loads a Package object into a Truck object.

        Args:
            package (Package): Package object
        Returns:
            None
        """
        if isinstance(package, Package) and self.capacity != 0:
            self.packages.append(package)
            self.capacity -= 1
            self.truck_clock = starting_time
            self.speed = MAX_TRUCK_DISTANCE_PER_SECOND
            self.status = f"En route via truck no. [{self.truck_id}]"

    def update_miles_driven(self, miles_traveled: float):
        """
        Updates the total miles driven by the truck.

        Args:
            miles_traveled (float): The number of miles traveled to be added to the current total.

        """
        # Add the miles traveled to the current total miles
        self.miles += miles_traveled

    def update_truck_clock(self, distance_traveled: float, current_clock: time):
        """
        Updates the truck's clock based on the distance traveled and current clock time.

        Args:
            distance_traveled (float): The distance traveled by the truck.
            current_clock (time): The current time on the truck's clock.

        Returns:
            Tuple[time, int]: A tuple containing the new truck time (time object) and the elapsed time in seconds.

        """
        # Calculate the elapsed time based on the distance traveled and the truck's speed
        delta_time: timedelta = timedelta(seconds=distance_traveled / self.speed)

        # Convert the elapsed time to a time object
        elapsed_time: time = time(
            hour=delta_time.seconds // 3600,
            minute=(delta_time.seconds // 60) % 60,
            second=delta_time.seconds % 60
        )

        # Create a datetime object combining the delivery date with the elapsed time
        date_time_from_elapsed_time: datetime = datetime.combine(
            date=DELIVERY_DATE, time=elapsed_time
        )

        # Create a datetime object combining the delivery date with the current clock time
        date_time_from_current_clock: datetime = datetime.combine(
            date=DELIVERY_DATE, time=current_clock
        )

        # Calculate the new truck time by adding the elapsed time to the current clock time
        new_truck_time: datetime = date_time_from_elapsed_time + timedelta(
            hours=date_time_from_current_clock.hour,
            minutes=date_time_from_current_clock.minute,
            seconds=date_time_from_current_clock.second
        )

        # Update the truck's clock with the new time
        self.truck_clock = new_truck_time

        # Return the new truck time as a time object and the elapsed time in seconds
        return (new_truck_time.time(), delta_time.seconds)

    def deliver_package(self, package: Package, packages_delivered: List[Package]):
        """
        Delivers a package and updates its status.

        Args:
            package (Package): The package to be delivered.
            packages_delivered (List[Package]): A list to store delivered packages.

        Notes:
            If the package is not found in self.packages, it prints the package (for error handling).
            Otherwise, it updates the package status, appends it to packages_delivered, and removes it from self.packages.

        """
        # Check if the package is in the list of packages to be delivered
        if package not in self.packages:
            # Print the package (for error handling or debugging purposes)
            print(package)
        else:
            # Update the package status with the delivery information
            package.status = f'Package delivered at {self.truck_clock.time()} from truck no. [{self.truck_id}]'

            # Append the delivered package to the list of packages delivered
            packages_delivered.append(package)

            # Remove the delivered package from the list of packages to be delivered
            self.packages.remove(package)
