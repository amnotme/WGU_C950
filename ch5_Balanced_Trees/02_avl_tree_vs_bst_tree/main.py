from BinarySearchTree import BinarySearchTree, BSTNode
from AVLTree import AVLTree, AVLNode

# FIXME Write function to determine the max depth of a tree
list_from_input = input()
list_of_ints = [int(digit) for digit in list_from_input.split(' ')]

# Create empty tree objects
avl_tree = AVLTree()
binary_search_tree = BinarySearchTree()

bst_total_comparisons = 0
avl_total_comparisons = 0

bst_max_depth = 0
avl_max_depth = 0


def maxDepth(node):
    if node is None:
        return -1

    else:

        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

        # Use the larger one
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1

for digit in list_of_ints:
    comparisons = 0
    print(f"Key: {digit}")

    comparisons = avl_tree.insert(AVLNode(digit))
    print(f"AVL - Insert comparisons: {comparisons}")
    avl_total_comparisons += comparisons

    comparisons = binary_search_tree.insert(BSTNode(digit))
    print(f"BST - Insert comparisons: {comparisons}")
    bst_total_comparisons += comparisons

    print()

avl_max_depth = maxDepth(avl_tree.root)
bst_max_depth = maxDepth(binary_search_tree.root)

print(f"Total # of comparisons")
print(f"AVL tree: {avl_total_comparisons}")
print(f"Binary search tree: {bst_total_comparisons}")
print()

print("Max tree depth")
print(f"AVL tree: {avl_max_depth}")
print(f"Binary search tree: {bst_max_depth}")
print()

# Print the tree after all inserts are complete
print('Trees after insertions:')
print('AVL tree', avl_tree)
print('\nBinary search tree', binary_search_tree)
