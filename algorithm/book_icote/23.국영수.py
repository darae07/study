# -*- coding:utf-8 -*-
# 국어 내림차순
# 영어 오름차순
# 수학 내림차순
# 이름 오름차순
n = int(input())
students = []
for _ in range(n):
    students.append(input().split())

students.sort(key=lambda s: (-int(s[1]), int(s[2]), -int(s[3]), s[0]))

for s in students:
    print(s[0])
