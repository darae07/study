# 행렬 무한으로 초기화
# 자기 자신으로 = 0
# 경로마다 최소값으로 적용
# 플로이드 알고리즘 matrix[a][b] = min(matrix[a][b], matrix[a][k]+matrix[k][b])

n = int(input())
m = int(input())

matrix = [[1e7]*n for _ in range(n)]
for i in range(n):
    matrix[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    if matrix[a-1][b-1] > c:
        matrix[a-1][b-1] = c

for k in range(n):
    for a in range(n):
        for b in range(n):
            matrix[a][b] = min(matrix[a][b], matrix[a][k]+matrix[k][b])

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1e7:
            print(0, end=' ')
        else:
            print(matrix[i][j], end=' ')
    print()
