from typing import Any, List, Optional, Union

from constants import AT_HUB_TEXT


class HashMap:

    """A hash map for storing key-value pairs.

    Args:
        size: The size of the hash map.

    Attributes:
        size: The size of the hash map.
        table: A list of lists, where each inner list represents
        a bucket in the hash map.

    Methods:
        add: Adds a key-value pair to the hash map.
        get: Gets the value associated with a key in the hash map.
        remove: Removes a key-value pair from the hash map.
        contains: Checks if a key is present in the hash map.
        size: Gets the size of the hash map.
        clear: Clears the hash map.
    """

    def __init__(self, size: int = 100) -> None:
        self.size: int = size
        self.table: List[List[Any]] = [[] for _ in range(self.size)]

    def add(
        self,
        key: Union[object, Any],
        value: Any,
        object_key: Optional[str] = None
    ) -> bool:
        """Adds a key-value pair to the hash map.

        Args:
            key: The key to add.
            value: The value to add.

        Returns:
            True if the key-value pair was added successfully, False otherwise.
        """
        if object_key:
            hash_code = hash(key.__getattribute__(object_key)) % self.size
        else:
            hash_code = hash(key) % self.size
        bucket = self.table[hash_code]
        for i, kvp in enumerate(bucket):
            if kvp[0] == key:
                bucket[i] = (key, value)
                return True
        bucket.append((key, value))
        return True

    def get(self, key: Any, object_key: Optional[str] = None) -> Optional[Any]:
        """Gets the value associated with a key in the hash map.

        Args:
            key: The key to get the value for.

        Returns:
            The value associated with the key, or None
            if the key is not present in the hash map.
        """

        if object_key:
            hash_code = hash(key.__getattribute__(object_key)) % self.size
        else:
            hash_code = hash(key) % self.size
        bucket = self.table[hash_code]
        for kvp in bucket:
            if kvp[0] == key:
                return kvp[1]
        return None

    def remove(self, key: Any) -> bool:
        """Removes a key-value pair from the hash map.

        Args:
            key: The key to remove.

        Returns:
            True if the key-value pair was removed successfully,
            False otherwise.
        """
        hash_code = hash(key) % self.size
        bucket = self.table[hash_code]
        for i, kvp in enumerate(bucket):
            if kvp[0] == key:
                bucket.pop(i)
                return True
        return False

    def contains(self, key: Any) -> bool:
        """Checks if a key is present in the hash map.

        Args:
            key: The key to check for.

        Returns:
            True if the key is present in the hash map, False otherwise.
        """
        hash_code = hash(key) % self.size
        bucket = self.table[hash_code]
        for kvp in bucket:
            if kvp[0] == key:
                return True
        return False

    def size(self) -> int:
        """Gets the size of the hash map.

        Returns:
            The size of the hash map.
        """
        return self.size

    def clear(self) -> None:
        """Clears the hash map.
        """
        self.table = [[] for _ in range(self.size)]

    def display_package_status(self) -> None:
        """
        Displays all packages to the console, one package per line.
        """
        all_packages = self.get_all_elements()
        for package in all_packages:
            print(package)

    def print_package(self, key) -> None:
        """
        Displays one selected package to the console.
        :param key: the package ID of the package to display
        :type key: int
        """
        print(self.get(key))

    def get_all_elements(self) -> List[Any]:
        flat_list: List[Any] = []
        for element in self.table:
            if type(element) is list:
                # If the element is of type list, iterate through the sublist
                for item in element:
                    if len(item) > 0:
                        flat_list.append(item)
            else:
                flat_list.append(element)

        return flat_list
