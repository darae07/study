# n개의 동전
# n개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최소값을 구하라
# 동전 오름차순 정렬
# 동전 반복하면서 동전 누적 합계 구함
# 동전 합계 < 현재 동전이면 종료.
n = int(input())
coins = list(map(int, input().split()))
coins.sort()
answer = 1

for coin in coins:
    if answer < coin:
        break
    answer += coin

print(answer)
