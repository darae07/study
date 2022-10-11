# n개의 여행지
# 여행지 서로 연결되어 있으면 양방향 이동이 가능
# 서로소 집합: union, find
# union = 루트를 찾고, 값이 큰 노드의 부모를 작은 노드로 설정
# find = 루트 노드가 아니라면 루트를 찾을때까지 재귀적으로 호출

# 부모를 찾고 DP저장
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    # 값이 큰 노드의 부모를 작은 노드로 설정
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(graph, path):
    n = len(graph)
    m = len(path)
    parent = [0]*(n+1)
    # 부모를 자신으로 설정
    for i in range(1, n+1):
        parent[i] = i

    # 연결 존재하면 union연산 수행
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                union(parent, i+1, j+1)

    result = True
    # 다른 집합이면 여행 불가
    for i in range(m-1):
        if find(parent, path[i]) != find(parent, path[i+1]):
            result = False
    return result


print(solution([[0, 1, 0, 1, 1, ], [1, 0, 1, 1, 0], [0, 1, 0, 0, 0],
      [1, 1, 0, 0, 0], [1, 0, 0, 0, 0]], [2, 3, 4, 3]))
