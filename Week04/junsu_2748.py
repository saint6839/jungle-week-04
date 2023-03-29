import sys
n = int(sys.stdin.readline())

fibo = [0 for _ in range(90)]

fibo[0] = 0
fibo[1] = 1
for i in range(0,n+1):
    if i== 0:
        ans = 0
    elif i == 1:
        ans = 1
    else:
        ans = fibo[i] = fibo[i-1] + fibo[i-2]
    fibo.append(ans)
print(ans)
