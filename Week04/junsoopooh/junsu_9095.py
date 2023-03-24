import sys

t = int(sys.stdin.readline())
ans = []
pi = [0 for _ in range(12)]
pi[1] = 1
pi[2] = 2
pi[3] = 4
for i in range(4,12):
    pi[i] = pi[i-2] + pi[i-1] + pi[i-3]

for _ in range(t):
    num = int(sys.stdin.readline())
    ans.append(pi[num])

print(*ans, sep= '\n')