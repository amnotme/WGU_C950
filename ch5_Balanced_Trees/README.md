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
