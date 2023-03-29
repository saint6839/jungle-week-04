import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def dfs(x, y):
    if not dp[x][y]:
        dp[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[x][y] < board[nx][ny]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

    return dp[x][y]

results = []
for i in range(n):
    for j in range(n):
       results.append(dfs(i, j))

print(max(results))
