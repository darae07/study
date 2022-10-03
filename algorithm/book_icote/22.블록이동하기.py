# 보드 초기화 -> 외곽 외벽 추가
# 로봇 위치 초기화 - 집합
# 최소시간 = 최단거리 = bfs
# 큐를 이용한 bfs
# 이동 가능한 위치 방문 안했으면 큐에 추가
# 이동 가능한 위치 구하기
# 로봇 위치 = 집합 (y1,x1)(y2,x2)
# 이동
# 상하좌우 반복 다음 좌표 계산 후 유효하면 배열에 추가
# 회전 - 로봇의 두 좌표 y가 같으면 가로, x가 같으면 세로
# 가로 -> 세로: i=[1,-1], (y1+i,x1) and (y2+i,x2) == 0 이면 이동 가능
#  (y1,x1)(y1+i,x1), (y2,x2)(y2+i,x2) 배열에 추가
# 세로 -> 가로: i=[-1,1], (y1,x1+i) and (y2,x2+i) == 0 이면 이동 가능
#  (y1,x1)(y1,x1+i), (y2,x2)(y2,x2+i) 배열에 추가
# 유효한 이동 위치 배열 반환
from collections import deque


def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    # 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        # 로봇의 두 위치당 다음 좌표 계산
        pos1_n_x, pos1_n_y, pos2_n_x, pos2_n_y = pos1_x + \
            dx[i], pos1_y+dy[i], pos2_x+dx[i], pos2_y+dy[i]
        # 이동 가능하면 추가
        if board[pos1_n_x][pos1_n_y] == 0 and board[pos2_n_x][pos2_n_y] == 0:
            next_pos.append({(pos1_n_x, pos1_n_y), (pos2_n_x, pos2_n_y)})
    # 회전
    # 현재 가로
    if pos1_x == pos2_x:
        for i in [-1, 1]:
            if board[pos1_x+i][pos1_y] == 0 and board[pos2_x+i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x+i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x+i, pos2_y)})
    # 현재 세로
    elif pos1_y == pos2_y:
        for i in [-1, 1]:
            if board[pos1_x][pos1_y+i] == 0 and board[pos2_x][pos2_y+i] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y+i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y+i)})
    return next_pos


def solution(board):
    n = len(board)
    # 보드 확대 -> 외벽 추가
    new_board = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]

    queue = deque()
    visited = []
    # 로봇위치 - 두개의 좌표 집합으로 표현
    pos = {(1, 1), (1, 2)}
    queue.append((pos, 0))

    # bfs
    while queue:
        pos, cost = queue.popleft()
        if (n, n) in pos:
            return cost
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                queue.append((next_pos, cost+1))
                visited.append(next_pos)
    return 0
