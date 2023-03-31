import sys

n = int(sys.stdin.readline())
score = []
for _ in range(n):
    score.append(int(sys.stdin.readline()))

dp = [[0, 0] for _ in range(10001)]

for i in range(1,n+1):
    if i == 1:
        dp[i][0] = score[0]
        dp[i][1] = 0
    elif i == 2:
        dp[i][0] = score[1]
        dp[i][1] = score[0] + score[1]
    else:
        dp[i][0] = max(dp[i-2][0],dp[i-2][1]) + score[i-1]
        dp[i][1] = dp[i-1][0] + score[i-1]
        if dp[i][1] < dp[i-1][1]:
            dp[i][1] = dp[i-1][1]
print(max(dp[i]))
