# -*- coding:utf-8 -*-
# 가장 쉬운 풀이법 = k를 반복하면서 food_times 감산
# 시간초과, 런타임에러
import heapq


def solution(food_times, k):
    food_index = 0
    for i in range(k):
        while food_times[food_index] == 0:
            food_index += 1
        food_times[food_index] -= 1
        food_index = (food_index+1) % len(food_times)
    return food_index+1

# 2. 정답
# 시간이 적게 걸리는 음식부터 확인하는 그리디 문제
# 우선순위 큐를 이용헤 시간이 적게 걸리는 음식부터 제거해나간다.
# 음식 (시간, 번호) 튜플로 우선순위 큐에 삽입
# 잔여 음식 개수(큐 길이)*꺼낼 요소 잔여 시간보다 k가 크면 꺼내고 k 감산
# 루프 종료 후 남은 요소 인덱스 기준으로 정렬후 인덱스 반환


def answer(food_times, k):
    if sum(food_times) <= k:
        return -1
    heap = []
    for i in range(len(food_times)):
        heapq.heappush(heap, (food_times[i], i+1))

    sum_value = 0
    cycle = 0
    food_length = len(food_times)

    while sum_value+((heap[0][0]-cycle)*food_length) <= k:
        now = heapq.heappop(heap)[0]
        sum_value += (now-cycle)*food_length
        food_length -= 1
        cycle = now
    result = sorted(heap, key=lambda x: x[1])
    return result[(k-sum_value) % food_length][1]
