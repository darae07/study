# n 볼링공 개수, m 볼링공의 무게 범위 (1-m)
# balls = 공 무게 목록, 인덱스+1 = 공 번호
# a,b 두 사람이 서로 무게가 다른 볼링공을 골라야함
# 가능한 조합 개수
# balls 정렬
# 마지막-1공까지 반복하면서 현재 공과 무게 같은 공 우측 인덱스 구함
# n-우측인덱스-1씩 계속 더함
from bisect import bisect_right


n, m = map(int, input().split())
balls = list(map(int, input().split()))
balls.sort()
comb = 0
for ball in balls:
    i = bisect_right(balls, ball)
    comb += (n-i)

print(comb)


# 2. 무게를 통한 접근
# 무게별 공 갯수 구하고, 공 하나 선택할 때마다 선택 가능한 공 갯수를 줄여나가기
# 각 무게별 선택 가능한 공 갯수 = 전체 공 - 현재 무게 공 갯수
# 무게별 공 개수 * 선택 가능한 공 개수

answer = 0
weights = [0]*(m+1)
for ball in balls:
    weights[ball] += 1

for i in range(m):
    n -= weights[i]
    answer += weights[i]*n
print(answer)
