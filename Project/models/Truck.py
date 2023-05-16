from dataclasses import dataclass, field
from typing import List
from datetime import datetime, timedelta, time
from models.package import Package
from constants import AT_HUB_TEXT, MAX_TRUCK_CAPACITY, MAX_TRUCK_DISTANCE_PER_SECOND, DELIVERY_DATE

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


    def update_miles_driven(self, miles_traveled: float):
        self.miles += miles_traveled


    def update_truck_clock(self, distance_traveled: float, current_clock: time):

        delta_time: timedelta = timedelta(
            seconds=distance_traveled / self.speed
        )

        elapsed_time: time = time(
            hour=delta_time.seconds // 3600,
            minute=(delta_time.seconds // 60) % 60,
            second=delta_time.seconds % 60
        )

        date_time_from_elapsed_time: datetime = datetime.combine(
            date=DELIVERY_DATE, time=elapsed_time
        )

        date_time_from_current_clock: datetime = datetime.combine(
            date=DELIVERY_DATE, time=current_clock
        )

        new_truck_time: datetime = date_time_from_elapsed_time + timedelta(
            hours=date_time_from_current_clock.hour,
            minutes=date_time_from_current_clock.minute,
            seconds=date_time_from_current_clock.second
        )

        self.truck_clock = new_truck_time
        return (new_truck_time.time(), delta_time.seconds)


    def deliver_package(self, package: Package):
        package.status = f'Package delivered at {self.truck_clock.time()}'
        self.packages.remove(package)




