
# 4*4 크기의 공간
# 각 칸에 물고기 한마리 존재. 번호와 방향
# 물고기 번호 1 - 16
# 방향 1-8
# 상어 0.0시작, 해당 물고기 방향 얻음
# 물고기 이동
# 번호순 - 이동할수 있는 방향 정할때까지 45도 반시계 회전
# 이동 가능하면 이동(물고기 있으면 해당칸 물고기와 위치 바꿈)
# 종료후 상어 이동
# 방향대로 이동, 한번에 여러칸 이동 가능
# 이동한 칸의 물고기 먹고 방향 가짐
# 물고기 없는 칸으로는 이동 불가
# 상어 이동 가능 칸이 없으면 종료
# 먹을수 있는 물고기 번호 최대값

import copy
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
fish = [None]*17
d = 0
INF = 1e9
matrix = [[] for _ in range(4)]
# for i in range(4):
#     a = list(map(int, input().split()))
#     for j in range(0, 8, 2):
#         matrix[i].append((a[j], a[j+1]))
#         fish[a[j]] = [i, j]
# y, x = 0, 0
# first = matrix[0][0]
# fish[first[0]] = None
# d = first[1]
# matrix[0][0] = INF


def move():
    for i in range(1, 17):
        f = fish[i]
        if f:
            cy, cx = f[0], f[1]
            cn, cd = matrix[cy][cx][0], matrix[cy][cx][1]
            ny, nx = cy+dy[cd], cx+dx[cd]
            while ny < 0 or ny >= 4 or nx < 0 or nx >= 4 or matrix[ny][nx] != INF:
                cd = cd+1 if cd < 8 else 1
                ny, nx = cy+dy[cd], cx+dx[cd]
            if matrix[ny][nx]:
                matrix[cy][cx] = matrix[ny][nx]
                fish[matrix[ny][nx][0]] = [cy, cx]
                fish[i] = [ny][nx]
            else:
                matrix[cy][cx] = False
                fish[i] = None
            matrix[ny][nx] = (cn, cd)


# print(matrix)
# print(fish)
# 매트릭스 - [물고기 번호, 방향 인덱스]
# 좌회전함수
# 물고기 찾는 함수 - 물고기 번호로 좌표 반환, 없으면 None(이중 for문)

# 물고기 이동 함수 - 1부터 16까지 반복, 물고기 찾고,
# 있으면 8까지 반복문 안에서 현재 방향으로 물고기 이동 가능한지 확인,
# 가능하면 현재 방향 업데이트 후 물고기 스왑
# 안되면 좌회전 적용

# 상어 이동 가능 위치 찾기
# 현재 상어 위치와 행렬 받아서 4칸 안에서 이동 가능한 칸의 좌표 배열로 반환

# dfs 완전탐색
# 행렬, 현재 상어 위치, 먹은 물고기 합계 받음
# 행렬 딥카피, 물고기 먹음 처리(합계 증가, 상어 위치 물고기 번호 -1)
# 물고기 이동, 상어 이동 가능 위치 찾기
# 위치 없으면 결과값 최대값으로 갱신
# 위치 있으면 각 위치에 dfs 적용

array = [[None] * 4 for _ in range(4)]
for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        array[i][j] = [data[j*2], data[j*2+1]-1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]


def turn_left(direction):
    return (direction+1) % 8


result = 0


def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i, j)
    return None


def move_all_fish(array, shark_y, shark_x):
    for i in range(1, 17):
        position = find_fish(array, i)
        if position != None:
            y, x = position[0], position[1]
            direction = array[y][x][1]
            for j in range(8):
                nx = x+dx[direction]
                ny = y+dy[direction]
                if 0 <= nx < 4 and 0 <= ny < 4:
                    if not (nx == shark_x and ny == shark_y):
                        array[y][x][1] = direction
                        array[y][x], array[ny][nx] = array[ny][nx], array[y][x]
                        break
                direction = turn_left(direction)


def get_possible_positions(array, cy, cx):
    positions = []
    direction = array[cy][cx][1]
    for i in range(4):
        cx += dx[direction]
        cy += dy[direction]
        if 0 <= cy < 4 and 0 <= cx < 4:
            if array[cy][cx][0] != -1:
                positions.append((cy, cx))
    return positions


def dfs(array, y, x, total):
    global result
    array = copy.deepcopy(array)  # 왜 복제?
    total += array[y][x][0]
    array[y][x][0] = -1
    move_all_fish(array, y, x)

    positions = get_possible_positions(array, y, x)
    if len(positions) == 0:
        result = max(result, total)
        return
    for ny, nx in positions:
        dfs(array, ny, nx, total)


dfs(array, 0, 0, 0)
print(result)
