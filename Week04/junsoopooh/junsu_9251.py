import sys

first = list(sys.stdin.readline().rstrip())
l_a = len(first)
second = list(sys.stdin.readline().rstrip())
l_b = len(second)
LCS = [[0 for _ in range(l_b+1)]for _ in range(l_a+1)]

for i in range(l_a+1):
    for j in range(l_b+1):
        if i == 0 or j == 0:
            LCS[i][j] = 0
        elif first[i-1] == second[j-1]:
            LCS[i][j] = LCS[i-1][j-1] +1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

print(LCS[-1][-1])


## 문자열출력하는 코드
# result = []

# while LCS[i][j] > 0:
#     if LCS[i][j] == LCS[i-1][j]:
#         i = i-1
#     elif LCS[i][j] == LCS[i][j-1]:
#         j = j-1
#     else:
#         result.append(i)
#         result.append(j)
#         i = i - 1
#         j = j - 1

# print(result)
