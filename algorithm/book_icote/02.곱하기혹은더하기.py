# -*- coding:utf-8 -*-
# 각 자리가 숫자로만 이루어진 문자열 s
# 숫자 사이에 +혹은*기호만 가능. 가장 큰 수를 구하기
# 연산은 왼쪽에서부터 순차적으로 이루어진다고 가정


def solution(s):
    numbers = [int(n) for n in list(s)]
    result = 0
    for n in numbers:
        if n <= 1 or result <= 1:
            result += n
        else:
            result *= n
    return result


a = solution('02984')
print(a)
