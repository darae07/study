# n*n(2<=n<=20) 공간 물고기 m마리 아기상어 1마리
# 최초 아기상어 크기 = 2, 1초에 상하좌우 인접 한칸씩 이동
# 아기상어는 자신보다 큰 물고기가 있는 칸은 지나갈 수 없다.
# 크기가 작으면 먹을수 있고, 같으면 지나갈수 있음
# 더이상 먹을수 있는 물고기 없으면 종료
# 먹을수 있는 물고기 1마리 -> 먹으러 감
# 2마리 이상 -> 가장 가까운 물고기 먹으러 감
# 거리 = 지나가야 하는 칸의 개수의 최소값
# 가까운 물고기 많다면 위, 왼쪽 순서로 먹음
# 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을때마다 크기가 1 증가한다.
# 0: 빈칸
# 1-6: 칸에 있는 물고기 크기
# 9: 아기 상어의 위치
# 상어 위치를 넣으면 bfs 반복하는 탐색 함수
# 상하좌우 좌표 유효하고 방문 전이면 큐에 담음
# (y,x),dist
# 큐 있는 동안 꺼내며 물고기 먹으면 시간 합산, 상어 크기 합산, 상어 위치 업데이트 후 종료,
# 아니면 상하좌우 다시 큐에 담음
# 큐 비면 시간 반환
# 오답
from collections import deque
from re import L

n = int(input())
matrix = []
x, y = 0, 0
for i in range(n):
    matrix.append(list(map(int, input().split())))
    for j in range(n):
        if matrix[i][j] == 9:
            x = j
            y = i
            matrix[i][j] = 0
time = 0
size = 2
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
while False:
    queue = deque([((y, x), 0)])
    visited = set()
    while queue:
        (cy, cx), dist = queue.popleft()
        if 0 < matrix[cy][cx] < size:
            size += matrix[cy][cx]
            matrix[cy][cx] = 0
            time += dist
            x, y = cx, cy
            break
        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]
            if 0 <= nx < n and 0 <= ny < n and matrix[ny][nx] <= size and (ny, nx) not in visited:
                queue.append(((ny, nx), dist+1))
                visited.add((ny, nx))
    if len(queue) == 0:
        print(time)
        break


# 정답
# 현재 위치부터 모든 위치까지 최단 거리 구하기
# 먹을 물고기 찾기

INF = 1e9
ate = 0


def dist_matrix():
    dist = [[-1]*n for _ in range(n)]
    queue = deque([(y, x)])
    dist[y][x] = 0
    while queue:
        cy, cx = queue.popleft()
        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if dist[ny][nx] == -1 and matrix[ny][nx] <= size:
                    dist[ny][nx] = dist[cy][cx]+1
                    queue.append((ny, nx))
    return dist


def find(dist):
    cy, cx = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= matrix[i][j] < size:
                if dist[i][j] < min_dist:
                    cy, cx = i, j
                    min_dist = dist[i][j]
    if min_dist == INF:
        return None
    else:
        return cy, cx, min_dist


while True:
    value = find(dist_matrix())
    if value == None:
        print(time)
        break
    y, x = value[0], value[1]
    time += value[2]
    matrix[y][x] = 0
    ate += 1
    if ate >= size:
        size += 1
        ate = 0
