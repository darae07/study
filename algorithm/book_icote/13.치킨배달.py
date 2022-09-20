# -*- coding:utf-8 -*-
# n*n 크기 도시 매트릭스 주어짐
# 요소 0-빈칸, 1-집, 2-치킨집
# 각 집은 치킨거리를 갖는다.  |r1-r2| + |c1-c2|
# 첫째 줄 n, m
# 가장 수익을 많이 낼수 있는 치킨집 최대 개수 m, 나머지 치킨집 폐업할때
# 도시의 치킨 거리 최소값
# m<=13 -> 13Cm은 100000을 넘지 않는다. 집의 개수 최대 100 -> 완전탐색

# 행렬 돌면서 집, 치킨집 배열에 추가
# 치킨집 m개만큼 조합
# 각 조합마다 도시치킨거리 구하기
# 모든 조합마다 치킨거리 확인하며 최소값으로 갱신
from itertools import combinations
n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c))
candidates = list(combinations(chicken, m))


def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx)+abs(hy-cy))
        result += temp
    return result


result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))
print(result)
