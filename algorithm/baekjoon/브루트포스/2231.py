# 분해합 = 각 자리수의 합
# 생성자 m = 분해합 n. 분해합 주어졌을때 생성자 구하고, 없으면 0 출력
# 생성자 = n+n의 각 자리수 합
import math
n = int(input())
m = n
for num in range(n, 0, -1):
    total = sum([int(v) for v in list(str(num))])+num
    if total == n:
        m = min(m, num)
    if total < n-(len(str(n))-1)*9:
        break
print(m if m < n else 0)
