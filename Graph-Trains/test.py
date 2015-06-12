import networkx as nx
G = nx.MultiDiGraph()
G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])
G.add_edge('A', 'B', weight=5)
G.add_edge('B', 'C', weight=4)
G.add_edge('C', 'D', weight=8)
G.add_edge('D', 'C', weight=8)
G.add_edge('D', 'E', weight=6)
G.add_edge('A', 'D', weight=5)
G.add_edge('C', 'E', weight=2)
G.add_edge('E', 'B', weight=3)
G.add_edge('A', 'E', weight=7)

#print(G.edges())
# print([p for p in nx.all_simple_paths(G, source='A', target='C', cutoff=3)])
#print(nx.shortest_path(G, source='A', target='C', weight=10))
# print(nx.all_pairs_dijkstra_path_length(G))
# print(nx.shortest_path(G, source='A', target='E'))

"""
def split_input(path):
    letter_input = path.replace("-", "")
    n = 2
    return [letter_input[i:i+n] for i in range(0, len(letter_input)-1, 1)]


def first_five():
    test_list = split_input("A-B-C")
    print(test_list)
    result = 0
    for element in test_list:
        result += nx.dijkstra_path_length(G, element[0], element[1])
    print(result)


def eight():
    return nx.dijkstra_path_length(G, source='A', target='C')
print(eight())
"""


# print(nx.all_neighbors(G, 'C'))
# print(G.successors('C'))
# print(nx.single_source_dijkstra_path(G, source='A'))

"""
def six():
    neighbours = G.successors('C')
    for neighbour in neighbours:
        result = ['C'] + nx.shortest_path(G, source=neighbour, target='C')
        if len(result) < 5:
            print(result)
"""


"""
def nine():
    neighbours = G.successors('B')
    for neighbour in neighbours:
        result = nx.dijkstra_path_length(
            G, source='B', target=neighbour) + nx.dijkstra_path_length(
            G, source=neighbour, target='B')
        print(result)
"""
