# n,m = 카드 갯수, 목표 합계
# 카드 입력
# 뽑을 카드가 3장이므로 n**3해도 십만
# bfs + 최적화 -> 최적화 과정에서 모든 케이스 고려 못해 오답이 됨
# 모든 경우 탐색해야 한다는 점에서 결국 조합 문제
# 조합 직접 구현시 시간 초과 나는 이유

from itertools import combinations
n, m = map(int, input().split())
cards = list(map(int, input().split()))


def get_total_combination(remain, total, k):
    result = []
    if k == 0:
        result.append(total)
    for i, v in enumerate(remain):
        result += get_total_combination(remain[i+1:], total+v, k-1)
    return result


combination = combinations(cards, 3)
value = 0
for comb in combination:
    v = sum(comb)
    if value < v and v <= m:
        value = v
print(value)
