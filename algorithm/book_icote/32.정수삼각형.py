# 왼쪽 대각선 혹은 오른쪽 대각선 - 인덱스 -1 또는 +0

n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(dp[i])):
        value = 0
        for k in range(-1, 1):
            px = j+k
            py = i-1
            if 0 <= px < len(dp[py]):
                value = max(value, dp[py][px])
        dp[i][j] += value
print(max(dp[n-1]))
