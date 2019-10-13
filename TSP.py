from collections import deque


def TSP(graph):
    # prepare the queue, each element in a queue is (node, mask, path, cost)
    q = deque()
    for node in range(len(graph)):
        q.append((node, 1 << node, [node], 0))

    # prepare the memo, memo[mask][node] records the min cost
    memo = [[float('inf')] * len(graph) for _ in range(1 << len(graph))]

    # start the loop
    cost_min = float('inf')
    opt_path = list()
    while q:
        node, mask, path, cost = q.popleft()

        if mask == (1 << len(graph)) - 1 and cost < cost_min:
            cost_min = cost
            opt_path = list(path)
            continue

        if memo[mask][node] < cost:
            continue

        for node_next in range(len(graph)):
            mask_next = mask | (1 << node_next)
            cost_next = cost + graph[node][node_next]
            if mask_next != mask and cost_next < memo[mask_next][node_next]:
                memo[mask_next][node_next] = cost_next
                q.append((node_next, mask_next, path + [node_next], cost_next))

    return opt_path


if __name__ == "__main__":
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    print(TSP(graph))
