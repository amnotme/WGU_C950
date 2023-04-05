# 4.9 BST traversal - Find keys in a range

# Specification

Given 2 alphanumeric values, implement a find_in_range() function that finds all keys within the range of the 2 values that branch from a specific node's key (including the specified node).

Code to read in and insert values into the tree has been provided as well as code to print the resulting list key within the range.

# Requirements

1) Read in the beginning and ending values of the range. The ending value must be greater than the beginning. The values can include any ASCII character (not just integers).

2) Read in the key of the node that find_in_range() will start from and find the node in the tree.

3) Implement the find_in_range() function. find_in_range() has 3 cases to determine if the current node's key is:

- less than the beginning range value
- within the range
- or greater than the ending range value

Store all keys within the range in the list `keys_in_range` (defined for you).

Ex: For the input

```
bat start ding being clock quick last name truck
craft
question
ding

```

where

- `bat start ding being clock quick last name truck` are the keys of the nodes entered into the tree
- `craft` is the beginning range value
- `question` is the ending range value
- `ding` is the key of the starting node that all found results will branch from

the output ends with

```
Keys in range: ['ding', 'last', 'name']

```
