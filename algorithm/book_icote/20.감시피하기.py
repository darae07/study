# -*- coding:utf-8 -*-
# n 복도 길이
# 행렬 n*n x 빈칸, s 학생, t 선생님
# 벽을 세개 뽑기
# 벽 개수 3이면 선생님 검사함수 호출
# 아니면 매트릭스에 벽 적용, 재귀호출
# 매트릭스 벽 제거
# 벽 조합마다 모든 선생님에대해 검사 -> 학생 만나면 NO, 안만나면 yes
# 선생님 상하좌우 좌표 적용후 빈칸이면 유효하면 재귀호출
# 벽이면 종료, 학생이면 no
# 벽 조합 yes면 정답 yes 업데이트
import time
from itertools import combinations

n = int(input())
matrix = []
teachers = []
spaces = []
for i in range(n):
    matrix.append(list(input().split()))
    for j in range(n):
        if matrix[i][j] == 'T':
            teachers.append((i, j))
        elif matrix[i][j] == 'X':
            spaces.append((i, j))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
answer = 'NO'


def look(y, x, d):
    if 0 <= y < n and 0 <= x < n:
        if matrix[y][x] == 'S':
            return True
        if matrix[y][x] == 'X':
            return look(y+dy[d], x+dx[d], d)
        else:
            return False
    else:
        return False


def search():
    global answer
    for t in teachers:
        for i in range(4):
            lo = look(t[0]+dy[i], t[1]+dx[i], i)
            if lo:
                return
    answer = 'YES'


def make_wall(count):
    if count == 3:
        search()
    else:
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 'X':
                    matrix[i][j] = 'O'
                    make_wall(count+1)
                    matrix[i][j] = 'X'


start = time.time()
# make_wall(0)
walls_comb = list(combinations(spaces, 3))
for walls in walls_comb:
    for (i, j) in walls:
        matrix[i][j] = 'O'
    search()
    if answer == 'YES':
        break
    for (i, j) in walls:
        matrix[i][j] = 'X'
print('time: ', time.time()-start)
print(answer)
