# 실패율= 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 도달한 플레이어의 수
# n 스테이지 개수, stages - 각 사용자가 멈춰있는 스테이지의 번호
# 실패율 높은 스테이지부터 내림차순으로 스테이지 번호가 담겨있는 배열 리턴
# 스테이지 정보 = [(실패율, 스테이지 번호)]
# stages 길이 = 사용자 수
# 도달한 플레이어의 수 = 스테이지 오름차순으로 탐색할때, 전체 사용자수 - 현재 스테이지에 진입하지 못한 사용자 수
# 현재 스테이지에 진입하지 못한 사용자 수 = 전체 사용자수 - 직전 스테이지까지 실패한 사용자 수
# -> (스테이지 탐색시마다 실패한 사용자 감산(로직 수행후 실시))

def solution(N, stages):
    answer = []
    persons = len(stages)
    for i in range(1, N+1):
        count = stages.count(i)
        if persons == 0:
            fail = 0
        else:
            fail = count/persons
        answer.append((fail, i))
        persons -= count
    answer.sort(key=lambda x: (-x[0], x[1]))
    return [x[1] for x in answer]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
