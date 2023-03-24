import bisect
import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
dp = [numbers[0]]


for i in range(N):
    if numbers[i] > dp[-1]:
        dp.append(numbers[i])
    else:
        index = bisect.bisect_left(dp, numbers[i])
        dp[index] = numbers[i]

print(len(dp))