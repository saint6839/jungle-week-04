import sys

n = int(sys.stdin.readline())
ropes = []
for _ in range(n):
    rope = int(sys.stdin.readline())
    ropes.append(rope)

ropes.sort()
list = []
tmp = 0
for i in range(n):
    tmp = ropes[i] * (n-i)
    list.append(tmp)
ans = max(list)
print(ans)