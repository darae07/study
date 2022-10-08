# 1. 오답
# 2일차부터 갱신 -> 오늘 완료될수 있는 상담중에 최대값으로 갱신
# 오늘 완료될수 있는 상담 = 오늘 i >= 상담시작 인덱스+시간
# 오늘 최대 이익 = 최대값-전날 이익, 오늘 발생 이익

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dp = [0]*n
for i in range(1, n):
    earn = [data[j][1] for j in range(n) if i >= data[j][0]+j]
    value = 0
    if earn:
        value = max(earn)
    dp[i] = dp[i-1] + value
print(dp)
print(dp[n-1])


# 2. 정답
# 오늘 상담을 진행할경우 최대 이익 = 오늘 상담 이익 + 오늘 상담 종료 후 낼수 있는 최대 이익
# 오늘 상담 종료후 낼수 있는 최대 이익은 뒤로 갈수록 적어짐
# -> 맨뒤가 최소이므로 dp를 마지막 날짜부터 업데이트
# 점화식 dp[i] = i번째 날부터 마지막 날까지 낼 수 있는 최대 이익
# dp[i] => t[i]+i가 성립 즉, n보다 작거나 같을때,
# dp[i] = max(p[i]+dp[t[i]+i], max_value)

n = int(input())
t = []
p = []
dp = [0]*(n+1)
max_value = 0
for _ in range(n):
    time, pay = map(int, input().split())
    t.append(time)
    p.append(pay)

for i in range(n-1, -1, -1):
    time = t[i]+i
    if time <= n:
        dp[i] = max(p[i]+dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value


print(max_value)
