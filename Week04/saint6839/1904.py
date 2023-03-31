import sys

N = int(sys.stdin.readline())

dp = [1, 2]

for i in range(1, N):
    dp.append((dp[i] + dp[i-1]) % 15746)

print(dp[N-1])
