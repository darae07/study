# 1. 오답
# k = log 3 n
# 가운데 공백의 크기 3**(k-1) 정사각형
# 9개의 면으로 나눠서..
# k-1 k-1 k-1
# k-1 공백 k-1
# k-1 k-1 k-1
import math


def pattern(k):
    if k == 1:
        return ['***', '* *', '***']
    child_pattern = pattern(k-1)
    stars = []
    for i in child_pattern:
        stars.append(i*3)
    for i in child_pattern:
        stars.append(i+' '*3**(k-1)+i)
    for i in child_pattern:
        stars.append(i*3)
    return stars


n = int(input())
print('\n'.join(pattern(int(math.log(n, 3)))))

# 2. 정답


def pattern(k):
    if k == 3:
        return ['***', '* *', '***']
    child_pattern = pattern(k//3)
    stars = []
    for i in child_pattern:
        stars.append(i*3)
    for i in child_pattern:
        stars.append(i+' '*(k//3)+i)
    for i in child_pattern:
        stars.append(i*3)
    return stars


n = int(input())
print('\n'.join(pattern(n)))
