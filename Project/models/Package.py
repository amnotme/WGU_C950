from typing import Any


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

    def __init__(
        self,
        package_id: str,
        address: str,
        city: str,
        state: str,
        zipcode: str,
        delivery_time: str,
        weight: str,
        status: str,
        notes: str
    ) -> None:
        self.package_id: str = package_id
        self.address: str = address
        self.city: str = city
        self.state: str = state
        self.zipcode: str = zipcode
        self.delivery_time: str = delivery_time
        self.weight: str = weight
        self.status: str = status
        self.notes: str = notes

    """
    Complexity: O(1)
    """
    def set_id(self, package_id: str) -> None:
        self.package_id = package_id

    """
    Complexity: O(1)
    """
    def set_address(self, address: str) -> None:
        self.address = address

    """
    Complexity: O(1)
    """
    def set_city(self, city: str) -> None:
        self.city = city

    """
    Complexity: O(1)
    """
    def set_state(self, state: str) -> None:
        self.state = state

    """
    Complexity: O(1)
    """
    def set_zipcode(self, zipcode: str) -> None:
        self.zipcode = zipcode

    """
    Complexity: O(1)
    """
    def set_delivery_time(self, delivery_time: str) -> None:
        self.delivery_time = delivery_time

    """
    Complexity: O(1)
    """
    def set_status(self, status: str) -> None:
        self.status = status

    """
    Complexity: O(1)
    """
    def set_notes(self, notes: str) -> None:
        self.notes = notes

    """
    Complexity: O(1)
    """
    def __repr__(self) -> str:
    """Returns a string representation of the package object.

    Returns:
        A string representation of the package object.
    """
        return (
            f"Package(package_id='{self.package_id}', "
            f"address='{self.address}', "
            f"city='{self.city}', "
            f"state='{self.state}', "
            f"zipcode='{self.zipcode}', "
            f"delivery_time='{self.delivery_time}', "
            f"weight='{self.weight}', "
            f"status='{self.status}', "
            f"notes='{self.notes}')"
        )
