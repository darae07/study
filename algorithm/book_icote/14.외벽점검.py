# -*- coding:utf-8 -*-
# n= 외벽의 길이 1<n<=200
# week= 취약 지점의 위치 1<len(week)<=15
# dist= 각 친구가 1시간동안 이동할수 있는 거리 1<len(dist)<=8
# 입력 작기 때문에 모든 친구 나열하는 순열
# 출력: 필요 친구 최소 수. 불가능한 경우 -1

# dist 모든 조합-> 점검 가능한지 체크 -> 조합 길이 최소값으로 업데이트
# 점검: 1시간.
# 방향- 시계/반시계
# 출발점- 무관
# 원형 데이터는 길이를 2배로 늘려 일자 형태로 만들면 유리하다
# w^2*d! -> n^2이 아닌 취약점만 검사하도록 구현

# 반복1. 출발점 무관 -> 모든 출발점에 대해 검사. 모든 위치 반복문
# 반복2. 친구 투입 수-> 모든 친구 투입 순서 - 친구 나열 순열
# 친구 1명부터 투입-> 이동 가능한 위치 계산
# 반복3. 모든 취약점 가능한지 검사 -> 취약점 출발점-한바퀴까지 검사
# 친구수 별도 변수로
# 현재 친구수로 검사 가능한 위치 계산
# 친구가 갈수있는 위치 < 이동 가능한 위치 -> 친구 +=1
# 친구 늘린후 마지막 위치 갱신
# 반복 종료후 정답 갱신(모든 순열에 대해 갱신)
from itertools import permutations


def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)

    friends_sequence = list(permutations(dist, len(dist)))
    answer = len(dist)+1
    for start in range(length):
        for friends in friends_sequence:
            count = 1
            position = weak[start]+friends[count-1]

            for goal in range(start, start+length):
                if position < weak[goal]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[goal]+friends[count-1]
            answer = min(answer, count)

    if answer > len(dist):
        return -1
    return answer
