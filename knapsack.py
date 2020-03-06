def knapsack(weights, values, capacity):
    n = len(weights)
    memo = [[0] * (capacity + 1) for _ in range(n + 1)]

    for y in range(1, n + 1):
        for x in range(1, capacity + 1):
            if weights[y - 1] > x:
                memo[y][x] = memo[y - 1][x]
            else:
                memo[y][x] = max(memo[y - 1][x], values[y - 1] + memo[y - 1][x - weights[y - 1]])

    return memo[-1][-1]


if __name__ == "__main__":
    weights = [10, 20, 5, 7, 9]
    values = [2, 1, 100, 20, 2]
    capacity = 40
    print(knapsack(weights, values, capacity))
