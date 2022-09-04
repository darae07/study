
# 1. 시간초과
# a, b, v = 낮 이동가능 미터,밤 미끄러지는 미터,높이
# 정상에 올라간 후에는 미끄러지지 않는다.
# 모두 올라가는데 며칠 걸리는가? = days

import math
a, b, v = map(int, input().split())
position = 0
days = 0
while position < v:
    position += a
    days += 1
    if position > v:
        break
    position -= b
print(days)


# 2. 계산실수
# a, b, v = 낮 이동가능 미터,밤 미끄러지는 미터,높이
# 정상에 올라간 후에는 미끄러지지 않는다.
# 모두 올라가는데 며칠 걸리는가? = days
# 입력값이 크기 때문에 O(v)보다 최적화 필요
# (a-b)*days >= v-b
# days >= v-b // (a-b)
# b<a => a-b는 0이 될수 없음
a, b, v = map(int, input().split())
days = (v-b) // (a-b)
print(days)


# 3. 정답
# (a-b)*days >= v-b
# days >= v-b / (a-b)
# days는 정수여야 하므로 수식에 ceil 필요
# b<a => a-b는 0이 될수 없음
# 시간복잡도 O(1)
a, b, v = map(int, input().split())
days = math.ceil((v-b) / (a-b))
print(days)
