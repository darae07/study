# -*- coding:utf-8 -*-
# n개의 동전 -> 만들수 없는 최소의 금액
# coins = 화폐 단위로 이루어진 동전 배열. 단위와 갯수가 유한함
# 그리디 - 작은 값부터 순차적으로 더하면 target-1까지 만들수 있음
# 정당성 확보!
# 정당성 - target 1부터 코인 순차적으로 더하면 target-1까지 만들수 있는 금액

def solution(n, coins):
    coins.sort()
    target = 1
    for coin in coins:
        if target < coin:
            return target
        target += coin
    return target


print(solution(5, [3, 2, 1, 1, 9]))
