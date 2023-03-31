import sys

n = int(sys.stdin.readline())

drinks = [0]
for _ in range(n):
    drinks.append(int(sys.stdin.readline()))

if n == 1:
    print(drinks[1])
    sys.exit()

dp = [0 for _ in range(n+3)]

dp[1] = drinks[1]
dp[2] = drinks[1] + drinks[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-2] + drinks[i], dp[i - 3] + drinks[i - 1] + drinks[i])

print(max(dp))