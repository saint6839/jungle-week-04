import sys
one = sys.stdin.readline().rstrip()
two = sys.stdin.readline().rstrip()

one =['7'] + list(one)

a = len(one)
two = ['8'] + list(two)
b = len(two)
word = []
matrix = [[0 for _ in range(a)] for _ in range(b)]
for i in range(a):
    for j in range(b):
        if two[j] == one[i]:
            matrix[j][i] = matrix[j-1][i-1] + 1
        else:
            matrix[j][i] = max(matrix[j-1][i],matrix[j][i-1])
# for i in range(a): 문자열 순서를 바꿔서넣으면 답이 달라진다.
#     if i != 0 and matrix[b-1][i-1] < matrix[b-1][i]:
#         word.append(one[i])
if word :
    print(matrix[b-1][a-1])
    print(*word, sep='')
else:
    print(0)