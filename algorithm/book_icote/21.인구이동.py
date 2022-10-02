# -*- coding:utf-8 -*-
# 탐색 가능한 지역 큐, 방문횟수 매트릭스
# 이동 횟수
# 탐색 가능한 지역: 초기값 = 모든 좌표, 연합 발생할때마다 추가
# 방문횟수: 매트릭스 초기값 = -1, 방문할 때마다 이동횟수로 업데이트
# 이동 완료되면 횟수+1

# 탐색 가능한 지역 반복하면서 연합 발생하는지 체크
# 연합체크 - 출발점 기준으로 큐, 연합 생성, 방문 체크
# 큐 bfs -> 가까운 위치부터 상하좌우 탐색
# 좌표값 유효하고 이번에 방문 안한 지점이면 - 현재 도시와 인구차 범위내에 있으면
# -> 큐에 추가, 연합에 추가, 방문 처리
# 연합이 발생했으면 탐색 가능한 지역에 연합 추가하고 반복 계속, 탐색 횟수 기록
# 발생 안했으면 종료 후 탐색횟수 반환

from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
city = deque([(i, j) for i in range(n) for j in range(n)])
union = [[-1]*n for _ in range(n)]
total_count = 0


def process(y, x):
    united = []
    united.append((y, x))
    queue = deque()
    queue.append((y, x))
    union[y][x] = total_count
    summary = graph[y][x]
    count = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[ny][nx] < total_count:
                if l <= abs(graph[ny][nx] - graph[y][x]) <= r:
                    queue.append((ny, nx))
                    union[ny][nx] = total_count
                    summary += graph[ny][nx]
                    count += 1
                    united.append((ny, nx))

    if count > 1:
        val = summary//count
        for i, j in united:
            graph[i][j] = val
            city.append((i, j))
    return count


while True:
    for _ in range(len(city)):
        i, j = city.popleft()
        if union[i][j] < total_count:
            process(i, j)
    if city:
        total_count += 1
    else:
        break

print(total_count)
