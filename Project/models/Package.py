import datetime
from dataclasses import dataclass


@dataclass
class Package:

    """A dataclass to create a package object that then gets
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

    package_id: int
    address: str
    city: str
    state: str
    zipcode: int
    delivery_time: datetime
    weight: float
    status: str
    notes: str
