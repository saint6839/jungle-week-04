import sys


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    coin = map(int, sys.stdin.readline().split())
    m = int(sys.stdin.readline())

    dp = [0] * 10001
    dp[0] = 1

    # 반복문을 통해 코인을 확인
    for i in coin:
        # 반복문을 통해 코인으로 1원부터 m원까지 만들 수 있는 경우의 수를 확인
        for j in range(1, m + 1):
            if j - i >= 0:
                dp[j] += dp[j - i]

    print(dp[m])