# 0, 1 끊어질때마다 그룹 나눔
# 두 그룹 갯수 중 최소값
s = input()
group0 = 0
group1 = 0
prev = ''
for char in s:
    if prev != char:
        if char == '1':
            group1 += 1
        else:
            group0 += 1
    prev = char
print(min(group0, group1))
