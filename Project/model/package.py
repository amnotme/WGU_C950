class Package:
    """A model to create a package object that then gets
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

    def __init__(self, package_id, address, city, state, zipcode, delivery_time, weight, status, notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.delivery_time = delivery_time
        self.weight = weight
        self.status = status
        self.notes = notes

    def __repr__(self):
        return f"Package ID: {self.package_id}, Delivery address: {self.address}, Deliver by: {self.delivery_time}, Status: {self.status}"
