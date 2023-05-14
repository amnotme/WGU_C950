from dataclasses import dataclass, field
from typing import List

from models.package import Package
from constants import AT_HUB_TEXT, MAX_TRUCK_CAPACITY

@dataclass
class Truck:

    """
        A dataclass used to create a truck object that will hold a
        package objects.

    Attributes:
        packages: A list of package objects.
        speed: The speed of the truck in miles per hour.
        miles: The number of miles the truck has traveled.
        capacity: The maximum capacity of the truck in terms of the number
            of packages it can hold.
        status: The current status of the truck, such as
            "AT HUB" or "Out for Delivery".
    """

    truck_id: int
    packages: List[Package] = field(default_factory=list)
    speed: float = field(default_factory=lambda: 0.0)
    miles: float = field(default_factory=lambda: 0.0)
    capacity: int = field(default_factory=lambda: MAX_TRUCK_CAPACITY)
    status: str = field(default_factory=lambda: AT_HUB_TEXT)

    def __repr__(self):
        """
        Returns a string representation of the Truck Id .

        Returns:
            A string representation of the Truck id.
        """
        return f"{self.truck_id}"

    def load_truck(self, package: Package) -> None:
        """
        Loads a Package object into a Truck object.

        Args:
            package (Package): Package object
        Returns:
            None
        """
        if isinstance(package, Package.__class__):
            self.packages.append(package)
