import sys

n = int(sys.stdin.readline())
score = []
for _ in range(n):
    score.append(int(sys.stdin.readline()))

pi = [[0, 0, 0] for _ in range(n+1)]



for i in range(1,n+1):
    if i == 1:
        pi[1][1] = score[0]
        pi[1][2] = 0
    elif i == 2:
        pi[2][1] = score[1]
        pi[2][2] = score[0] + score[1]
    else:
        pi[i][1] = max(pi[i-2][1],pi[i-2][2]) + score[i-1]
        pi[i][2] = pi[i-1][1] + score[i-1]
ans = max(pi[n])
print(ans)