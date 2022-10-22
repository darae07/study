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

group_count = 0
member_count = 0
for j in range(len(fear)):
    member_count += 1
    if fear[j] <= member_count:  # 지금까지 누적된 인원이 필요 인원보다 많거나 같으면
        group_count += 1
        member_count = 0
print(group_count)
