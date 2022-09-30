# -*- coding:utf-8 -*-
# n*n 크기 시험관  (1 ≤ N ≤ 200, 1 ≤ K ≤ 1,000)
# 바이러스 1~k
# 바이러스 위치 행렬
# s초, x, y 위치에 존재하는 바이러스 종류 (0 ≤ S ≤ 10,000, 1 ≤ X, Y ≤ N)
# 모든 바이러스 1초마다 상하좌우 증식
# 매초마다 번호가 낮은 바이러스부터 증식. 빈칸에만 증식 가능

# 1. 오답
# 증식(matrix, kind): 배열 반복
# 칸이 kind일때 상하좌우 dfs 호출
# dfs 좌표 유효하고 빈칸이면 바이러스 적용, 상하좌우 재귀호출
# -> 시간복잡도 n^2*s*k -> 너무 높음..
# 빈칸 기준으로 상하좌우 가장 작은 바이러스로 업데이트
# -> 시간복잡도 s*n^2

from collections import deque
# n, k = map(int, input().split())
# matrix = []
# for _ in range(n):
#     matrix.append(list(map(int, input().split())))


# def append_virus(matrix, kind):
#     n = len(matrix)
#     m = len(matrix[0])
#     d_y = [0, -1, 0, 1]
#     d_x = [1, 0, -1, 0]

#     def dfs(y, x, c):
#         if 0 <= x < n and 0 <= y < m:
#             if matrix[y][x] == 0 and c == 1:
#                 matrix[y][x] = kind
#             if matrix[y][x] == kind:
#                 for d in range(4):
#                     dfs(y+d_y[d], x+d_x[d], c+1)
#     for i in range(n):
#         for j in range(m):
#             if matrix[i][j] == kind:
#                 dfs(i, j, 0)


# s, x, y = map(int, input().split())
# d_y = [0, -1, 0, 1]
# d_x = [1, 0, -1, 0]
# for _ in range(s):
#     for kind in range(1, k+1):
#         append_virus(matrix, kind)

# print(matrix)
# print(matrix[y-1][x-1])

# 2. 큐를 사용한 bfs
# 바이러스가 있는 칸 = 출발해야할 지점으로 판단
# 큐에 바이러스 종류, 출발점, 시간 담음
# 바이러스 오름차순으로 담아서 오름차순으로 탐색될수 있도록 함
# s가 같은것부터(같은 높이) 순회(선입선출)
# 탐색하면서 4방향 넣고 매트릭스 업데이트

n, k = map(int, input().split())
matrix = []
virus = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
    for j in range(n):
        if matrix[i][j] != 0:
            virus.append((matrix[i][j], 0, i, j))

target_s, target_y, target_x = map(int, input().split())

d_y = [0, -1, 0, 1]
d_x = [1, 0, -1, 0]
virus.sort()
queue = deque(virus)
while queue:
    v, s, y, x = queue.popleft()
    if s == target_s:
        break
    for d in range(4):
        nx = x+d_x[d]
        ny = y+d_y[d]
        if 0 <= nx < n and 0 <= ny < n:
            if matrix[ny][nx] == 0:
                matrix[ny][nx] = v
                queue.append((v, s+1, ny, nx))
print(matrix)
print(matrix[target_y-1][target_x-1])
