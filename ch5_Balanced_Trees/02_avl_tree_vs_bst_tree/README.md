# AVL tree vs BST tree

## Specification

Count the number of comparisons that are performed when a node is inserted into an AVL and a Binary search tree. You will also determine the maximum depth of each tree after all of the nodes are inserted. The lab will allow you to see the efficiency gained by using a AVL (balanced) tree instead of a Binary search tree to sort data.

## Requirements

1) In the the main program (main.py), read in a list of integers separated by a space. Each integer is a node's key. Insert the keys into both given AVL and Binary search trees.

2) Edit the code in both AVLTree.py and BinarySearchTree.py to count the number of comparisons that occur when a node is inserted. The insert() functions should return the number of comparisons. In the main program, print the number of insert comparisons per key.

3) In the main program, print the total number of comparisons to insert all of the keys into both trees.

4) In the main program, write a function to determine the max depth of each tree and output the results. *Hint: The root node has a depth of 0 and the root's children have a depth of 1.*

Code to print each tree is also provided for you to visualize the trees that are built.

Ex: For the input

```
47 19 3 12 18

```

the output is

```
Key: 47
AVL - Insert comparisons: 0
BST - Insert comparisons: 0

Key: 19
AVL - Insert comparisons: 1
BST - Insert comparisons: 1

Key: 3
AVL - Insert comparisons: 2
BST - Insert comparisons: 2

Key: 12
AVL - Insert comparisons: 2
BST - Insert comparisons: 3

Key: 18
AVL - Insert comparisons: 3
BST - Insert comparisons: 4

Total # of comparisons
AVL tree: 8
Binary search tree: 10

Max tree depth
AVL tree: 2
Binary search tree: 4

Trees after insertions:
AVL tree
    ____19
   /      \
  12       47
 /  \
3    18

Binary search tree
          _47
         /
  ______19
 /
3
 \
  12
    \
     18

```
