# 문자열 a, b
# a를 편집하여 b로 변환
# 세가지 연산중 한번에 하나 선택 가능
# 1. 삽입: 하나의 문자 삽입
# 2. 삭제: 하나의 문자 삭제
# 3. 교체: 하나의 문자 교체
# 편집 거리 = 연산의 수
# 최소 편집 거리 계산
# 점화식
# 행과 열에 해당하는 문자가 서로 같다면 왼쪽 위에 해당하는 수를 삽입
# 서로 다르다면 행기준 삽입(왼쪽), 삭제(위쪽), 교체(왼쪽위) 중 최소값 +1
# 점화식 최소값 = 빈 문자열에서 연산 =>0행과 0열 - 각각 인덱스+1만큼 연산 필요

def solution(a, b):
    m = len(b)
    n = len(a)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][0] = i
    for j in range(1, m+1):
        dp[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1+min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
    return dp[n][m]
