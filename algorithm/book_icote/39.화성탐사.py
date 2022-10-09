# 출발 지점에서 목표 지점까지 최적의 경로
# (0,0) -> (n-1,n-1)지점까지 이동 최소 비용
# 각 위치 이동 최소 비용 존재
# 최단거리 테이블
# 우선순위 큐
# 위치에 이동할 때마다 상하좌우 큐에 추가
# 가까운것부터 뽑아서 계산
# 현재 거리가 더 짧으면 진행, 비용, 상하좌우 큐에 추가

import heapq


def solution(graph):
    INF = 1e9
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n = len(graph)

    distance = [[INF]*n for _ in range(n)]

    x, y = 0, 0
    queue = [(graph[y][x], y, x)]
    # 최단거리 테이블로 구성
    distance[y][x] = graph[y][x]

    while queue:
        dist, y, x = heapq.heappop(queue)
        # 현재 거리가 더 멀면 통과
        if distance[y][x] < dist:
            continue
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            # 좌표 유효하지 않으면 통과
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist+graph[ny][nx]
            # 현재 거리가 더 짧은 경우 진행
            if cost < distance[ny][nx]:
                distance[ny][nx] = cost
                heapq.heappush(queue, (cost, ny, nx))
    print(distance)
    return distance[n-1][n-1]


print(solution([[5, 5, 4], [3, 9, 1], [3, 2, 7]]))
