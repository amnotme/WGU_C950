from BinarySearchTree import BinarySearchTree, Node

# Write find_in_range() function


# Main
if __name__ == "__main__":
    tree = BinarySearchTree()
    keys_in_range = []

    # Insert some random-looking integers into the tree.
    user_values = input('Enter values to be inserted separated by spaces: ')
    print()

    for value in user_values.split():
        new_node = Node(value)
        tree.insert(new_node)

    print('Initial tree:')
    print(tree)
    print()

    # Read in range values and starting node's key

    # Find starting node in tree

    # Find keys in range from starting node

    # Output list of keys in range
    print('Keys in range:', keys_in_range)
