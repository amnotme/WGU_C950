import sys
from graph import Graph, Vertex

def create_graph(filename):
    # TO-DO: read the lines in the specified file
    # to create a Graph object. Returns 3 values:
    #
    #     prison_graph, prisoner_vertex, exit_vertex


    # The following line is here as a placeholder. Replace
    # this line with the real return values once you
    # load them from the prison data file.
    return None, None, None

def count_exit_paths(g, start_vertex, exit_vertex):
    # TO-DO: use depth-first-search to count how many distinct
    # paths exist from the given start vertex to the given
    # exit vertex. May be used recursively, if desired.
    

    # The following line is here as a placeholder. Replace
    # this line with the real return value once you determine
    # the correct result.
    return 0


if __name__ == "__main__":
    prison_filename = sys.argv[1]
    prison_graph, prisoner_vertex, exit_vertex = create_graph(prison_filename)
    num_paths = count_exit_paths(prison_graph, prisoner_vertex, exit_vertex)
    print(num_paths)
