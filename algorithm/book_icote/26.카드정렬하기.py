# -*- coding:utf-8 -*-
# 정렬해서 앞에서부터 2개씩 끊어서 계산 -> 두개씩 끊었을때 최소임을 보장할수 없음
# 우선순위 큐 -> 최소 두값 꺼내서 결과값에 더하고 더한값을 힙에 다시 넣기
# 힙에 요소가 하나일때까지

import heapq

n = int(input())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

result = 0

while len(cards) > 1:
    o = heapq.heappop(cards)
    t = heapq.heappop(cards)
    s = o+t
    result += s
    heapq.heappush(cards, s)

print(result)
