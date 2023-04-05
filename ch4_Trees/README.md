# **4.1 Binary trees**

**Binary tree basics**

In a list, each node has up to one successor. In a ***binary tree***, each node has up to two children, known as a *left child* and a *right child*. "Binary" means two, referring to the two children. Some more definitions related to a binary tree:

- ***Leaf***: A tree node with no children.
- ***Internal node***: A node with at least one child.
- ***Parent***: A node with a child is said to be that child's parent. A node's ***ancestors*** include the node's parent, the parent's parent, etc., up to the tree's root.
- ***Root***: The one tree node with no parent (the "top" node).

Another section discusses binary tree usefulness; this section introduces definitions.

Below, each node is represented by just the node's key, as in B, although the node may have other data.

**Depth, level, and height**

A few additional terms:

- The link from a node to a child is called an ***edge***.
- A node's ***depth*** is the number of edges on the path from the root to the node. The root node thus has depth 0.
- All nodes with the same depth form a tree ***level***.
- A tree's ***height*** is the largest depth of any node. A tree with just one node has height 0.

**Special types of binary trees**

Certain binary tree structures can affect the speed of operations on the tree. The following describe special types of binary trees:

- A binary tree is ***full*** if every node contains 0 or 2 children.
- A binary tree is ***complete*** if all levels, except possibly the last level, are completely full and all nodes in the last level are as far left as possible.
- A binary tree is ***perfect***, if all internal nodes have 2 children and all leaf nodes are at the same level.


# **4.2 Applications of trees**

**File systems**

Trees are commonly used to represent hierarchical data. A tree can represent files and directories in a file system, since a file system is a hierarchy.


**Binary space partitioning**

***Binary space partitioning*** (***BSP***) is a technique of repeatedly separating a region of space into 2 parts and cataloging objects contained within the regions. A ***BSP tree*** is a binary tree used to store information for binary space partitioning. Each node in a BSP tree contains information about a region of space and which objects are contained in the region.

In graphics applications, a BSP tree can be used to store all objects in a multidimensional world. The BSP tree can then be used to efficiently determine which objects must be rendered on screen. The viewer's position in space is used to perform a lookup within the BSP tree. The lookup quickly eliminates a large number of objects that are not visible and therefore should not be rendered.

# **4.3 Binary search trees**

**Binary search trees**

An especially useful form of binary tree is a ***binary search tree*** (BST), which has an ordering property that any node's left subtree keys ≤ the node's key, and the right subtree's keys ≥ the node's key. That property enables fast searching for an item, as will be shown later.


**Searching**

To ***search*** nodes means to find a node with a desired key, if such a node exists. A BST may yield faster searches than a list. Searching a BST starts by visiting the root node (which is the first currentNode below):

```python
if (currentNode->key == desiredKey) {
   return currentNode; // The desired node was found
}
else if (desiredKey < currentNode->key) {
   // Visit left child, repeat
}
else if (desiredKey > currentNode->key) {
   // Visit right child, repeat
}
```

**Best case BST search runtime**

Searching a BST in the worst case requires H + 1 comparisons, meaning O(H) comparisons, where H is the tree height. Ex: A tree with a root node and one child has height 1; the worst case visits the root and the child: 1 + 1 = 2. A major BST benefit is that an N-node binary tree's height may be as small as O($logN$), yielding extremely fast searches. Ex: A 10,000 node list may require 10,000 comparisons, but a 10,000 node BST may require only 14 comparisons.

A binary tree's height can be minimized by keeping all levels full, except possibly the last level. Such an "all-but-last-level-full" binary tree's height is $H=$⌊$log2N$⌋.

**Successors and predecessors**

A BST defines an ordering among nodes, from smallest to largest. A BST node's ***successor*** is the node that comes after in the BST ordering, so in A B C, A's successor is B, and B's successor is C. A BST node's ***predecessor*** is the node that comes before in the BST ordering.

If a node has a right subtree, the node's successor is that right subtree's leftmost child: Starting from the right subtree's root, follow left children until reaching a node with no left child (may be that subtree's root itself). If a node doesn't have a right subtree, the node's successor is the first ancestor having this node in a left subtree. Another section provides an algorithm for printing a BST's nodes in order.

# **4.4 BST search algorithm**

Given a key, a ***search***
 algorithm returns the first node found matching that key, or returns null if a matching node is not found. A simple BST search algorithm checks the current node (initially the tree's root), returning that node as a match, else assigning the current node with the left (if key is less) or right (if key is greater) child and repeating. If such a child is null, the algorithm returns null (matching node not found).


```python
BSTSearch(tree, key) {
  cur = tree->root   
  while (cur is not null)
     if (key == cur->key)
        return cur // Found
     else if (key < cur->key)
        cur = cur->left
     else
        cur = cur->right
  return null // Not found
}
```

# **4.5 BST insert algorithm**

Given a new node, a BST ***insert*** operation inserts the new node in a proper location obeying the BST ordering property. A simple BST insert algorithm compares the new node with the current node (initially the root).

- *Insert as left child*: If the new node's key is less than the current node, and the current node's left child is null, the algorithm assigns that node's left child with the new node.
- *Insert as right child*: If the new node's key is greater than the current node, and the current node's right child is null, the algorithm assigns the node's right child with the new node.
- *Search for insert location*: If the left (or right) child is not null, the algorithm assigns the current node with that child and continues searching for a proper insert location.

```python
BSTInsert(tree, node) {
 if (tree->root is null)
   tree->root = node
   node->left = null
   node->right = null
 else
   cur = tree->root
   while (cur is not null)
     if (node->key < cur->key)
        if (cur->left is null)
          cur->left = node
          cur = null
        else
          cur = cur->left
     else
        if (cur->right is null)
          cur->right = node
          cur = null
        else
          cur = cur->right       
   node->left = null
   node->right = null
}
```

# **4.6 BST remove algorithm**

Given a key, a BST ***remove*** operation removes the first-found matching node, restructuring the tree to preserve the BST ordering property. The algorithm first searches for a matching node just like the search algorithm. If found (call this node X), the algorithm performs one of the following sub-algorithms:

- *Remove a leaf node:* If X has a parent (so X is not the root), the parent's left or right child (whichever points to X) is assigned with null. Else, if X was the root, the root pointer is assigned with null, and the BST is now empty.
- *Remove an internal node with single child:* If X has a parent (so X is not the root), the parent's left or right child (whichever points to X) is assigned with X's single child. Else, if X was the root, the root pointer is assigned with X's single child.
- *Remove an internal node with two children:* This case is the hardest. First, the algorithm locates X's successor (the leftmost child of X's right subtree), and copies the successor to X. Then, the algorithm recursively removes the successor from the right subtree.
```python
BSTRemove(tree, key) {
   par = null
   cur = tree->root
   while (cur is not null) { // Search for node
      if (cur->key == key) { // Node found
         if (!cur->left && !cur->right) {        // Remove leaf
            if (!par) // Node is root
               tree->root = null
            else if (par->left == cur)
               par->left = null
            else
               par->right = null
         }
         else if (cur->left && !cur->right) {    // Remove node with only left child
            if (!par) // Node is root
               tree->root = cur->left
            else if (par->left == cur)
               par->left = cur->left
            else
               par->right = cur->left
         }
         else if (!cur->left && cur->right) {    // Remove node with only right child
            if (!par) // Node is root
               tree->root = cur->right
            else if (par->left == cur)
               par->left = cur->right
            else
               par->right = cur->right
         }
         else {                                  // Remove node with two children
            // Find successor (leftmost child of right subtree)
            suc = cur->right
            while (suc->left is not null)
               suc = suc->left
            successorData = Create copy of suc's data
            BSTRemove(tree, suc->key)     // Remove successor
            Assign cur's data with successorData
         }
         return // Node found and removed
      }
      else if (cur->key < key) { // Search right
         par = cur
         cur = cur->right
      }
      else {                     // Search left
         par = cur
         cur = cur->left
      }
   }
   return // Node not found
}
```

BST remove algorithm complexity

The BST remove algorithm traverses the tree from the root to find the node to remove. When the node being removed has 2 children, the node's successor is found and a recursive call is made. One node is visited per level, and in the worst case scenario the tree is traversed twice from the root to a leaf. A BST with $N$ nodes has at least $log2N$ levels and at most $N$ $$levels. Therefore, the runtime complexity of removal is best case $O(logN)$ and worst case $O(N).$

Two pointers are used to traverse the tree during removal. When the node being removed has 2 children, a third pointer and a copy of one node's data are also used, and one recursive call is made. Thus, the space complexity of removal is always $O(1)$.


# **4.7 BST inorder traversal**

A ***tree traversal*** algorithm visits all nodes in the tree once and performs an operation on each node. An ***inorder traversal*** visits all nodes in a BST from smallest to largest, which is useful for example to print the tree's nodes in sorted order. Starting from the root, the algorithm recursively prints the left subtree, the current node, and the right subtree.

```python
BSTPrintInorder(node) {
if (node is null)
return

  BSTPrintInorder(node->left)
  Print node
  BSTPrintInorder(node->right)
}
```

# **4.8 BST height and insertion order**

Recall that a tree's ***height*** is the maximum edges from the root to any leaf. (Thus, a one-node tree has height 0.)

The *minimum* N-node binary tree height is $ℎ=|log2N|$ , achieved when each level is full except possibly the last. The *maximum* N-node binary tree height is N - 1 (the - 1 is because the root is at height 0).

Searching a BST is fast if the tree's height is near the minimum. Inserting items in random order naturally keeps a BST's height near the minimum. In contrast, inserting items in nearly-sorted order leads to a nearly-maximum tree height.
