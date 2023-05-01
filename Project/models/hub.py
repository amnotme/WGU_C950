from typing import Any, Union
from dataclasses import dataclass
import datetime

# @dataclass(unsafe_hash=True)
class Hub:

    def __init__(self, hub_name, address, zipcode):
        self.hub_name = hub_name
        self.address = address
        self.zipcode = zipcode
        self.previous_hub: [Any] = None
        self.distance = float("inf")

    def __repr__(self):
        """
        Returns a formatted string showing the street address of the location.

        :return: a formatted string showing the street address of the location
        :rtype: str
        """
        return "{}".format(self.address)

    # hub_name: str
    # address: str
    # zipcode: int
    # previous_hub: Any = None
    # distance: float = float("inf")