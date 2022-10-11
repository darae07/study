# 공항에는 g개의 탑승구. 1-g번까지
# p개의 비행기 탑승구 중 한곳에 도킹, 비어있어야함
# 도킹할 수 없는 비행기 나오면 운행 종료
# 최대 몇대의 비행기 도킹할수 있는지

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


def solution(g, airplanes):
    parent = [0]*(g+1)
    for i in range(1, g+1):
        parent[i] = i

    result = 0
    for to in airplanes:
        to = find(parent, to)
        if to == 0:  # 집합의 루트가 0 == 해당 집합에 도킹 가능한 탑승구가 없음
            return result
        union(parent, to, to-1)
        result += 1


print(solution(4, [4, 1, 1]))
