from AVLTree import AVLTree, Node

# Create an empty AVLTree object.
tree = AVLTree()

# Insert some random-looking integers into the tree.
keys = [ 10, 20, 5, 22, 15, 47, 19, 3, 12, 18 ]
for key in keys:
    node = Node(key)
    tree.insert(node)

# Print the tree after all inserts are complete.
print("Tree after initial insertions:")
print(tree)

# Find and remove the node with the key value 12.
# This should cause a right rotation on node 10.
print("Remove node 12:")
tree.remove_key(12)
print(tree)

# Find and remove the node with the key value 20.
# This should cause its right child to shift up into
# the 20 node's position without any other reordering
# required.
print("Remove node 20:")
tree.remove_key(20)
print(tree)

# Attempt to remove a node with key 30, a value not in the tree.
print("Remove node 30 (should not be in tree):")
if not tree.remove_key(30):
    print("*** Key not found. Tree is not changed. ***")
print(tree)
