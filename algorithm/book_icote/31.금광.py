# 큐-> 이동 가능한 좌표 추가
# ((좌표y,x),(합계, 횟수))
# m이 행렬의 열 길이 => 답은 마지막 열 중에 있음
# 첫번째 열 초기화, 두번째 열부터 가능한 선택지 중 최적의 선택지로 업데이트 해나감
# 마지막 열 중 최대값 = 정답
from collections import deque


def solution(matrix):
    queue = deque()
    m = len(matrix[0])
    for i in range(len(matrix)):
        queue.append(((i, 0), (matrix[i][0], 1)))
    result = 0
    while queue:
        (y, x), (s, c) = queue.popleft()
        if c == m:
            result = max(result, s)
        if c < m:
            for i in range(-1, 2):
                nx = x+1
                ny = y+i
                if 0 <= nx < len(matrix[0]) and 0 <= ny < len(matrix):
                    queue.append(((ny, nx), (s+matrix[ny][nx], c+1)))
    return result

# dp[i][j] = dp[i][j]+max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])


def solutionDP(matrix):
    m = len(matrix[0])
    n = len(matrix)
    for j in range(1, m):
        for i in range(n):
            px = j-1
            value = 0
            for y in range(-1, 2):
                py = i+y
                if 0 <= py < n:
                    value = max(matrix[py][px], value)
            matrix[i][j] += value
    result = 0
    for i in range(n):
        result = max(result, matrix[i][m-1])

    return result


print(solutionDP([[1, 3, 1, 5], [2, 2, 4, 1], [5, 0, 2, 3], [0, 6, 1, 2]]))
