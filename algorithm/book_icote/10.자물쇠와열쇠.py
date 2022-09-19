# -*- coding:utf-8 -*-
# 어려움
# 자물쇠 격자 n*n
# 열쇠 m*m -> 회전, 이동 -> 자물쇠 홈 다 채워야함
# 0은 홈, 1은 돌기
# 열수 있는지 여부
# 먼저 회전이 필요한지 체크
# 이동 체크
# 입력값이 20이하이므로, 모든 원소에 접근시 400
# 1초에 2천만 가능하므로 열쇠를 이동시켜 모든 경우의 수 구하는 접근 방법 시도할수 있다.
# 자물쇠를 3배로 키우고, 자물쇠 패턴 중앙에 위치
# 열쇠 돌리는 함수
# 자물쇠 중앙이 모두 1인지 확인하는 함수

# 열쇠 돌리는 함수
def rotate_matrix_90(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = matrix[i][j]
    return result

# 자물쇠 중앙이 모두 1인지 확인


def check(new_lock):
    lock_len = len(new_lock) // 3
    for i in range(lock_len, lock_len*2):
        for j in range(lock_len, lock_len*2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠 3배, 중앙에 위치
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    # 4방향 열쇠 회전
    for rotation in range(4):
        key = rotate_matrix_90(key)
        # 자물쇠 좌표 이동
        for x in range(1, n*2):
            for y in range(1, n*2):
                # 열쇠 끼우기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock) == True:
                    return True
                # 열쇠 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False
