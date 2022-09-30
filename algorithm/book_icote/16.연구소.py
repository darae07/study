# -*- coding:utf-8 -*-
# n, m (3<=n,m<=8)
# 벽 조합 = 모든 좌표 목록 중 3개 조합
# 모든 조합에 대해 검사
# 벽 적용
# 바이러스 적용
# 안전지대 개수 세기
# 조합마다 안전지대 개수 갱신
from itertools import combinations


def append_virus(matrix):
    n = len(matrix)
    m = len(matrix[0])
    direction_y = [0, -1, 0, 1]
    direction_x = [1, 0, -1, 0]

    def dfs(y, x):
        if 0 <= y < n and 0 <= x < m and matrix[y][x] == 0:
            matrix[y][x] = 2
            for i in range(4):
                dfs(y+direction_y[i], x+direction_x[i])
    for y in range(n):
        for x in range(m):
            if matrix[y][x] == 2:
                for i in range(4):
                    dfs(y+direction_y[i], x+direction_x[i])


def count_safe(matrix):
    n = len(matrix)
    m = len(matrix[0])
    count = 0
    for y in range(n):
        for x in range(m):
            if matrix[y][x] == 0:
                count += 1
    return count


n, m = map(int, input().split())
origin_matrix = []
for _ in range(n):
    origin_matrix.append(list(map(int, input().split())))

points = []
for i in range(n):
    for j in range(m):
        points.append((i, j))

safe_area = 0
walls_combination = list(combinations(points, 3))
for walls in walls_combination:
    matrix = [row[:] for row in origin_matrix]
    count = 0  # 오답포인트. 3지점 모두 벽을 세울수 있을때만 검사
    for (y, x) in walls:
        if matrix[y][x] == 0:
            matrix[y][x] = 1
            count += 1
    if count != 3:
        continue
    append_virus(matrix)
    curr_safe_count = count_safe(matrix)
    safe_area = max(safe_area, curr_safe_count)

print(safe_area)
