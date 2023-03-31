import sys

n = int(sys.stdin.readline())

dp = [0 for _ in range(n+2)]

dp[1] = 1
dp[2] = 1

def fibo(number):
    if dp[number] > 0:
        return dp[number]
    elif number > 1:
        dp[number] = fibo(number - 1) + fibo(number - 2)
        return dp[number]

print(fibo(n))
