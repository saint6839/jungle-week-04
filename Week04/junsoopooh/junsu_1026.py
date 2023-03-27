import sys

n = int(sys.stdin.readline())
list_a = list(map(int,sys.stdin.readline().split()))
list_b = list(map(int,sys.stdin.readline().split()))

s = 0
for i in range(n):
    s += min(list_a) * max(list_b)
    list_a.pop(list_a.index(min(list_a)))
    list_b.pop(list_b.index(max(list_b)))

print(s)