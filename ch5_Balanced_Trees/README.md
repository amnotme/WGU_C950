# 5.1 AVL: A balanced tree

**Balanced BST**

An ***AVL tree*** is a BST with a height balance property and specific operations to rebalance the tree when a node is inserted or removed. This section discusses the balance property; another section discusses the operations. A BST is ***height balanced*** if for any node, the heights of the node's left and right subtrees differ by only 0 or 1.

A node's ***balance factor*** is the left subtree height minus the right subtree height, which is 1, 0, or -1 in an AVL tree.

Recall that a tree (or subtree) with just one node has height 0. For calculating a balance factor, a non-existent left or right child's subtree's height is said to be -1.

**AVL tree height**

Minimizing binary tree height yields fastest searches, insertions, and removals. If nodes are inserted and removed dynamically, maintaining a minimum height tree requires extensive tree rearrangements. In contrast, an AVL tree only requires a few local rotations (discussed in a later section), so is more computationally efficient, but doesn't guarantee a minimum height. However, theoreticians have shown that an AVL tree's worst case height is no worse than about 1.5x the minimum binary tree height, so the height is still O(log N) where N is the number of nodes. Furthermore, experiments show that AVL tree heights in practice are much closer to the minimum.

**Storing height at each AVL node**

An AVL tree implementation can store the subtree height as a member of each node. With the height stored as a member of each node, the balance factor for any node can be computed in O(1) time. When a node is inserted in or removed from an AVL tree, ancestor nodes may need the height value to be recomputed.

# 5.2 AVL rotations

**Tree rotation to keep balance**

Inserting an item into an AVL tree may require rearranging the tree to maintain height balance. A ***rotation*** is a local rearrangement of a BST that maintains the BST ordering property while rebalancing the tree.

**Algorithms supporting AVL trees**

The `AVLTreeUpdateHeight` algorithm updates a node's height value by taking the maximum of the child subtree heights and adding 1.

The `AVLTreeSetChild` algorithm sets a node as the parent's left or right child, updates the child's parent pointer, and updates the parent node's height.

The `AVLTreeReplaceChild` algorithm replaces one of a node's existing child pointers with a new value, utilizing `AVLTreeSetChild` to perform the replacement.

The `AVLTreeGetBalance` algorithm computes a node's balance factor by subtracting the right subtree height from the left subtree height.

```python
AVLTreeUpdateHeight(node) {
   leftHeight = -1
   if (node->left != null)
      leftHeight = node->left->height
   rightHeight = -1
   if (node->right != null)
      rightHeight = node->right->height
   node->height = max(leftHeight, rightHeight) + 1
}

AVLTreeSetChild(parent, whichChild, child) {
   if (whichChild != "left" && whichChild != "right")
      return false

   if (whichChild == "left")
      parent->left = child
   else
      parent->right = child
   if (child != null)
      child->parent = parent

   AVLTreeUpdateHeight(parent)
   return true
}

AVLTreeReplaceChild(parent, currentChild, newChild) {
   if (parent->left == currentChild)
      return AVLTreeSetChild(parent, "left", newChild)
   else if (parent->right == currentChild)
      return AVLTreeSetChild(parent, "right", newChild)
   return false
}

AVLTreeGetBalance(node) {
   leftHeight = -1
   if (node->left != null)
      leftHeight = node->left->height
   rightHeight = -1
   if (node->right != null)
      rightHeight = node->right->height
   return leftHeight - rightHeight
}
```

**Right rotation algorithm**

A right rotation algorithm is defined on a subtree root (node D) which must have a left child (node B). The algorithm reassigns child pointers, assigning B's right child with D, and assigning D's left child with C (B's original right child, which may be null). If D's parent is non-null, then the parent's child D is replaced with B. Other tree parts (T1..T4 below) naturally stay with their parent nodes.

```python
AVLTreeRotateRight(tree, node) {
   leftRightChild = node->left->right
   if (node->parent != null)
      AVLTreeReplaceChild(node->parent, node, node->left)
   else { // node is root
      tree->root = node->left
      tree->root->parent = null
   }
   AVLTreeSetChild(node->left, "right", node)
   AVLTreeSetChild(node, "left", leftRightChild)
}
```

**AVL tree balancing**

When an AVL tree node has a balance factor of 2 or -2, which only occurs after an insertion or removal, the node must be rebalanced via rotations. The `AVLTreeRebalance` algorithm updates the height value at a node, computes the balance factor, and rotates if the balance factor is 2 or -2.

**AVLTreeRebalance algorithm**

```python
AVLTreeRebalance(tree, node) {
   AVLTreeUpdateHeight(node)        
   if (AVLTreeGetBalance(node) == -2) {
      if (AVLTreeGetBalance(node->right) == 1) {
         // Double rotation case.
         AVLTreeRotateRight(tree, node->right)
      }
      return AVLTreeRotateLeft(tree, node)
   }
   else if (AVLTreeGetBalance(node) == 2) {
      if (AVLTreeGetBalance(node->left) == -1) {
         // Double rotation case.
         AVLTreeRotateLeft(tree, node->left)
      }
      return AVLTreeRotateRight(tree, node)
   }        
   return node
}
```

# 5.3 AVL insertions

**Insertions requiring rotations to rebalance**

Inserting an item into an AVL tree may cause the tree to become unbalanced. A rotation can rebalance the tree.

**Four imbalance cases**

After inserting a node, nodes on the path from the new node to the root should be checked for a balance factor of 2 or -2. The first such node P triggers rebalancing. Four cases exist, distinguishable by the balance factor of node P and one of P's children.

**Insertion with rebalancing**

An AVL tree insertion involves searching for the insert location, inserting the new node, updating balance factors, and rebalancing.

Balance factor updates are only needed on nodes ascending along the path from the inserted node up to the root, since no other nodes' balance could be affected. Each node's balance factor can be recomputed by determining left and right subtree heights, or for speed can be stored in each node and then incrementally updated: +1 if ascending from a left child, -1 if from a right child. If a balance factor update yields 2 or -2, the imbalance case is determined via that node's left (for 2) or right (for -2) child's balance factor, and the appropriate rotations performed.

**AVL insertion algorithm**

Insertion starts with the standard BST insertion algorithm. After inserting a node, all ancestors of the inserted node, from the parent up to the root, are rebalanced. A node is rebalanced by first computing the node's balance factor, then performing rotations if the balance factor is outside of the range [-1,1].

```python
AVLTreeInsert(tree, node) {
   if (tree->root == null) {
      tree->root = node
      node->parent = null
      return
   }

   cur = tree->root
   while (cur != null) {
      if (node->key < cur->key) {
         if (cur->left == null) {
            cur->left = node
            node->parent = cur
            cur = null
         }
         else
            cur = cur->left
      }
      else {
         if (cur->right == null) {
            cur->right = node
            node->parent = cur
            cur = null
         }
         else
            cur = cur->right
      }
   }

   node = node->parent
   while (node != null) {
      AVLTreeRebalance(tree, node)
      node = node->parent
   }
}
```

**AVL insertion algorithm complexity**

The AVL insertion algorithm traverses the tree from the root to a leaf node to find the insertion point, then traverses back up to the root to rebalance. One node is visited per level, and at most 2 rotations are needed for a single node. Each rotation is an O(1) operation. Therefore, the runtime complexity of insertion is O(log N).

Because a fixed number of temporary pointers are needed for the AVL insertion algorithm, including any rotations, the space complexity is O(1).


# 5.4 AVL removals

**Removing nodes in AVL trees**

Given a key, an AVL tree ***remove*** operation removes the first-found matching node, restructuring the tree to preserve all AVL tree requirements. Removal begins by removing the node using the standard BST removal algorithm. After removing a node, all ancestors of the removed node, from the nodes' parent up to the root, are rebalanced. A node is rebalanced by first computing the node's balance factor, then performing rotations if the balance factor is 2 or -2.

**AVL tree removal algorithm**

To remove a key, the AVL tree removal algorithm first locates the node containing the key using `BSTSearch`. If the node is found, AVLTreeRemoveNode is called to remove the node. Standard BST removal logic is used to remove the node from the tree. Then AVLTreeRebalance is called for all ancestors of the removed node, from the parent up to the root.


```Python
AVLTreeRemoveNode(tree, node) {
   if (node == null)
      return false
   . # BST removal
   .
   .
   node = parent
   while (node != null) {
      AVLTreeRebalance(tree, node)            
      node = node->parent
   }
   return true
}

AVLTreeRebalance(tree, node) {
   AVLTreeUpdateHeight(node)        
   if (AVLTreeGetBalance(node) == -2) {
      if (AVLTreeGetBalance(node->right) == 1) {
         // Double rotation case.
         AVLTreeRotateRight(tree, node->right)
      }
      return AVLTreeRotateLeft(tree, node)
   }
   else if (AVLTreeGetBalance(node) == 2) {
      if (AVLTreeGetBalance(node->left) == -1) {
         // Double rotation case.
         AVLTreeRotateLeft(tree, node->left)
      }
      return AVLTreeRotateRight(tree, node)
   }        
   return node
}
```

AVLTreeRebalance algorithm.

```python
AVLTreeRebalance(tree, node) {
   AVLTreeUpdateHeight(node)
if (AVLTreeGetBalance(node) == -2) {
if (AVLTreeGetBalance(node->right) == 1) {
         // Double rotation case.
         AVLTreeRotateRight(tree, node->right)
      }
return AVLTreeRotateLeft(tree, node)
   }
elseif (AVLTreeGetBalance(node) == 2) {
if (AVLTreeGetBalance(node->left) == -1) {
         // Double rotation case.
         AVLTreeRotateLeft(tree, node->left)
      }
return AVLTreeRotateRight(tree, node)
   }
return node
}
```

AVLTreeRemoveKey algorithm.

```python
AVLTreeRemoveKey(tree, key) {
   node = BSTSearch(tree, key)
return AVLTreeRemoveNode(tree, node)
}
```

AVLTreeRemoveNode algorithm.

```python
AVLTreeRemoveNode(tree, node) {
   if (node == null)
      return false

   // Parent needed for rebalancing
   parent = node->parent

   // Case 1: Internal node with 2 children
   if (node->left != null && node->right != null) {
      // Find successor
      succNode = node->right
      while (succNode->left != null)
         succNode = succNode->left

      // Copy the value from the node
      node = Copy succNode

      // Recursively remove successor
      AVLTreeRemoveNode(tree, succNode)

      // Nothing left to do since the recursive call will have rebalanced
      return true
   }

   // Case 2: Root node (with 1 or 0 children)
   else if (node == tree->root) {
      if (node->left != null)
         tree->root = node->left
      else
         tree->root = node->right

      if (tree->root)
         tree->root->parent = null

      return true
   }

   // Case 3: Internal with left child only
   else if (node->left != null)
      AVLTreeReplaceChild(parent, node, node->left)

   // Case 4: Internal with right child only OR leaf
   else
      AVLTreeReplaceChild(parent, node, node->right)

   // node is gone. Anything that was below node that has persisted is already correctly
   // balanced, but ancestors of node may need rebalancing.
   node = parent
   while (node != null) {
      AVLTreeRebalance(tree, node)            
      node = node->parent
   }
   return true
}
```

AVL removal algorithm complexity
In the worst case scenario, the AVL removal algorithm traverses the tree from the root to the lowest level to find the node to remove, then traverses back up to the root to rebalance. One node is visited per level, and at most 2 rotations are needed for a single node. Each rotation is an O(1) operation. Therefore, the runtime complexity of an AVL tree removal is O(log N).

Because a fixed number of temporary pointers are needed for the AVL removal algorithm, including any rotations, the space complexity is O(1).





# 5.5 Python: AVL Trees

**The Node class for AVL Trees**

Because AVL Trees are a form of a binary search tree, the AVLTree class is similar to the BinarySearchTree class. A Node class is used that contains data members key, left, and right, as well as two new data members:

- parent - A pointer to the parent node, or None for the root.
- height - The height of the subtree at the node. A single node has a height of 0.

The height data member is used to detect imbalances in the tree after insertions or removals, while the parent data member is used during rotations to correct imbalances. The Node class contains methods that are useful for AVL operations:

- get_balance() - Returns the node's balance factor. The balance factor is the left child's height minus the right child's height. A height of -1 is used in the calculation if the child is None.
- update_height() - Calculates the node's current height and assigns the height data member with the new value.
- set_child() - Assigns either the left or right child data members with a new node.
- replace_child() - Replaces a current child node with a new node.

```python
class Node:
    # Constructor with a key parameter creates the Node object.
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0

    # Calculate the current nodes' balance factor,
    # defined as height(left subtree) - height(right subtree)
    def get_balance(self):
        # Get current height of left subtree, or -1 if None
        left_height = -1
        if self.left is not None:
            left_height = self.left.height

        # Get current height of right subtree, or -1 if None
        right_height = -1
        if self.right is not None:
            right_height = self.right.height

        # Calculate the balance factor.
        return left_height - right_height

    # Recalculate the current height of the subtree rooted at
    # the node, usually called after a subtree has been
    # modified.
    def update_height(self):
        # Get current height of left subtree, or -1 if None
        left_height = -1
        if self.left is not None:
            left_height = self.left.height

        # Get current height of right subtree, or -1 if None
        right_height = -1
        if self.right is not None:
            right_height = self.right.height

        # Assign self.height with calculated node height.
        self.height = max(left_height, right_height) + 1

		# Assign either the left or right data member with a new
		# child. The parameter which_child is expected to be the
		# string "left" or the string "right". Returns True if
		# the new child is successfully assigned to this node, False
		# otherwise.
		def set_child(self, which_child, child):
		    # Ensure which_child is properly assigned.
		    if which_child != "left" and which_child != "right":
		        return False

		    # Assign the left or right data member.
		    if which_child == "left":
		        self.left = child
		    else:
		        self.right = child

		    # Assign the parent data member of the new child,
		    # if the child is not None.
		    if child is not None:
		        child.parent = self

		    # Update the node's height, since the subtree's structure
		    # may have changed.
		    self.update_height()
		    return True

		# Replace a current child with a new child. Determines if
		# the current child is on the left or right, and calls
		# set_child() with the new node appropriately.
		# Returns True if the new child is assigned, False otherwise.
		def replace_child(self, current_child, new_child):
		    if self.left is current_child:
		        return self.set_child("left", new_child)
		    elif self.right is current_child:
		        return self.set_child("right", new_child)

		    # If neither of the above cases applied, then the new child
		    # could not be attached to this node.
		    return False
```

**Rotations and rebalancing**

Tree rotations are required to correct any problems where the left and right subtrees of a node have heights that differ by more than 1. After a new node is inserted into an AVL tree, either one or two rotations will fix any imbalance that happens. The rotate_left() and rotate_right() methods perform these operations. The rebalance() method examines the structure of the subtree of a node, and determines which rotations to do if a height imbalance exists at the node.

The AVLTree class with rotate_left(), rotate_right() and rebalance() methods.

```python
class AVLTree:
    # Constructor to create an empty AVLTree. There is only
    # one data member, the tree's root Node, and it starts
    # out as None.
    def __init__(self):
        self.root = None

    # Performs a left rotation at the given node. Returns the
    # new root of the subtree.
    def rotate_left(self, node):
        # Define a convenience pointer to the right child of the
        # left child.
        right_left_child = node.right.left

        # Step 1 - the right child moves up to the node's position.
        # This detaches node from the tree, but it will be reattached
        # later.
        if node.parent is not None:
            node.parent.replace_child(node, node.right)
        else:  # node is root
            self.root = node.right
            self.root.parent = None

        # Step 2 - the node becomes the left child of what used
        # to be its right child, but is now its parent. This will
        # detach right_left_child from the tree.
        node.right.set_child('left', node)

        # Step 3 - reattach right_left_child as the right child of node.
        node.set_child('right', right_left_child)

        return node.parent

    # Performs a right rotation at the given node. Returns the
    # subtree's new root.
    def rotate_right(self, node):
        # Define a convenience pointer to the left child of the
        # right child.
        left_right_child = node.left.right

        # Step 1 - the left child moves up to the node's position.
        # This detaches node from the tree, but it will be reattached
        # later.
        if node.parent is not None:
            node.parent.replace_child(node, node.left)
        else:  # node is root
            self.root = node.left
            self.root.parent = None

        # Step 2 - the node becomes the right child of what used
        # to be its left child, but is now its parent. This will
        # detach left_right_child from the tree.
        node.left.set_child('right', node)

        # Step 3 - reattach left_right_child as the left child of node.
        node.set_child('left', left_right_child)

        return node.parent

    # Updates the given node's height and rebalances the subtree if
    # the balancing factor is now -2 or +2. Rebalancing is done by
    # performing a rotation. Returns the subtree's new root if
    # a rotation occurred, or the node if no rebalancing was required.
    def rebalance(self, node):

        # First update the height of this node.
        node.update_height()        

        # Check for an imbalance.
        if node.get_balance() == -2:

            # The subtree is too big to the right.
            if node.right.get_balance() == 1:
                # Double rotation case. First do a right rotation
                # on the right child.
                self.rotate_right(node.right)

            # A left rotation will now make the subtree balanced.
            return self.rotate_left(node)

        elif node.get_balance() == 2:

            # The subtree is too big to the left
            if node.left.get_balance() == -1:
                # Double rotation case. First do a left rotation
                # on the left child.
                self.rotate_left(node.left)

            # A right rotation will now make the subtree balanced.
            return self.rotate_right(node)

        # No imbalance, so just return the original node.
        return node
```

**Insertions**

AVL insertions are performed in two steps:

1. Insert into the tree using the normal binary search tree insertion algorithm.
2. Call rebalance() on all nodes along a path from the new node's parent up to the root.

Step 1 requires $O(log N)$ steps, since an AVL tree has $O(log N)$ levels, and the loop makes the current node go down one level with each iteration. Step 2 requires $O(log N)$ steps, again since the path back up to the root has $O(log N)$ levels to visit, and rotations are $O(1)$ operations. Thus, the insert() method has a worst-case runtime of $O(log N)$.

Figure 5.5.3: The AVLTree insert() method.

```python
def insert(self, node):

    # Special case: if the tree is empty, just set the root to
    # the new node.
    if self.root is None:
        self.root = node
        node.parent = None

    else:
        # Step 1 - do a regular binary search tree insert.
        current_node = self.root
        while current_node is not None:
            # Choose to go left or right
            if node.key < current_node.key:
                # Go left. If left child is None, insert the new
                # node here.
                if current_node.left is None:
                    current_node.left = node
                    node.parent = current_node
                    current_node = None
                else:
                    # Go left and do the loop again.
                    current_node = current_node.left
            else:
                # Go right. If the right child is None, insert the
                # new node here.
                if current_node.right is None:
                    current_node.right = node
                    node.parent = current_node
                    current_node = None
                else:
                    # Go right and do the loop again.
                    current_node = current_node.right

        # Step 2 - Rebalance along a path from the new node's parent up
        # to the root.
        node = node.parent
        while node is not None:
            self.rebalance(node)
            node = node.parent
```

**Removals**

Removal from an AVL tree is a two-step process, similar to insertion:

1. Remove the node in the same way nodes are removed from a binary search tree. One of four cases is identified to determine how to remove the node. In the most general case, the node's key is replaced by the successor node's key in the tree, and the successor is then more easily removed.
2. Call rebalance() on all the nodes on the path from the removed node's parent up to the root. If the node's successor was ultimately removed, the rebalancing begins from the the successor's parent, not the original target node.

As with insertion, each step requires $O(1)$ operations to be performed, first on a path from the root down to a leaf, and then on a path near a leaf back up to the root. Because the height of an AVL tree is guaranteed to be $O(log N)$, the entire remove algorithm runs in worst-case $O(log N)$ time.

The AVLTree remove_node() method.

```python
def remove_node(self, node):
    # Base case:
    if node is None:
        return False

    # Parent needed for rebalancing.
    parent = node.parent

    # Case 1: Internal node with 2 children
    if node.left is not None and node.right is not None:
        # Find successor
        successor_node = node.right
        while successor_node.left != None:
            successor_node = successor_node.left

        # Copy the value from the node
        node.key = successor_node.key

        # Recursively remove successor
        self.remove_node(successor_node)

        # Nothing left to do since the recursive call will have rebalanced
        return True

    # Case 2: Root node (with 1 or 0 children)
    elif node is self.root:
        if node.left is not None:
             self.root = node.left
        else:
             self.root = node.right

        if self.root is not None:
             self.root.parent = None

        return True

    # Case 3: Internal with left child only
    elif node.left is not None:
        parent.replace_child(node, node.left)

    # Case 4: Internal with right child only OR leaf
    else:
        parent.replace_child(node, node.right)

    # node is gone. Anything that was below node that has persisted is already correctly
    # balanced, but ancestors of node may need rebalancing.
    node = parent
    while node is not None:
        self.rebalance(node)            
        node = node.parent

    return True
```

Often the user does not know where the desired node object to be removed is in the tree, or even if the node exists at all. The remove_key() method can be used to first search for the node using the BinarySearchTree search() method, and then call remove_node() only if search()returns a Node pointer.

The search() and remove_key() methods.

```Python
# Searches for a node with a matching key. Does a regular
# binary search tree search operation. Returns the node with the
# matching key if it exists in the tree, or None if there is no
# matching key in the tree.
def search(self, key):
    current_node = self.root
    while current_node is not None:
        # Compare the current node's key with the target key.
        # If it is a match, return the current key; otherwise go
        # either to the left or right, depending on whether the
        # current node's key is smaller or larger than the target key.
        if current_node.key == key: return current_node
        elif current_node.key < key: current_node = current_node.right
        else: current_node = current_node.left

# Attempts to remove a node with a matching key. If no node has a matching key
# then nothing is done and False is returned; otherwise the node is removed and
# True is returned.
def remove_key(self, key):
    node = self.search(key)
    if node is None:
        return False
    else:
        return self.remove_node(node)
```
