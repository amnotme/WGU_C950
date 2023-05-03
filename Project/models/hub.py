import math


class Hub:
    """
    Model class for a hub.  A hub is a location / node.

    Args:
        hub_name: The name of the hub.
        address: The address of the hub.
        zipcode: The zipcode of the hub.

    Attributes:
        hub_name: The name of the hub.
        address: The address of the hub.
        zipcode: The zipcode of the hub.
        previous_hub: The previous hub in the shortest path from the start hub.
        distance: The distance from the start hub to this hub.
    """
    def __init__(self, hub_name: str, address: str, zipcode: int):
        """
        Initializes a new Hub object.

        Args:
            hub_name (str): The name of the hub.
            address (str): The address of the hub.
            zipcode (int): The zipcode of the hub.
        """
        self.hub_name: str = hub_name
        self.address: str = address
        self.zipcode: int = zipcode
        self.previous_hub: "Hub" = None
        self.distance: float = math.inf

    def __repr__(self):
        """
        Returns a string representation of the hub.

        Returns:
            A string representation of the hub.
        """
        return f"{self.address}"

    def __lt__(self, other: "Hub") -> bool:
        """
        Less than '<' monkey patch to compare distances.

        Args:
            other: The other hub to compare to.

        Returns:
            True if the distance to this hub is less than the distance
            to the other hub.
        """
        return self.distance < other.distance
