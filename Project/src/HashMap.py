from typing import Any, List, Optional


class HashMap:

    """A hash map for storing key-value pairs.

    Args:
        size: The size of the hash map.

    Attributes:
        size: The size of the hash map.
        table: A list of lists, where each inner list represents a bucket in the hash map.

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

    def add(self, key: Any, value: Any) -> bool:
        """Adds a key-value pair to the hash map.

        Args:
            key: The key to add.
            value: The value to add.

        Returns:
            True if the key-value pair was added successfully, False otherwise.
        """
        hash_code = hash(key) % self.size
        bucket = self.table[hash_code]
        for i, kvp in enumerate(bucket):
            if kvp[0] == key:
                bucket[i] = (key, value)
                return True
        bucket.append((key, value))
        return True

    def get(self, key: Any) -> Optional[Any]:
        """Gets the value associated with a key in the hash map.

        Args:
            key: The key to get the value for.

        Returns:
            The value associated with the key, or None if the key is not present in the hash map.
        """
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
            True if the key-value pair was removed successfully, False otherwise.
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



    def print(self) -> None:
        """Displays all packages in the hash table to the console,
           grouped by hash table bucket.
        Returns:
            None
        """
        print('-------Hash Table-------')
        for package in self.table:
            print(str(package))

    def print_all_packages(self) -> None:
        """
        Displays all packages to the console, one package per line.
        """
        for row in self.table:
            for package in row:
                print(package)

    def reset_packages(self) -> None:
        """
        Resets status for all packages to "AT HUB".
        """
        for row in self.table:
            for package in row:
                package.status = "AT HUB"

    def print_package(self, key) -> None:
        """
        Displays one selected package to the console.
        :param key: the package ID of the package to display
        :type key: int
        """
        print(self.get(key))
