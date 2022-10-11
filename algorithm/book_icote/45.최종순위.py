# t = 테스트 케이스 수
# n = 팀의 수
# last_score = 작년 순위
# m = 등수가 서로 바뀐 쌍의 수
# 등수가 바뀐 정보
# 위상 정렬
# 노드 -> 자신보다 순위가 낮은 노드 가리키도록
# 각 노드별 진입차수 계산
# 순서 변경시 노드 방향 변경-> a,b -> last_score 인덱스순 정렬 -> 진입차수 a+1, b-1
# 큐에 진입차수 0인 노드 삽입
# 연산마다 큐 검사 - 위상정렬 유효한지 체크 - 비면 사이클 발생, 1개 이상이면 중복 가지 발생

# 노드간 연결 여부 조회해야함 -> 인접행렬 방식으로 간선 업데이트
# 동시에, 진입 차수 테이블에 업데이트
# 노드 개수 만큼 진입차수 0인 노드를 반복함
# 큐를 이용하여 반복할 노드를 저장
# 매 반복시 큐의 길이가 1이면 유효한 위상정렬
# 길이 > 1 : 여러 가지가 존재하는 그래프, 길이 = 0 : 사이클이 존재하는 그래프

from collections import deque

t = int(input())


def solution():
    n = int(input())
    last_score = list(map(int, input().split()))
    graph = [[False]*(n+1) for _ in range(n+1)]
    table = [0]*(n+1)
    for i in range(n):
        for j in range(i+1, n):
            graph[last_score[i]][last_score[j]] = True
            table[last_score[j]] += 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if graph[b][a]:
            a, b = b, a
        table[a] += 1
        table[b] -= 1
        graph[a][b] = False
        graph[b][a] = True

    queue = deque()
    for i in range(1, n+1):
        if table[i] == 0:
            queue.append(i)

    result = []
    for i in range(n):
        if len(queue) == 0:
            return 'IMPOSSIBLE'
        if len(queue) > 1:
            return '?'
        a = queue.popleft()
        result.append(a)
        for b in range(1, n+1):
            if graph[a][b]:
                table[b] -= 1
                if table[b] == 0:
                    queue.append(b)
    return ' '.join(str(s) for s in result)


for _ in range(t):
    print('answer: ', solution())
