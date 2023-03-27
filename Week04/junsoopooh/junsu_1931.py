import sys

n = int(sys.stdin.readline())
table = []
for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())
    table.append([a,b])
table.sort()
table.sort(key=lambda x:x[1])
cnt = 1
time = table[0][1]
for i in range(1,n):
    if table[i][0] >= time:
        cnt += 1
        time = table[i][1]
print(cnt)