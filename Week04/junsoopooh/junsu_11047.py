import sys

n, k = map(int,sys.stdin.readline().split())

coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))
i = n-1
cnt = 0
while i >= 0:
    if k - coins[i] >= 0:
        cnt += k//coins[i]
        k = k%coins[i]
    else:
        i -= 1
    if k == 0:
        print(cnt)
        break