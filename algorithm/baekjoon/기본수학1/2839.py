# 1. 시간초과
# 정확하게 n 킬로그램 -> 안되면 -1
# 봉지 3, 5짜리
# 최대한 적은 봉지 소모, 필요 봉지 갯수 출력
# n<=5a+3b => 같으면 a+b, n이 작으면 -1
# 최소힙 -> (갯수, 잔여n) 추가
# 힙이 비어있지 않으면 하나씩 꺼내기 -> 잔여 0이면 갯수 반환
# 3,5 감산 연산 하고 튜플 힙에 없으면 힙에 넣음
# 연산후 힙 빌때까지 값 못찾으면 -1 반환
import heapq
n = int(input())
heap = []
heapq.heappush(heap, (0, n))
while len(heap) > 0:
    (count, remain_k) = heapq.heappop(heap)
    if remain_k == 0:
        print(count)
        break
    if remain_k >= 3:
        item = (count+1, remain_k-3)
        if item not in heap:
            heapq.heappush(heap, item)
    if remain_k >= 5:
        item = (count+1, remain_k-5)
        if item not in heap:
            heapq.heappush(heap, item)
print(-1)


# n을 5의 배수가 될때까지 3씩 빼주고, 5의 배수가 되면 몫을 더해 값을 구한다.
# 3,5로 떨어지지 않을 경우 -1을 리턴
n = int(input())
count = 0
while n >= 0:
    if n % 5 == 0:
        count += (n//5)
        print(count)
        break
    n -= 3
    count += 1
else:
    print(-1)
