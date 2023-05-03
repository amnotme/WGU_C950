from dataclasses import dataclass
from typing import List

from models.package import Package


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
    packages: List[Package]
    speed: float
    miles: float
    capacity: int
    status: str
