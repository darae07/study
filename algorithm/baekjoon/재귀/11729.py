# 하노이의 탑
# 1<= n <= 20
# 출력: 1. 옮긴 횟수
# 2. from, to

bars = int(input())
count = [0]
result = []


def hanoi(fr, to, other, n):
    global count
    if n == 0:
        return
    hanoi(fr, other, to, n-1)
    count[0] += 1
    result.append((fr, to))
    hanoi(other, to, fr, n-1)


hanoi(1, 3, 2, bars)
print(count[0])
for (fr, to) in result:
    print(f'{fr} {to}')
