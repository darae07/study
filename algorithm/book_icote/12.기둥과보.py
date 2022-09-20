# -*- coding:utf-8 -*-
# 입력 [x,y,a,b] 좌표, 종류, 작업
# 출력 [x,y,a]
# 입력값 길이 <1000 -> n**2(2초), n**3(5초)
# 작업 수행할 때마다 유효한 작업인지 확인
# -> 먼저 작업을 수행하고, 결과 배열이 유효하지 않으면 되돌리기
# 유효한지 확인: 정답 배열 반복하면서 모든 값이 유효한지 확인
# 요소가 기둥이면: 바닥인지, 보의 끝인지, 다른 기둥이 아래 있는지
# 요소가 보면: 아래에 기둥이 있는지, 양옆에 보가 있는지
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:  # 기둥
            # 바닥/보 위에/기둥 위에
            if y == 0 or \
                [x-1, y, 1] in answer or [x, y, 1] in answer or \
                    [x, y-1, 0] in answer:
                continue
            return False
        elif stuff == 1:  # 보
            # 아래 기둥/옆에 보
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer \
                    or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0:
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        if operate == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
    return sorted(answer)


a = solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [
             5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]])
print(a)
