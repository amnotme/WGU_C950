from typing import List


class Truck:

    """A class used to create a truck object that will hold a package object.

    Attributes:
        truck: A list of package objects.
        speed: The speed of the truck in miles per hour.
        miles: The number of miles the truck has traveled.
        capacity: The maximum capacity of the truck in terms of the number of packages it can hold.
        status: The current status of the truck, such as "At HUB" or "Out for Delivery".
    """

    def __init__(self, capacity: int = 16) -> None:
        self.truck: List[Package] = []
        self.speed: float = 18
        self.miles: float = 0
        self.capacity: int = capacity
        self.status: str = 'AT HUB'

    """
    Complexity: O(1)
    """
    def add_package(self, package: Package) -> None:
        """Adds a package to the truck.

        Args:
            package: The package to add to the truck.
        """
        if len(self.truck) < self.capacity:
            self.truck.append(package)
        else:
            raise ValueError('Truck is full.')

    """
    Complexity: O(1)
    """
    def remove_package(self, package: Package) -> None:
        """Removes a package from the truck.

        Args:
            package: The package to remove from the truck.
        """
        self.truck.remove(package)

    """
    Complexity: O(1)
    """
    def add_miles(self, miles: float) -> None:
        """Adds miles to the truck's odometer.

        Args:
            miles: The number of miles to add to the odometer.
        """
        self.miles += miles

    """
    Complexity: O(1)
    """
    def set_status(self, status: str) -> None:
        """Sets the truck's status.

        Args:
            status: The new status of the truck.
        """
        self.status = status
