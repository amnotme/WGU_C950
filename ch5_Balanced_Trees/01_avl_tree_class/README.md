zyDE 5.5.1: Exploring the AVLTree class.

The following program inserts some nodes into an AVL tree and then removes some nodes. Try the following activities to see if you can predict how the tree will change:

- Add the value 30 in the middle of the keys list (after the 15). How does the insertion change the initial tree?
- What key could be added to the end of the keys list that would cause at least one rotation when the node is inserted?
- Remove the root (15) immediately after all the nodes are inserted. Does the removal change the tree's height?
- Which nodes will trigger a rotation when removed?

```
Tree after initial insertions:

      ____15______
     /            \
    10            _20
   /  \          /   \
  5    12      _19    22
 /            /         \
3            18          47

Remove node 12:

    ___15______
   /           \
  5            _20
 / \          /   \
3   10      _19    22
           /         \
          18          47

Remove node 20:

    ___15______
   /           \
  5            _22
 / \          /   \
3   10      _19    47
           /
          18

Remove node 30 (should not be in tree):
*** Key not found. Tree is not changed. ***

    ___15______
   /           \
  5            _22
 / \          /   \
3   10      _19    47
           /
          18

```
