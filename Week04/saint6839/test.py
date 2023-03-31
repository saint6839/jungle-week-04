import sys

words1 = [0] + list(sys.stdin.readline().rstrip())
words2 = [0] + list(sys.stdin.readline().rstrip())

dp = [["" for _ in range(len(words1))] for _ in range(len(words2))]

# print(*dp , sep='\n')
# print(words1)
# print(words2)
for i in range(1, len(words2)):
    for j in range(1, len(words1) ):
        if words2[i] == words1[j]:
            dp[i][j] = dp[i-1][j-1] + words2[i]
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
        # print(*dp, sep='\n')
print(len(dp[len(words2)-1][-1]))
print(dp[len(words2)-1][-1])
