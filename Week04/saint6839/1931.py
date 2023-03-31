import sys

N = int(sys.stdin.readline())

times = []

for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())

    times.append([s, e, e-s])


times.sort(key=lambda x:(x[1], x[0]))
results = []

for time in times:
    if not results:
        results.append(time)
        continue

    if results[-1][1] <= time[0]:
        results.append(time)

print(len(results))