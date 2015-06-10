graph = {
    "1": ["2", "3", "5", "10"],
    "2": ["4", "1"],
    "3": ["1", "6"],
    "4": ["2", "5", "6"],
    "5": ["4", "1"],
    "6": ["3", "4", "7"],
    "7": ["6", "8"],
    "8": ["7", "9"],
    "9": ["8", "10"],
    "10": ["9", "1"],
    "11": ["12"],
    "12": ["11"]
}

"""
def bfs(graph, start, end):
    visited = set()
    queue = []
#    path_to[x] = y
#    if we go to x through y
    path_to = {}

    queue.append(start)
    visited.add(start)
    path_to[start] = None
    found = False
    path_length = 0

    while len(queue) != 0:
        current_node = queue.pop(0)
        if current_node == end:
            return True
        for neighbour in graph[current_node]:
            if neighbour not in visited:
                path_to[neighbour] = current_node
                visited.add(neighbour)
                queue.append(neighbour)
    if found:
        while path_to[end] is not None:
            path_length += 1
            end = path_to[end]

    return path_length

result = bfs(graph, "1", "9")
print(result)
"""

graph1 = {'A': ['B', 'D', 'E'],
          'B': ['C'],
          'C': ['D', 'E'],
          'D': ['C', 'E'],
          'E': ['B']}


def BreadthFirstLevels(G, root):
    """
    Generate a sequence of bipartite directed graphs, each consisting
    of the edges from level i to level i+1 of G. Edges that connect
    vertices within the same level are not included in the output.
    The vertices in each level can be listed by iterating over each
    output graph.
    """
    visited = set()
    currentLevel = [root]
    while currentLevel:
        for v in currentLevel:
            visited.add(v)
        nextLevel = set()
        levelGraph = {v: set() for v in currentLevel}
        for v in currentLevel:
            for w in G[v]:
                if w not in visited:
                    levelGraph[v].add(w)
                    nextLevel.add(w)
        return levelGraph
        currentLevel = nextLevel

print(BreadthFirstLevels(graph1, "C"))
