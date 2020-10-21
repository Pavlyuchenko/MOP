import math


class Node:
    def __init__(self, zatopene=False):
        self.visited = False
        self.distance = math.inf

        self.connected_nodes = []
        self.zatopene = zatopene

        self.home = False

    def connect(self, other):
        self.connected_nodes.append(other)
        other.connected_nodes.append(self)


def init():
    """nodes_count, paths_count, limit_count = [
        int(x) for x in input().split(" ")]  # node = křižovatka, path = cesta, limit = kolik zvládne cest bez rýmy
    zatopene_nodes = input()

    join_nodes = [input() for _ in range(paths_count)]"""

    # Easy příklad

    """ nodes_count, paths_count, limit_count = 5, 4, 2
    zatopene_nodes = "0 0 0 1 1"
    join_nodes = ["0 1", "1 2", "2 3", "3 4"] """

    # Harder z papieru
    nodes_count, paths_count, limit_count = 10, 14, 2
    zatopene_nodes = [int(x) for x in "0 0 1 1 0 0 1 0 0 0".split(" ")]
    join_nodes = ["0 1", "0 2", "0 3", "1 4", "1 6", "2 5",
                  "3 5", "3 7", "4 5", "5 6", "5 7", "6 8", "7 9", "8 9"]

    nodes = [Node() if zatopene_nodes[i] == 0 else Node(True)
             for i in range(nodes_count)]

    connect_nodes(join_nodes, nodes)

    print("Nodes:", nodes)

    # [print(node.zatopene) for node in nodes] # Zatopenost check
    nodes[-1].home = True
    nodes[-1].distance = 0

    print(graph_traversal(nodes[0]))

    [print(node.distance) for node in nodes]


def connect_nodes(joined_nodes, nodes):
    for join in joined_nodes:
        first, second = join.split(" ")
        first, second = int(first), int(second)

        nodes[first].connect(nodes[second])


def graph_traversal(node):
    node.visited = True
    min_distance = math.inf

    for i in node.connected_nodes:
        print("s")
        if i.visited:
            if i.distance < min_distance:
                min_distance = i.distance + 1
        else:
            node_distance = graph_traversal(i)
            if node_distance.distance < min_distance:
                min_distance = node_distance.distance

    if node.distance == 0:
        return 0

    node.distance = min_distance + 1

    print(node.distance)

    return node.distance


init()
