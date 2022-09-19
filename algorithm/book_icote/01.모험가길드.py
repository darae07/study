# -*- coding:utf-8 -*-
# n명의 모험가
# 공포도 배열
# 공포도 x이면 x이상 인원으로 구성할때 그룹 수의 최대값
def count_group(n, fear_list):
    fear_list.sort()
    member_count = 0
    group_count = 0
    for i in range(len(fear_list)):
        member_count += 1
        if fear_list[i] <= member_count:
            group_count += 1
            member_count = 0
    return group_count


a = count_group(5, [2, 3, 1, 2, 2])
print(a)
