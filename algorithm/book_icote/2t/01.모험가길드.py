# 모험가 n명
# 공포도 목록
# 공포도 x인 모험가는 x명 이상으로 구성
# 그룹 수의 최대값
# 공포도 순으로 정렬, 최소 인원부터 그룹 구성

n = int(input())
fear = list(map(int, input().split()))
fear.sort()

i = 0
group_count = 0

while i < len(fear):
    i += fear[group_count]
    if i >= len(fear):
        break
    group_count += 1
print(group_count)
