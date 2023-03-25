import sys

a = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
dp = [0 for _ in range(1001)]


for i in range(a):
    for j in range(i):
        if nums[i] > nums[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))