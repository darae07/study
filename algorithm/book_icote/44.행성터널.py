# 신장 트리
# 크루스칼 알고리즘
# 행성= 3차원 좌표위의 점
# 행성 거리 min(|x1-x2|,|y1-y2|,|z1-z2|)
# 터널 n-1개

# 거리가 x,y,z좌표 거리 비교후 최소값 취하면 됨
# -> 도시별 x,y,z 좌표 축별로 각각 모으고 정렬 -> 각 축에 대한 도시 i, i+1번째를 비교하면
# 해당 도시의 축에 대한 최소 거리를 얻을 수 있음
# -> 이를 모아 정렬하면 항상 두 도시에 대한 최소 거리를 얻을 수 있음
# 두 도시간 최소 거리일때(합집합 연산 수행시) 거리 합산

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, cities):
    parent = [i for i in range(n)]
    result = 0
    x = [(cities[i][0], i) for i in range(n)]
    y = [(cities[i][1], i) for i in range(n)]
    z = [(cities[i][2], i) for i in range(n)]

    x.sort()
    y.sort()
    z.sort()

    edges = []
    for i in range(n-1):
        edges.append((x[i+1][0]-x[i][0], x[i][1], x[i+1][1]))
        edges.append((y[i+1][0]-y[i][0], y[i][1], y[i+1][1]))
        edges.append((z[i+1][0]-z[i][0], z[i][1], z[i+1][1]))

    edges.sort()
    for edge in edges:
        cost, a, b = edge
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            result += cost

    return result


n = int(input())
citeis = []
for _ in range(n):
    citeis.append(list(map(int, input().split())))

print(solution(n, citeis))
