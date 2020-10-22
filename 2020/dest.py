import math


class Node:
    def __init__(self, zatopeno=False):
        self.visited = False
        self.distance = math.inf

        self.connected_nodes = []
        self.zatopeno = zatopeno

        self.wet_distance = None
        self.alt_distance = []

    def connect(self, other):
        self.connected_nodes.append(other)
        other.connected_nodes.append(self)


def init():
    priklad_choose = 4

    if priklad_choose == 1:
        # S inputem

        nodes_count, paths_count, limit_count = [
            int(x) for x in input().split(" ")]
        zatopene_nodes = [int(x) for x in input().split(" ")]

        join_nodes = [input() for _ in range(paths_count)]

    elif priklad_choose == 2:
        # Easy příklad

        nodes_count, paths_count, limit_count = 5, 4, 2
        zatopene_nodes = [int(x) for x in "0 0 0 1 1".split(" ")]
        join_nodes = ["0 1", "1 2", "2 3", "3 4"]

    elif priklad_choose == 3:
        # Harder z papieru

        nodes_count, paths_count, limit_count = 10, 14, 2
        zatopene_nodes = [int(x) for x in "0 0 1 1 0 0 1 0 0 0".split(" ")]
        join_nodes = ["0 1", "0 2", "0 3", "1 4", "1 6", "2 5", "3 7",
                      "3 5", "4 5", "5 6", "5 7", "6 8", "7 9", "8 9"]
    elif priklad_choose == 4:
        # Problematikos

        nodes_count, paths_count, limit_count = 11, 11, 2
        zatopene_nodes = [int(x) for x in "0 0 0 0 0 0 1 0 0 0 0".split(" ")]
        join_nodes = ["0 1", "0 6", "1 2", "2 3", "3 4", "4 5", "5 8",
                      "6 7", "7 8", "8 9", "9 10"]

    nodes = [Node() if zatopene_nodes[i] == 0 else Node(True)
             for i in range(nodes_count)]

    for join in join_nodes:
        first, second = join.split(" ")
        first, second = int(first), int(second)

        nodes[first].connect(nodes[second])

    # print("Nodes:", nodes)

    # [print(node.zatopeno) for node in nodes]  # Zatopenost check
    nodes[0].distance = 0

    queue = [nodes[0]]

    min_dist = -1

    while len(queue) != 0:
        curr = queue.pop(0)

        if curr == nodes[-1]:
            min_dist = curr.distance
            break

        if curr.wet_distance == 0:
            continue

        for next in curr.connected_nodes:
            if not next.visited:
                queue.append(next)
                next.distance = curr.distance + 1
                next.visited = True
                if curr.zatopeno and not curr.wet_distance:
                    next.wet_distance = limit_count-1
                if curr.wet_distance:
                    next.wet_distance = curr.wet_distance - 1

    print(min_dist)


init()
