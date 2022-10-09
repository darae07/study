# 학생 수, 비교 횟수
# 두 학생 성적 비교 (a,b) = (a<b)
# 순위를 알수 있다 = 모든 노드와 연결되어 있다.
# 플로이드 알고리즘으로 모든 최단거리 계산,
# 연결 횟수가 n이면 순위 알수 있는 학생이라고 판단
# 연결 횟수가 n인 학생의 수

def solution(n, compare):
    graph = [[1e7]*n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0

    for a, b in compare:
        graph[a-1][b-1] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

    result = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if graph[i][j] != 1e7 or graph[j][i] != 1e7:
                count += 1
        if count == n:
            result += 1

    return (result)


print(solution(6, [(1, 5), (3, 4), (4, 2), (4, 6), (5, 2), (5, 4)]))
