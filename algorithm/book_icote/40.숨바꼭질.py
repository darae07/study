# 1번 헛간 -> 최단 거리가 가장 먼 헛간
# m개의 양방향 통로
# 최단거리 = 지나야 하는 길의 최소 개수
# 출력: 숨을 헛간(여러개면 가장 작은 번호), 거리, 같은 거리인 헛간의 개수

import heapq


def solution(n, root):
    INF = 1e9
    distance = [INF]*(n+1)
    distance[1] = 0

    graph = [[] for _ in range(n+1)]
    for a, b in root:
        graph[a].append(b)
        graph[b].append(a)

    queue = [(0, 1)]
    while queue:
        d, a = heapq.heappop(queue)
        for b in graph[a]:
            dist = d+1
            if dist < distance[b]:
                distance[b] = dist
                heapq.heappush(queue, (dist, b))

    max_value = 0
    for v in distance:
        if v != INF:
            max_value = max(max_value, v)
    long = [i for i in range(n+1) if distance[i] == max_value]
    long.sort()
    if len(long) == 0:
        return [0, 0, 0]
    return [long[0], max_value, len(long)]


print(solution(6, [(3, 6), (4, 3), (3, 2), (1, 3), (1, 2), (2, 4), (5, 2)]))
