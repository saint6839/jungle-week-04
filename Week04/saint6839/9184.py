import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0 for _ in range(M)] for _ in range(N)]
dp[0][0] = board[0][0]

dx = [1, 0, 1]
dy = [0, 1, 1]

for i in range(N):
    for j in range(M):
         for k in range(3):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                dp[nx][ny] = max(dp[nx][ny], dp[i][j] + board[nx][ny])

print(dp[N-1][M-1])