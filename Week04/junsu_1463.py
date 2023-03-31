import sys

n = int(sys.stdin.readline())

pi=[0 for _ in range(n+1)]
for i in range(1,n+1):
    if i == 1:
        pi[i] = 0
    elif i == 2:
        pi[i] = 1
    elif i == 3:
        pi[i] = 1
    else:
        if i%2 == 0:
            if i%3 == 0:
                pi[i] = min(pi[i//3],pi[i//2],pi[i-1]) + 1
            else:
                pi[i] = min(pi[i//2],pi[i-1]) + 1
        else:
            if i%3 == 0:
                pi[i] = min(pi[i//3],pi[i-1]) + 1
            else:
                pi[i] = pi[i-1] + 1
print(pi[n])