def knapsack(weights, values, capacity):
    n = len(weights)
    memo = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] > j:
                memo[i][j] = memo[i - 1][j]
            else:
                memo[i][j] = max(memo[i - 1][j], values[i - 1] + memo[i - 1][j - weights[i - 1]])

    return memo[n][capacity]


if __name__ == "__main__":
    weights = [10, 20, 5, 7, 9]
    values = [2, 1, 100, 20, 2]
    capacity = 40
    print(knapsack(weights, values, capacity))
