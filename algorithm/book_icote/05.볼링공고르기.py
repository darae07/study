# -*- coding:utf-8 -*-
# a,b 두사람
# n개의 볼링공. 각각 무게 적혀있음. 공번호 1번부터 부여
# 같은 무게의 여러 공 다른 공으로 간주
# 볼링공 무게 1-M까지 자연수
import time


def solution(n, m, balls):
    count = 0
    for i in range(len(balls)):
        for j in range(i+1, len(balls)):
            if balls[i] != balls[j]:
                count += 1
    return count


start = time.time()
print(solution(8, 5, [1, 5, 4, 3, 2, 4, 5, 2]))
print('time:', time.time()-start)


# 2. 무게별 공 개수 구하고, 무게가 작은 공부터 a가 공 하나를 선택했을때
# b가 고를수 있는 공의 개수를 구함
# 조합이므로 a,b 순서만 바뀐 쌍은 고려하지 않음
def answer(n, m, balls):
    weights = [0 for _ in range(m+1)]
    for ball in balls:
        weights[ball] += 1

    combination = 0
    for i in range(1, m):
        for j in range(i+1, m+1):
            combination += weights[i]*weights[j]
    return combination


b = answer(8, 5, [1, 5, 4, 3, 2, 4, 5, 2])
print(b)
