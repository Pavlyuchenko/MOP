import math
from time import time

t = time()


class Node:
    def __init__(self, zatopeno=False):
        self.visited = False
        self.distance = math.inf

        self.connected_nodes = []
        self.zatopeno = zatopeno

        self.wet_distance = None
        self.alt_distance = {}

    def connect(self, other):
        self.connected_nodes.append(other)
        other.connected_nodes.append(self)


def init():
    """nodes_count, paths_count, limit_count = [
        int(x) for x in input().split(" ")]  # node = křižovatka, path = cesta,
        limit = kolik zvládne cest bez rýmy
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

    for join in join_nodes:
        first, second = join.split(" ")
        first, second = int(first), int(second)

        nodes[first].connect(nodes[second])

    # print("Nodes:", nodes)

    # [print(node.zatopene) for node in nodes] # Zatopenost check
    nodes[0].distance = 0

    queue = [nodes[0]]

    while len(queue) != 0:
        curr = queue.pop(0)

        if curr == nodes[-1]:
            break
        
        if curr.wet_distance <= 0:
            curr.distance = curr.alt_distance[0]
            # tutaj som skončil
    
        if curr.wet_distance:
            for next in curr.connected_nodes:
                if not next.visited:
                    queue.append(next)
                    next.distance = curr.distance + 1
                    next.visited = True
                    next.wet_distance = curr.wet_distance - 1
                    
                if next.visited and next.wet_distance:
                    next.alt_distance.append(curr.distance + 1)
        else:
            for next in curr.connected_nodes:
                if not next.visited:
                    queue.append(next)
                    next.distance = curr.distance + 1
                    next.visited = True
                    if next.zatopeno:
                        next.wet_distance = limit_count

                if next.visited and next.wet_distance:
                    next.alt_distance.append(curr.distance + 1)

    print(curr.distance)


print(time() - t)