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
