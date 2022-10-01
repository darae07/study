# -*- coding:utf-8 -*-
# n개의 숫자
# n 목록
# 연산자 개수 [+-*//]
# 연산자 배열 -> 모든 경우 순열
# 숫자, 연산자 배열 -> 순차적으로 연산
# 시간초과
from itertools import product
n = int(input())
numbers = list(map(int, input().split()))
opers = []
oper_input = list(map(int, input().split()))
for i in range(4):
    opers += [i]*oper_input[i]


def calc(a, b, i):
    if i == 0:
        return a+b
    elif i == 1:
        return a-b
    elif i == 2:
        return a*b
    else:
        return a//b


min_value = 1e7
max_value = 0
perms = list(product(opers, repeat=n-1))

for i in range(len(perms)):
    temp = numbers[0]
    for j in range(n-1):
        temp = calc(temp, numbers[j+1], perms[i][j])
    min_value = min(min_value, temp)
    max_value = max(max_value, temp)
print(max_value)
print(min_value)

# 정답
# dfs를 통한 재귀적 중복 순열 계산
# 백트래킹 -> 조건을 만족하는 경우만 계산
n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div,  = map(int, input().split())

min_value = 1e9
max_value = -1e9


def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, now+numbers[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now-numbers[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now*numbers[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now/numbers[i]))
            div += 1


dfs(1, numbers[0])
print(max_value)
print(min_value)
