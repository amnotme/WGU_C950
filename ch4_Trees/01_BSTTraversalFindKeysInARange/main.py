from BinarySearchTree import BinarySearchTree, Node
from typing import List


def in_order_traversal(starting_node: Node, left: str, right: str, starting_node_value: str, keys_found: List) -> None:
    if starting_node is None:
        return

    in_order_traversal(starting_node.left, left, right, starting_node_value, keys_found)
    # We do an inorder traversal from the designated starting node.
    # If the key is within the range and not already in the List, then add it.
    if starting_node.key >= left and starting_node.key <= right and starting_node.key not in keys_found:
        keys_found.append(starting_node.key)
    in_order_traversal(starting_node.right, left, right, starting_node_value, keys_found)

def find_in_range(tree: BinarySearchTree, starting_node: str, range_min: int, range_max: int):
    keys = []

    # Find starting node in tree
    found_node = tree.search(starting_node)

    in_order_traversal(found_node, range_min, range_max, starting_node, keys)
    return keys



# Main
if __name__ == "__main__":
    tree = BinarySearchTree()
    keys_in_range = []

    # Insert some random-looking integers into the tree.
    print('Enter values to be inserted separated by spaces: ')
    user_values = input()


    for value in user_values.split():
        new_node = Node(value)
        tree.insert(new_node)

    print('Initial tree:')
    print(tree)
    print()

    # Read in range values and starting node's key
    range_min = input("beginning range: ").strip()
    range_max = input("ending range: ").strip()
    starting_node = input("Starting Node: ")

    # Find keys in range from starting node

    keys_in_range = find_in_range(tree, starting_node, range_min, range_max)

    # Output list of keys in range
    print('Keys in range:', keys_in_range)
