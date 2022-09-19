# -*- coding:utf-8 -*-
# 0,1로만 이뤄진 문자열 s
# 연속된 하나 이상의 숫자를 잡고 모두 반대로 뒤집기(0->1 or 1->0)
# 모두 같게 만드는 최소 행동의 횟수

def solution(s):
    group0 = 0
    group1 = 0
    prev = ''
    for char in s:
        if char != prev:
            if char == '0':
                group0 += 1
            elif char == '1':
                group1 += 1
            prev = char
    return min(group0, group1)


print(solution('00101100'))
