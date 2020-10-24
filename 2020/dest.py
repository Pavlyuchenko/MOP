import math


class Node:
    def __init__(self, zatopeno=False):
        self.visited = False
        self.distance = math.inf

        self.connected_nodes = []
        self.zatopeno = zatopeno

    def connect(self, other):
        self.connected_nodes.append(other)
        other.connected_nodes.append(self)


def init(priklad_choose=1):

    if priklad_choose == 1:
        # S inputem

        nodes_count, paths_count, limit_count = [
            int(x) for x in input().split(" ")]

        zatopene_nodes = [int(x) for x in input().split(" ")]

        nodes = [Node() if zatopene_nodes[i] == 0 else Node(True)
                 for i in range(nodes_count)]

        for i in range(paths_count):
            first, second = [int(x) for x in input().split(" ")]
            nodes[first].connect(nodes[second])

    elif priklad_choose == 2:
        # Easy příklad impossible

        nodes_count, paths_count, limit_count = 5, 4, 2
        zatopene_nodes = [int(x) for x in "0 1 0 0 0".split(" ")]
        join_nodes = ["0 1", "1 2", "2 3", "3 4"]

    elif priklad_choose == 3:
        # Easy příklad possible

        nodes_count, paths_count, limit_count = 5, 4, 2
        zatopene_nodes = [int(x) for x in "0 0 0 1 1".split(" ")]
        join_nodes = ["0 1", "1 2", "2 3", "3 4"]

    elif priklad_choose == 4:
        # Harder z papieru

        nodes_count, paths_count, limit_count = 10, 14, 2
        zatopene_nodes = [int(x) for x in "0 0 1 1 0 0 1 0 0 0".split(" ")]
        join_nodes = ["0 1", "0 2", "0 3", "1 4", "1 6", "2 5", "3 5",
                      "3 7", "4 5", "5 6", "5 7", "6 8", "7 9", "8 9"]
    elif priklad_choose == 5:
        # Problematikos

        nodes_count, paths_count, limit_count = 11, 11, 2
        zatopene_nodes = [int(x) for x in "0 0 0 0 0 0 1 0 0 0 0".split(" ")]
        join_nodes = ["0 1", "0 6", "1 2", "2 3", "3 4", "4 5", "5 8",
                      "6 7", "7 8", "8 9", "9 10"]

    elif priklad_choose == 6:
        # Problematikos grandos

        nodes_count, paths_count, limit_count = 24, 36, 6
        zatopene_nodes = [
            int(x) for x in "0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0".split(" ")]
        join_nodes = ["0 1", "0 3", "0 6", "1 2", "1 3", "1 4", "2 6", "2 7", "3 8", "4 7",  # 10
                      "5 8", "6 9", "6 10", "7 11", "7 12", "8 13", "8 14", "9 15", "10 15",  # 9
                      "10 16", "11 15", "11 17", "12 17", "12 18", "13 18", "14 18", "15 20",  # 8
                      "15 21", "16 19", "17 20", "18 21", "18 22", "19 23", "20 23", "21 23", "22 23"]  # 9

    if priklad_choose != 1:
        nodes = [Node() if zatopene_nodes[i] == 0 else Node(True)
                 for i in range(nodes_count)]

        for join in join_nodes:
            first, second = join.split(" ")
            first, second = int(first), int(second)

            nodes[first].connect(nodes[second])

    nodes[-1].distance = 0
    queue = [nodes[-1]]
    min_dist = -1

    while len(queue) != 0:
        curr = queue.pop(0)

        for next in curr.connected_nodes:
            if not next.visited:
                if not(curr.zatopeno and curr.distance > limit_count):
                    queue.append(next)

                    next.distance = curr.distance + 1
                    next.visited = True

        if not(curr.zatopeno and curr.distance > limit_count):
            if curr == nodes[0]:
                min_dist = curr.distance
                break

    print(min_dist)


init(4)
