#내꺼, indexerror
import sys

n = int(sys.stdin.readline())

fibo = [0 for _ in range(n+1)]
fibo[1] = 1
fibo[2] = 2
for i in range(3,n+1):
    ans = fibo[i-1] + fibo[i-2]
    fibo[i] = ans%15746
 
print(fibo[n])

#정답
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for k in range(3,n+1):
    dp[k] = (dp[k-1]+ dp[k-2])%15746
print(dp[n])