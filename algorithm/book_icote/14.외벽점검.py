# -*- coding:utf-8 -*-
# n= 외벽의 길이 1<n<=200
# weak= 취약 지점의 위치 1<len(weak)<=15
# dist= 각 친구가 1시간동안 이동할수 있는 거리 1<len(dist)<=8
# 출력: 필요 친구 최소 수. 불가능한 경우 -1

# dist 모든 조합-> 점검 가능한지 체크 -> 조합 길이 최소값으로 업데이트
# 점검: 1시간.
# 방향- 시계/반시계
# 출발점- 무관
# 원형 데이터는 길이를 2배로 늘려 일자 형태로 만들면 유리하다
from itertools import permutations


def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    answer = len(dist)+1

    # 가능한 모든 출발점 검사
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1
            # 해당 친구가 점검할수 있는 마지막 위치
            position = weak[start]+friends[count-1]
            # 시작점부터 모든 취약 지점 확인
            for index in range(start, start+length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break  # 하나의 반복문 빠져나옴
                    position = weak[index] + friends[count-1]
            answer = min(answer, count)

    if answer > len(dist):
        return -1
    return answer
