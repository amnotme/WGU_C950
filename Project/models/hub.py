from typing import Any
import math

class Hub:

    def __init__(self, hub_name, address, zipcode):
        self.hub_name = hub_name
        self.address = address
        self.zipcode = zipcode
        self.previous_hub: [Any] = None
        self.distance = math.inf

    def __repr__(self):
        """Representation of hub"""
        return f"{self.address}"

    def __lt__(self, other):
        """Less than monkey patch to compare distances."""
        return self.distance < other.distance
