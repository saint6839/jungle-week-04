import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())

    ranks = []
    for _ in range(N):
        ranks.append(list(map(int, sys.stdin.readline().split())))

    ranks.sort(key=lambda x:(x[0]))

    results = []
    first_max = 0
    second_max = 0
    for rank in ranks:
        if not results:
            results.append(rank)
            first_max = rank[0]
            second_max = rank[1]
            continue
        if first_max < rank[0] and second_max < rank[1]:
            continue

        if first_max > rank[0]:
            first_max = rank[0]
        if second_max > rank[1]:
            second_max = rank[1]
        results.append(rank)

    print(len(results))

