from typing import Any
from dataclasses import dataclass

@dataclass
class Package:

    """A class to create a package object that then gets
    stored into a hash table and truck object.

    Attributes:
        package_id: The unique identifier of the package.
        address: The address of the destination.
        city: The city of the destination.
        state: The state of the destination.
        zipcode: The zip code of the destination.
        delivery_time: The delivery time of the package.
        weight: The weight of the package.
        status: The current status of the package.
        notes: Any additional notes about the package.
    """

    package_id: str
    address: str
    city: str
    state: str
    zipcode: str
    delivery_time: str
    weight: str
    status: str
    notes: str
