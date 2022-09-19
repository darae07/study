# -*- coding:utf-8 -*-
# 알파벳과 숫자 문자열 입력
# 알파벳 오름차순 + 숫자 더한 값 출력
def solution(s):
    alpha = []
    number = 0
    for char in s:
        if char.isdigit():
            number += int(char)
        else:
            alpha.append(char)
    alpha.sort()
    if number > 0:
        alpha.append(str(number))
    return ''.join(alpha)


print(solution('K1KA5CB7'))
