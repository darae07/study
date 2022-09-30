# -*- coding:utf-8 -*-
# dfs 오답
from collections import deque
import sys
input = sys.stdin.readline


n, m, k, x = map(int, input().split())
visited = [False] * (n+1)
edges = [[] for _ in range(n+1)]
distance = [n]*(n+1)

for _ in range(m):
    start, to = map(int, input().split())
    edges[start].append(to)

stack = []
stack.append((x, 0))
while len(stack) > 0:
    (start, dist) = stack.pop()
    if visited[start]:
        continue
    visited[start] = True
    distance[start] = min(distance[start], dist)
    for to in edges[start]:
        stack.append((to, dist+1))
    print(stack)
answer = [i for i in range(len(distance)) if distance[i] == k]
answer.sort()
print(distance)
print(answer)

# 2. bfs 정답
n, m, k, x = map(int, input().split())
edges = [[] for _ in range(n+1)]
distance = [-1]*(n+1)
distance[x] = 0

for _ in range(m):
    start, to = map(int, input().split())
    edges[start].append(to)

queue = deque([x])
while queue:
    start = queue.popleft()
    # 방문 가능한 모든 노드에 대해
    for to in edges[start]:
        # 아직 방문하지 않은 노드라면
        if distance[to] == -1:
            # 최단거리 갱신
            distance[to] = distance[start] + 1
            queue.append(to)
answer = [i for i in range(1, n+1) if distance[i] == k]

if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for city in answer:
        print(city)
