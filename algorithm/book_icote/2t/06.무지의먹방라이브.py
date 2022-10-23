# n개의 음식 (1-n까지 번호)
# 음식 먹는데 필요한 시간 담긴 배열 food_times
# 네트워크 장애 발생한 시간 k
# 음식은 1번 음식부터 먹기 시작하여, 번호 증가 순서대로 음식 1초간 먹고
# 다음음식으로 넘어감 - 남은 음식중 가장 가까운 다음 번호
# 음식 먹는 시간 소요되면 해당 음식은 빠짐
# 3초간 먹는 음식이라면, 3*길이 초 후에 해당 음식 삭제
# 음식 빠지는 순서는 가장 시간 적게 걸리는 순서
# 우선순위 큐 - 적게 걸리는 음식부터 제거
# 제거 - 음식 시간*남은음식개수 <= k
# 제거시 k-남은음식개수*음식시간
# 반복 종료 후 남은 음식 중에서 나머지 인덱스 구함
# 인덱스기 때문에 마지막먹은 음식+1번째 음식 구해짐 -> 정답
# 더 섭취할 음식 없다면 -1

import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    remain = len(food_times)
    prev = 0  # 이전 cycle 빼기 위한 변수
    while (q[0][0]-prev)*remain <= k:
        cycle = heapq.heappop(q)[0]
        # 현재 시간에서 이전 cycle 만큼은 이미 빠져있기 때문에 이전보다 초과된 부분만 빼주어야 함
        k -= remain*(cycle-prev)
        remain -= 1
        prev = cycle
    q.sort(key=lambda x: x[1])
    return q[k % remain][1]


print(solution([3, 1, 2], 5))
