# 병사 전투력 내림차순 배치
# 가장 긴 오름차순 수열 문제로 변환(배열 뒤집기)
# 가장 긴 증가하는 부분 수열 - 전형적인 dp 문제
# dp[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
# dp = 1로 초기화(자신만 포함하는 길이)
# 점화식 -> 현재 값을 추가할수 있는 경우, 이전까지 길이+1 = dp[j]+1중의 최대값
# 점화식 0<=j<i, dp[i] = max(dp[i], dp[j]+1) if array[j]<array[i])


n = int(input())
dp = [1]*n
persons = list(map(int, input().split()))
persons.reverse()

for i in range(1, n):
    for j in range(0, i):
        if persons[j] < persons[i]:
            dp[i] = max(dp[i], dp[j]+1)
    # 똑같은 표현
    dp[i] = max([dp[j]+1 for j in range(0, i) if persons[j] < persons[i]]
                + [dp[i]])

print(n-max(dp))
