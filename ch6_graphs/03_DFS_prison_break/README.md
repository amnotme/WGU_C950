# Prison Break (Depth-First-Search)

## Specification

Use the depth-first-search graph algorithm to count how many possible paths a prisoner has to travel from a starting cell to the exit. A map of the prison is represented with a graph, with rooms represented by vertices and corridors represented by edges. Some rooms contain security cameras and must be avoided by the prisoner.

## Provided code files:

- `graph.py` - An implementation of the Graph and Vertex classes. You are not to modify this file.
- `main.py` - The main module where you implement the required functions. The module contains a small program that calls the functions and outputs the number of exit paths.

## Requirements

Complete two main tasks for this lab:

1. Build the Graph object based on information from a text-based data file. Write the function: `create_graph(filename)`.
    - Parameter: the filename of the graph data file.
    - Returns: the graph object, the vertex where the prisoner starts, and the vertex where the exit is, in that order in a 3-tuple.
2. Use a depth-first-search algorithm to count the total number of different escape paths the prisoner could use. Write the function: `count_exit_paths(g, start_vertex, exit_vertex)`.
    - Parameters: the graph object, the vertex where the prisoner starts, and the vertex where the exit is.
    - Returns: an integer count of how many unique paths exist from the starting vertex to the exit vertex. Only count paths that do not contain vertices with cameras.

# Building the Graph Object

The prison is laid out in a rectangular grid with some number of rows and columns. Corridors exist between all adjacent rooms. The prisoner's cell is always in the North-West corner of the prison, and the exit is always in the South-East corner. The following diagram shows a sample prison with 3 rows and 4 columns, with two rooms that have cameras.

ASSET 1

The prison shown above is defined in a text file. The first line contains two integers separated by a space: the number of rows followed by the number of columns. Each subsequent line contains the row and column number of the cells that contain cameras. The file that represents the above prison is:

```txt
3 4
1 2
2 0

```

The first line ("`3 4`") specifies that the prison is a 3x4 grid (3 rows, 4 columns). The "`1 2`" line says that a camera exists at row 1 and column 2 (remembering that indexes start at 0), and the "`2 0`" line says that a camera exists at row 2 and column 0. The prisoner always starts at position (0, 0) and the exit is always at position (row count - 1, column count - 1).

The create_graph() function takes the name of the graph data file as an argument and returns the corresponding Graph object, in addition to pointers to the prisoner's starting position and the prison's exit position.

The filename is retrieved from the command-line using the `sys.argv` list.

Example usage:

```python
import sys
prison_filename = sys.argv[1]
prison_graph, prisoner_vertex, exit_vertex = create_graph(prison_filename)

```

Note that the Vertex class has been extended to include two special-purpose data members:

- has_camera: a Boolean representing whether or not the room has a camera, and
- visited: a Boolean to help with the depth-first-search algorithm.

# Counting Exit Paths

The prisoner wants to know how many exit paths exist. Note that the actual paths are not listed, only the total count is displayed. Exit paths must avoid all rooms that contain cameras. In the example 3x4 prison above, 4 distinct exit paths exist:

ASSET 2

The red, blue, green and purple lines show the 4 distinct paths the prisoner could take to get to the exit, while avoiding the cameras.

The count_exit_paths() function uses the depth-first-search algorithm to determine how many paths exist in the graph from start_vertex to exit_vertex that do not pass through any vertex, v, where v.has_camera is True.

For example, the following program will output the value "4" for the 3x4 prison shown above:

```python
import sys
prison_filename = sys.argv[1]
prison_graph, prisoner_vertex, exit_vertex = create_graph(prison_filename)
num_paths = count_exit_paths(prison_graph, prisoner_vertex, exit_vertex)
print(num_paths)

```

Hint: count_exit_paths() can be implemented with recursion!

## Available prison data files:

You are encouraged to create your own prison data files to test specific cases on your own computer. The following data files are available for testing in the zyLab environment below by entering the filename as a command-line argument.

- `prison_3x4.txt` - A data file that defines the 3x4 example prison shown in this specification, with 4 distinct exit paths.
- `prison_8x8.txt` - A medium-sized prison with 224 distinct exit paths.
- `prison_15x12.txt` - A large prison with 18,186 distinct exit paths.
