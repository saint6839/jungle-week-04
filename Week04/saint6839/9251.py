import sys

first_words = sys.stdin.readline().rstrip()
second_words = sys.stdin.readline().rstrip()

dp = [[0 for _ in range(len(second_words)+1)] for _ in range(len(first_words)+1)]

for i in range(1, len(first_words)+1):
    for j in range(1, len(second_words)+1):
        if first_words[i-1] == second_words[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])