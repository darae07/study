# n*n 좌표
# m 상어 수 k 냄새 유효 시간
# 상어 이동 - 인접한 칸중 아무 냄새 없는 칸
# -> 자신의 냄새가 있는 칸
# - 순서 우선순위 = 상어의 현재 방향에 따라 다름
# 같은 칸으로 이동하게 된 상어는 번호가 작은 상어가 큰 상어를 쫒아낸다
# 1번 상어만 남을때까지 몇초 걸리는가
# 1000초가 넘어도 다른 상어 남아있으면 -1 출력
# 상어 이동 -> 행렬에 값 있으면,
# [1]값이 k보다 작으면 -1, 0되면 None 처리
# [1]값이 k = 상어 -> 현재 상어 방향 -> table에서 우선순위 찾아 이동 가능할때까지 반복
# 이동 가능 = 1. 빈칸 2. 향기 있는 칸
# 향기 k인 경우 -> 상어 -> 큰상어 없애기 -> 작은 상어인 경우 덮어쓰고, 큰상어인 경우 무시

n, m, k = map(int, input().split())
# matrix = (상어번호, 향 잔여 초)

matrix = [[] for _ in range(n)]
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        a = None if data[j] == 0 else [data[j], k]
        matrix[i].append(a)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 상어 번호 당 방향 정보
shark_d = [[]] + [int(x)-1 for x in input().split()]
d_table = [[]]
for _ in range(m):
    d = []  # 위아래옆 방향별 우선순위 정보
    for _ in range(4):
        d.append([int(x)-1 for x in input().split()])
    d_table.append(d)

time = 0
count = m
while time < 1000:
    time += 1
    visited = [False]*(m+1)
    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                s, sent = matrix[i][j]
                if sent == k and not visited[s]:  # 상어 이동
                    di = shark_d[s]
                    done = False
                    visited[s] = True
                    for d in d_table[s][di]:
                        ny = i+dy[d]
                        nx = j+dx[d]
                        if 0 <= ny < n and 0 <= nx < n and matrix[ny][nx] == None:
                            matrix[ny][nx] = [s, k]
                            matrix[i][j][1] -= 1
                            done = True
                            break
                    if not done:
                        for d in d_table[s][di]:
                            ny = i+dy[d]
                            nx = j+dx[d]
                            if 0 <= ny < n and 0 <= nx < n:
                                cs = matrix[ny][nx]
                                if cs[1] == k:  # 상어
                                    count -= 1
                                    if cs[0] > s:  # 현재 상어가 더 작으면
                                        matrix[ny][nx] = [s, k]

                                break
                elif matrix[i][j][1] < k:  # 향기 -1
                    matrix[i][j][1] -= 1
                if matrix[i][j][1] == 0:
                    matrix[i][j] = None
    if count == 0:
        print(time)
        break

if time == 1000:
    print(-1)

# 2. 정답
# 자료형
# 1. 상어 위치 행렬 array - [상어 번호]
# 2. 상어 방향 배열 directions - [방향]
# 3. 냄새 행렬 smell - [[상어 번호, 남은 시간]]
# 4. 회전 방향 우선 순위 priorities - [[방향 번호(1-4)]*4(상하좌우)]*m(상어 번호)
# == priorities[상어 번호][방향 번호][상하좌우 4가지]

# 냄새 업데이트
# - i,j 반복, 냄새 있으면 -1,
# 상어 있으면 냄새 k로 세팅

# 상어 이동
# 냄새 정보로 상어 이동함 -> 냄새 업데이트 후 상어 이동
# 이번 텀에 옮겨진 것들중 우선순위 따라 처리하기 위해서 신규 행렬 생성
# 상어 존재하면 상어 방향 획득
# 냄새 없는곳 부터 확인
# 상어 방향 4 안에서 반복하며 확인
# 냄새 없으면 처리: 해당 상어 방향 이동, 새 행렬에 다른 상어 없으면 넣기, 있으면 낮은 번호로 업데이트
# 모두 냄새 있다면 자신의 냄새 있는곳으로 이동
# 상어 방향 4안에서 반복하며 확인
# 냄새가 자신의 냄새이면 처리: 방향 업데이트, 새 행렬에 상어 넣기
# 새 상어 행렬 반환

# 반복문 돌며 냄새 업데이트, 상어 위치 업데이트
# 1보다 큰 상어 없으면 시간 출력하고 종료
# 시간이 1000넘으면 -1 출력하고 종료

n,  m, k = map(int, input().split())
# 상어 위치
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 모든 상어의 현재 방향 정보
directions = list(map(int, input().split()))
# [특정 냄새의 상어 번호, 남은 시간]
smell = [[[0, 0]] * n for _ in range(n)]
# 각 상어의 회전 방향 우선 순위 정보
priorities = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 모든 냄새 업데이트


def update_smell():
    for i in range(n):
        for j in range(n):
            # 냄새 있으면 -1
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            # 상어 있으면 냄새 k로
            if array[i][j] != 0:
                smell[i][j] = [array[i][j], k]


def move():
    # 상어 위치 담기 -> 이번 텀에 옮겨진것만 처리하기 위해서
    new_array = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            # 상어 존재하면
            if array[x][y] != 0:
                # 방향 = 현재 상어의 방향
                direction = directions[array[x][y]-1]
                found = False
                # 냄새없는곳 확인
                for index in range(4):
                    di = priorities[array[x][y]-1][direction-1][index]
                    nx = x+dx[di-1]
                    ny = y+dy[di-1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][1] == 0:
                            # 해당 상어의 방향 이동
                            directions[array[x][y]-1] = di
                            # 다른 상어 없으면 넣기
                            if new_array[nx][ny] == 0:
                                new_array[nx][ny] = array[x][y]
                            # 있으면 번호 낮은 상어 들어감
                            else:
                                new_array[nx][ny] = min(
                                    new_array[nx][ny], array[x][y])
                            found = True
                            break
                if found:
                    continue
                # 모두 냄새 있다면 자신의 냄새 있는곳으로 이동
                for index in range(4):
                    di = priorities[array[x][y]-1][direction-1][index]
                    nx = x+dx[di-1]
                    ny = y+dy[di-1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][0] == array[x][y]:
                            directions[array[x][y]-1] = di
                            new_array[nx][ny] = array[x][y]
                            break
    return new_array


time = 0
while True:
    # 상어 위치 기반 냄새 업데이트
    update_smell()
    # 상어 위치 구하고 업데이트
    new_array = move()
    array = new_array
    time += 1
    check = True
    for i in range(n):
        for j in range(n):
            if array[i][j] > 1:
                check = False
    if check:
        print(time)
        break
    if time >= 1000:
        print(-1)
        break
