import sys

n = int(sys.stdin.readline())

cost = []
for i in range(n):
    a,b,c = map(int,sys.stdin.readline().split())
    cost.append([0,a,b,c])

pi = [[0,0,0,0] for _ in range(n+1)]



for i in range(1,n+1):
    if i == 1:
        pi[1][1] = cost[0][1]
        pi[1][2] = cost[0][2]
        pi[1][3] = cost[0][3]
    else:
        pi[i][1] = min(pi[i-1][2],pi[i-1][3]) + cost[i-1][1]
        pi[i][2] = min(pi[i-1][1],pi[i-1][3]) + cost[i-1][2]
        pi[i][3] = min(pi[i-1][1],pi[i-1][2]) + cost[i-1][3]
ans = min(pi[n][1:4])
print(ans)