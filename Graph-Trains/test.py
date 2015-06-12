import networkx as nx


# takes a list of nodes as input and divides them into overlapping pairs
def split_input(path):
    letter_input = path.replace("-", "")
    n = 2
    return [letter_input[i:i+n] for i in range(0, len(letter_input)-1, 1)]


def first_five(graph, path, number):
    test_list = split_input(path)
    # print(test_list)
    result = 0
    for element in test_list:
        # checks if current pair of nodes are neighbors
        if element[1] not in graph.successors(element[0]):
            result = 0
        else:
            result += nx.dijkstra_path_length(graph, element[0], element[1])
    if result == 0:
        result = "NO SUCH ROUTE"
    return "Output #{}: {}".format(number, result)


def six(graph, node):
    counter = 0  # counter for the number of trips
    neighbours = graph.successors(node)
    for neighbour in neighbours:
        result = [node] + nx.shortest_path(
            graph, source=neighbour, target=node)
# check for number of required stops
        if len(result) < 5:
            counter += 1
    return "Output #6: {}".format(counter)


def eight_and_nine(graph, source, target, number):
    if source == target:
        neighbours = graph.successors(source)
        for neighbour in neighbours:
            result = nx.dijkstra_path_length(
                graph, source=source,
                target=neighbour) + nx.dijkstra_path_length(
                graph, source=neighbour, target=target)
    else:
        result = nx.dijkstra_path_length(graph, source=source, target=target)
    return "Output #{}: {}".format(number, result)


def main():
    user_input = []  # stores edges with assigned weight(e.g. AB5, BC4)
    node_set = set()  # stores nodes

# basic console UI
    while True:
        choice = input("Enter: ")
        if choice == 'exit':
            break
        else:
            user_input.append(choice)

    for element in user_input:
        node_set.add(element[0])
        node_set.add(element[1])
    G = nx.MultiDiGraph()
    G.add_nodes_from(node_set)

    for element in user_input:
        G.add_edge(element[0], element[1], weight=int(element[2]))

    print(first_five(G, "A-B-C", 1))
    print(first_five(G, "A-D", 2))
    print(first_five(G, "A-D-C", 3))
    print(first_five(G, "A-E-B-C-D", 4))
    print(first_five(G, "A-E-D", 5))
    print(six(G, 'C'))
    print(eight_and_nine(G, 'B', 'B', 8))
    print(eight_and_nine(G, 'A', 'C', 9))

if __name__ == '__main__':
    main()
