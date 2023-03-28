import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

visited = [[] for _ in range(N + 1)]

small_stones = []
for _ in range(M):
    small_stones.append(int(sys.stdin.readline()))


queue = deque()
queue.append([1, 0, 0])
while queue:
    now, move, count = queue.popleft()
    for i in [move-1, move, move+1]:
        if i > 0:
            next = now + i
            if next == N:
                print(count+1)
                sys.exit()
            elif next > N:
                continue
            elif move not in visited[next] and next not in small_stones:
                visited[next].append(i)
                queue.append([next, i, count+1])
print(-1)

