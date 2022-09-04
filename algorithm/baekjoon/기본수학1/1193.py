# 시간초과
# 행렬(y,x)
# 분수 형태 f'{y}/{x}'
# 입력 n -> n번 지그재그 이동 반복 -> x,y값 획득
# 지그재그 반복 규칙:
# y가 0이면 x+=1 => x--, y++, x==0까지
# x가 0이면 y=x+1, x=0 => x++, y--, y==0까지

n = 5
x, y = 0, 0
dirrection_up = True
for _ in range(1, n):
    if dirrection_up:
        if y == 0:
            dirrection_up = False
            x += 1
        else:
            x += 1
            y -= 1
    else:
        if x == 0:
            dirrection_up = True
            y += 1
        else:
            x -= 1
            y += 1

print(f'{y+1}/{x+1}')


# 수열
# 1, 3, 6, 10 ... 현재 레벨 = 직전레벨+높이
# n > 레벨동안 반복 - n에서 레벨만큼 빼주면서 레벨 구함
# 잔여 n = 해당 줄에서 몇번째 요소인지 -> 0<n<=레벨 (서수 인덱스)
# 레벨에서 분수 계산법 : 홀수레벨 => x=n, y=level-n+1
# 짝수레벨 => x=level-n+1, y=n
# f'{y}/{x}'
n = int(input())
level = 1
while n > level:
    n -= level
    level += 1
if level % 2 == 0:
    x = level-n+1
    y = n
else:
    x = n
    y = level-n+1
print(f'{y}/{x}')
