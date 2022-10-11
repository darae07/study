# n개의 집(0, n-1), m개의 도로
# 모든 도로에는 가로등 존재, 도로 가로등 하루동안 켜기 위한 비용 = 도로의 길이
# 예시: 2,3번 집 연결 길이 7 = 비용 7
# 일부 가로등을 비활성화하여 절약할 수 있는 최대 금액
# 가로등 비활성화 해도 모든 집이 통행 가능해야함
# 모든 집이 하나의 집합으로 연결되어야 함
# 도로정보 (x,y,z) = (집1, 집2, 거리)
# 도로 탐색하면서 이미 같은 집합이면 절감 가능한 비용에 추가
# 아니면 union 연산
# 도로 정보를 비용 기준 오름차순 정렬


# 맞았지만 체크 포인트 = 신장 트리, 크루스칼 알고리즘
# -> 간선에 오름차순 정렬 수행후, 비용 낮은 순서대로 집합에 포함시킨다(그리디)

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


def solution(n, loads):
    house = [i for i in range(n)]
    result = 0

    loads.sort(key=lambda s: s[2])
    for load in loads:
        x, y, z = load[0], load[1], load[2]

        x = find(house, x)
        y = find(house, y)
        if x == y:
            result += z
        else:
            union(house, x, y)
    return result


print(solution(7, [[0, 1, 7], [0, 3, 5], [1, 2, 8],
      [1, 3, 9], [1, 4, 7], [2, 4, 5], [3, 4, 15], [3, 5, 6],
      [4, 5, 8], [4, 6, 9], [5, 6, 11]]))
