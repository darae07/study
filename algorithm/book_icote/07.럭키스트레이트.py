# -*- coding:utf-8 -*-
#

n = input()
left = 0
right = 0
for i in range(len(n)):
    if i < len(n)//2:
        left += int(n[i])
    else:
        right += int(n[i])
print('LUCKY' if left == right else 'READY')
