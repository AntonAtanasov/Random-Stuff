graph = {'A': ['B', 'D', 'E'],
         'B': ['C'],
         'C': ['D', 'E'],
         'D': ['C', 'E'],
         'E': ['B']}


def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath:
                    return newpath
        return None


def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths


def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

"""
def findPaths(G, u, n):
    if n == 0:
        return [[u]]
    paths = [[u] + path for neighbor
             in G.neighbors(u) for path
             in findPaths(G, neighbor, n - 1) if u not in path]
    return paths
"""

# print(find_path(graph, "A", "D"))
# print(find_shortest_path(graph, "A", "D"))
# print(find_all_paths(graph, "A", "D"))
# print(find_shortest_path(graph, "B", "B"))

"""
user_input = "A-E-B-C-D"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter_input = user_input.replace("-", "")
for letter in letter_input:
    new_alpha = alphabet.replace(letter, "")
>>> G.remove_nodes_from(new_alpha)

>>> G.nodes()
[1, 2, 3, 'spam']
>>> G.remove_edge(1,3)
"""
#print(find_all_paths(graph, 'C', ))
#print(findPaths(graph, 'C', 3))
print(find_all_paths(graph, 'E', 'C'))
