import sys

n = int(sys.stdin.readline())

pi = [0 for _ in range(n+1)]

for i in range(1,n+1):
    if i == 1:
        pi[1] = 1
    elif i == 2:
        pi[2] = 2
    else:
        pi[i] = ((pi[i-2]%10007) + (pi[i-1]%10007))%10007

print(pi[n])
