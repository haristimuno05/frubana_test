

def add_node_in_the_graph(graph, initial_node, destination_node):
    """
    Method to add a node in the graph
    If the initial_node already exists, the destination_node is added
    to a list initial_node. Otherwise, the initial_node is crated.

    :param graph: dictionary that represents the graph
    :param initial_node: initial node
    :param destination_node: des
    :return: graph dict
    """

    if initial_node in graph:
        graph[initial_node] = graph[initial_node] + [destination_node]
    else:
        graph[initial_node] = [destination_node]
    return graph


def get_path(graph, initial_node, destination_node):
    """
    Method to calculate the path between an initial_node and destination_node

    :param graph: dictionary that represents the graph
    :param initial_node: initial node
    :param destination_node: destination node
    :return: list that contains the path between two nodes given
    """
    stack = [(initial_node, [initial_node])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == destination_node:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


if __name__ == '__main__':
    """Principal method"""

    nodes = int(input())  # read number of nodes
    graph = dict()
    colors_nodes = dict()
    colors = input().split(' ')  # read nodes' colors

    # for each node, fills its color in a dict
    for c in range(nodes):
        colors_nodes[str(c+1)] = int(colors[c])

    # fill the bidirectional graph
    for n in range(nodes-1):
        node1, node2 = input().split(' ')

        add_node_in_the_graph(graph, node1, node2)
        add_node_in_the_graph(graph, node2, node1)

    # convert arrays to set
    for values in graph:
        graph[values] = set(graph[values])

    # for each node calculate all the path and the different colors
    for i in range(1, nodes+1):
        sum_different_colors = 1
        for j in range(1, nodes+1):
            if i != j:
                # get the path between i and j
                path = list(get_path(graph, str(i), str(j)))
                sum_result = []
                for p in path[0]:
                    # save the different colors
                    if colors_nodes[p] not in sum_result:
                        sum_result.append(colors_nodes[p])
                # different colors
                sum_different_colors += len(sum_result)
        print(sum_different_colors)
