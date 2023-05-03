from graphviz import Digraph


def visualize_graph(graph):
    dot = Digraph()

    # Add nodes
    for hubs_list in graph.adjacency_list:
        dot.node(str(hubs_list))

    # Add edges
    for node1 in graph.adjacency_list:
        for node2, distance in graph.adjacency_list.get(hub1):
            dot.edge(str(hub1), str(hub2), label=str(distance))

    dot.render('graph', view=True)
