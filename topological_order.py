def DFS(graph, visited, ans, i):
    # 1: visited, 0: unvisited, -1: visiting
    # the boolean True means whether it is DAG
    if visited[i] == 1:
        return True
    elif visited[i] == -1:
        return False
    else:
        visited[i] = -1
        for v in graph[i]:
            if DFS(graph, visited, ans, v) == False:
                return False
        visited[i] = 1
        ans.append(i)
        return True

def topological_order(graph):
    ans = list()
    visited = [0] * len(graph)
    is_DAG = True
    for i in range(len(graph)):
        if DFS(graph, visited, ans, i) == False:
            is_DAG = False
            break

    if is_DAG:
        return ans[::-1]
    else:
        return None


if __name__ == "__main__":
    graph = [[3],
             [7],
             [1],
             [2],
             [2],
             [1],
             [5],
             [8, 9],
             [],
             []]
    print(topological_order(graph))
