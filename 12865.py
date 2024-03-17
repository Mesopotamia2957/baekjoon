N, K = map(int, input().split())  # Number of items and knapsack capacity
items = []
for _ in range(N):
    W, V = map(int, input().split())  # Weight and value of each item
    items.append((W, V))

# Initialize DP table
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

# Populate DP table
for i in range(1, N + 1):
    for w in range(1, K + 1):
        if items[i-1][0] <= w:  # If current item can fit in the knapsack
            dp[i][w] = max(dp[i-1][w],  # Not taking the item
                           dp[i-1][w-items[i-1][0]] + items[i-1][1])  # Taking the item
        else:
            dp[i][w] = dp[i-1][w]

print(dp[N][K])  # Maximum value that can be achieved within the given weight limit
