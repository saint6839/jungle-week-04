import sys

N, K = map(int, sys.stdin.readline().split())


weights = [0]
values = [0]
for _ in range(N):
    weight, value = map(int, sys.stdin.readline().split())
    weights.append(weight)
    values.append(value)

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, K+1):
        if weights[i] <= j:
            dp[i][j] = max(values[i] + dp[i-1][j - weights[i]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])

