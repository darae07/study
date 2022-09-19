# -*- coding:utf-8 -*-
# n = 보드의 크기
# k = 사과의 개수
# 사과의 위치(행,렬 1부터 인덱싱)
# l = 방향 변환 횟수
# 방향 변환 정보(x=경과 초, c=방향: L왼, D오 90도 회전)
# 보드 사이즈로 행렬 초기화
# 사과 정보 입력
# 뱀 이동정보 입력
# 게임 시작, 초 증가시키며 뱀 이동정보 있을시 회전
# 벽이나 몸에 부딫치면 게임 종료. 언제 끝나는지 확인

# 방향 배열에 담기
# 시작 좌표 초기화
# 방향 변수 초기화
# 뱀 좌표 배열에 담기
# 시간 변수 초기화
# 반복 - 다음 좌표 계산하고 유효하면 매트릭스 업데이트, 뱀에 추가, 꼬리 삭제 수행
# 유효하지 않으면 종료 및 시간 반환
def turn(direction, c):
    return (direction+(1 if c == 'D' else -1)) % 4


n = 10
k = 4
k_list = [(1, 2), (1, 3), (1, 4), (1, 5)]
l = 4
times = [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')]

matrix = [[0]*(n+1) for _ in range(n+1)]
for tup in k_list:
    i, j = tup
    matrix[i][j] = 1

# times = [0]*10001
# for tup in l_list:
#     t, d = tup
#     times[int(t)] = 1 if d == 'D' else -1

# 동남서북
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

x, y = 1, 1
matrix[y][x] = 2
direction = 0
direction_index = 0
tail = [(x, y)]
time = 0
while True:
    time += 1
    nx = x + dx[direction]
    ny = y + dy[direction]
    if 1 <= nx and nx <= n and 1 <= ny and ny <= n and matrix[ny][nx] != 2:
        if matrix[ny][nx] == 0:
            matrix[ny][nx] = 2
            tail.append((nx, ny))
            px, py = tail.pop(0)
            matrix[py][px] = 0
        if matrix[ny][nx] == 1:
            matrix[ny][nx] = 2
            tail.append((nx, ny))
    else:
        print(time)
        break
    x, y = nx, ny
    if direction_index < len(times) and times[direction_index][0] == time:
        direction = turn(direction, times[direction_index][1])
        direction_index += 1
