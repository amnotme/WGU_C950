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
20 79 38 77 100 65 89 66 59 86 75 64 93 57 70 41 74 42 7 96 16 69 44 81 17 46 58 80 31 88 28 11 34 10 27 97 76 8 92 39
```

the output is

```

Key: 20
AVL - Insert comparisons: 0
BST - Insert comparisons: 0

Key: 79
AVL - Insert comparisons: 1
BST - Insert comparisons: 1

Key: 38
AVL - Insert comparisons: 2
BST - Insert comparisons: 2

Key: 77
AVL - Insert comparisons: 2
BST - Insert comparisons: 3

Key: 100
AVL - Insert comparisons: 2
BST - Insert comparisons: 2

Key: 65
AVL - Insert comparisons: 3
BST - Insert comparisons: 4

Key: 89
AVL - Insert comparisons: 3
BST - Insert comparisons: 3

Key: 66
AVL - Insert comparisons: 3
BST - Insert comparisons: 5

Key: 59
AVL - Insert comparisons: 3
BST - Insert comparisons: 5

Key: 86
AVL - Insert comparisons: 3
BST - Insert comparisons: 4

Key: 75
AVL - Insert comparisons: 4
BST - Insert comparisons: 6

Key: 64
AVL - Insert comparisons: 4
BST - Insert comparisons: 6

Key: 93
AVL - Insert comparisons: 3
BST - Insert comparisons: 4

Key: 57
AVL - Insert comparisons: 4
BST - Insert comparisons: 6

Key: 70
AVL - Insert comparisons: 4
BST - Insert comparisons: 7

Key: 41
AVL - Insert comparisons: 5
BST - Insert comparisons: 7

Key: 74
AVL - Insert comparisons: 4
BST - Insert comparisons: 8

Key: 42
AVL - Insert comparisons: 5
BST - Insert comparisons: 8

Key: 7
AVL - Insert comparisons: 4
BST - Insert comparisons: 1

Key: 96
AVL - Insert comparisons: 5
BST - Insert comparisons: 5

Key: 16
AVL - Insert comparisons: 5
BST - Insert comparisons: 2

Key: 69
AVL - Insert comparisons: 4
BST - Insert comparisons: 8

Key: 44
AVL - Insert comparisons: 5
BST - Insert comparisons: 9

Key: 81
AVL - Insert comparisons: 5
BST - Insert comparisons: 5

Key: 17
AVL - Insert comparisons: 5
BST - Insert comparisons: 3

Key: 46
AVL - Insert comparisons: 5
BST - Insert comparisons: 10

Key: 58
AVL - Insert comparisons: 4
BST - Insert comparisons: 7

Key: 80
AVL - Insert comparisons: 5
BST - Insert comparisons: 6

Key: 31
AVL - Insert comparisons: 4
BST - Insert comparisons: 3

Key: 88
AVL - Insert comparisons: 5
BST - Insert comparisons: 5

Key: 28
AVL - Insert comparisons: 5
BST - Insert comparisons: 4

Key: 11
AVL - Insert comparisons: 5
BST - Insert comparisons: 3

Key: 34
AVL - Insert comparisons: 4
BST - Insert comparisons: 4

Key: 10
AVL - Insert comparisons: 6
BST - Insert comparisons: 4

Key: 27
AVL - Insert comparisons: 5
BST - Insert comparisons: 5

Key: 97
AVL - Insert comparisons: 5
BST - Insert comparisons: 6

Key: 76
AVL - Insert comparisons: 4
BST - Insert comparisons: 7

Key: 8
AVL - Insert comparisons: 6
BST - Insert comparisons: 5

Key: 92
AVL - Insert comparisons: 5
BST - Insert comparisons: 5

Key: 39
AVL - Insert comparisons: 5
BST - Insert comparisons: 8

Total # of comparisons
AVL tree: 161
Binary search tree: 196

Max tree depth
AVL tree: 5
Binary search tree: 10

Trees after insertions:
AVL tree
                                 ____________________________65__________________
                                /                                                \
                  _____________38_______________                        __________77_______________
                 /                              \                      /                           \
      __________20______                  _______57___            ____70___                  _______89______
     /                  \                /            \          /         \                /               \
  __10___               _31            _42            _59       66         _75         ____81               _96____
 /       \             /   \          /   \          /   \        \       /   \       /      \             /       \
7        _16         _28    34      _41    44       58    64       69    74    76    79       86         _93      _100
 \      /   \       /              /         \                                         \        \       /        /
  8    11    17    27             39          46                                        80       88    92       97


Binary search tree
  ______________20__________________________________________________________________
 /                                                                                  \
7________                        ____________________________________________________79____________________________
         \                      /                                                                                  \
         _16               ____38________________________________________________                     _____________100
        /   \             /                                                      \                   /
      _11    17         _31                                    ___________________77            ____89___
     /                 /   \                                  /                                /         \
    10               _28    34                           ____65                              _86         _93
   /                /                                   /      \                            /   \       /   \
  8                27                              ____59       66_________               _81    88    92    96
                                                  /      \                 \             /                     \
                                       __________57       64            ____75          80                      97
                                      /            \                   /      \
                                    _41             58               _70       76
                                   /   \                            /   \
                                  39    42                         69    74
                                          \
                                           44
                                             \
                                              46
```
