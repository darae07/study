# 레벨, 레벨 범위
# n이 현재 레벨 범위보다 작거나 같을 때까지
# 현재 레벨 범위+=레벨*6, 레벨+=1
# 반복 종료 후 레벨 출력
n = int(input())
level = 1
level_range = 1
while n > level_range:
    level_range += 6*level
    level += 1
print(level)
