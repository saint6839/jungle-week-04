import sys

n = int(sys.stdin.readline())

dp = [[0,[]] for _ in range(1000001)]

dp[1][0] = 0
dp[1][1].append(1)
dp[2][0] = 1
dp[2][1].append(1)
dp[2][1].append(2)
dp[3][0] = 1
dp[3][1].append(1)
dp[3][1].append(3)

for i in range(4,n+1):
    if i%2 == 0:
        if i%3 == 0:
            if min(dp[i//3][0],dp[i//2][0],dp[i-1][0]) == dp[i//3][0]:
                dp[i][0] = dp[i//3][0] + 1
                dp[i][1] = dp[i//3][1] + [i]
            elif min(dp[i//3][0],dp[i//2][0],dp[i-1][0]) == dp[i//2][0]:
                dp[i][0] = dp[i//2][0] + 1
                dp[i][1] = dp[i//2][1] + [i]
            else:
                dp[i][0] = dp[i-1][0] + 1
                dp[i][1] = dp[i-1][1] + [i]
        else:
            if min(dp[i//2][0],dp[i-1][0]) == dp[i//2][0]:
                dp[i][0] = dp[i//2][0] + 1
                dp[i][1] = dp[i//2][1] + [i]
            else:
                dp[i][0] = dp[i-1][0] + 1
                dp[i][1] = dp[i-1][1] + [i]
    else:
        if i%3 == 0:
            if min(dp[i//3][0],dp[i-1][0]) == dp[i//3][0]:
                dp[i][0] = dp[i//3][0] + 1
                dp[i][1] = dp[i//3][1] + [i]
            else:
                dp[i][0] = dp[i-1][0] + 1
                dp[i][1] = dp[i-1][1] + [i]
        else:
            dp[i][0] = dp[i-1][0] + 1
            dp[i][1] = dp[i-1][1] + [i]

print(dp[n][0])
print(*dp[n][1][::-1],sep=' ')