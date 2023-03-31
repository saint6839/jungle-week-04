import sys

def find_path(current_city, visited):

    # 모든 도시를 방문했다면 visited 가 0b1111의 형태, 0으로 돌아온 값 반환
    if visited == (1 << N) - 1:
        return graph[current_city][0] or INF

    # 현재 도시에서 이미 방문한 적이 있는 상황이라면, 이전의 방문 상황에서 모든 경우의 수를 계산했을 것이다.
    # 때문에 해당 값을 바로 값을 반환하고 더 이상의 방문을 하지 않는다.
    if DP[current_city][visited]:
        return DP[current_city][visited]

    # visited에서 확인할 수 있는 방문하지 않은 도시를 찾아 방문한다.
    tmp = INF
    for next_city in range(N):
        if not visited & (1 << next_city) and graph[current_city][next_city]:
            tmp = min(tmp, find_path(next_city, visited | (1 << next_city)) + graph[current_city][next_city])
    DP[current_city][visited] = tmp
    return tmp


N = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
INF = float('inf')
DP = [[None] * (2**N) for _ in range(N)]

print(find_path(0, 1 << 0))