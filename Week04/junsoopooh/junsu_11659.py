import sys

n,m = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
dp = [0] *100001

for x in range(1,n+1):
    if x == 1:
        dp[x] = nums[0]
    else:
        dp[x] = nums[x-1]+dp[x-1]
ans = []
for _ in range(m):
    i, j = map(int,sys.stdin.readline().split())
    tmp = dp[j]-dp[i-1]
    ans.append(tmp)

print(*ans, sep='\n')