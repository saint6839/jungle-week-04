import sys

N, K = map(int, sys.stdin.readline().split())

coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))

coins.sort(reverse=True)

result = 0
for coin in coins:
    result += K // coin
    K = K % coin

print(result)