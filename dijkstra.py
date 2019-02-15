from heapq import *
from collections import defaultdict


def dijkstra(edges, start, end):
    # build a graph
    graph = defaultdict(list)
    for v1, v2, dist_cur in edges:
        graph[v1].append([dist_cur, v2])
        # TODO: uncomment following line to make the graph undirected
        # graph[v2].append([dist_cur, v1])

    # prepare
    queue = [(0, start, "")]
    distances = dict()

    # start main loop
    while queue:
        dist_total, v1, path = heappop(queue)
        if v1 not in distances:
            distances[v1] = dist_total
            path = path + " -> " + v1
            if v1 == end:
                return dist_total, path[4:]
            for dist_curr, v2 in graph[v1]:
                dist_next = dist_total + dist_curr
                heappush(queue, (dist_next, v2, path))

    return float("inf"), ""


if __name__ == "__main__":
    edges = [("A", "B", 7),
             ("A", "D", 5),
             ("B", "C", 8),
             ("B", "D", 9),
             ("B", "E", 7),
             ("C", "E", 5),
             ("D", "E", 15),
             ("D", "F", 6),
             ("E", "F", 8),
             ("E", "G", 9),
             ("F", "G", 11)]

    distance, path = dijkstra(edges, "A", "G")
    print("Path: {}, Distance: {}".format(path, distance))
