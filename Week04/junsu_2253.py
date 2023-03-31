import sys

n,m = map(int,sys.stdin.readline().split())
mini = []
for _ in range(m):
    mini.append(int(sys.stdin.readline()))

dp = [[float('inf') for _ in range(int(((8*n+1)**0.5)) + 2)] for _ in range(n+1)]
dp[1][0]=0
for i in range(2,n+1):
    if i in mini:
        continue
    for v in range(1,int((8*i+1)**0.5)+1):
        dp[i][v] = min(dp[i-v][v-1],dp[i-v][v],dp[i-v][v+1])+1

if min(dp[n]) == float('inf'):
    print(-1)
else:
    print(min(dp[n]))