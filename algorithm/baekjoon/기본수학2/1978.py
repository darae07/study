# 소수 판별. 왜 제곱근까지 구하면 안되는건지?
# 식의 오류를 잡기
import math
n = 4
nums = [1, 3, 5, 7]
sqrts = list(map(lambda x: math.ceil(x**(1/2)), nums))

for i, num in enumerate(sqrts):
    if nums[i] == 1:
        n -= 1
    for s in range(2, int(num)):

        if nums[i] % s == 0:
            n -= 1
            break
print(n)


n = int(input())
nums = list(map(int, input().split()))

for num in nums:
    if num == 1:
        n -= 1
    for s in range(2, num):
        if num % s == 0:
            n -= 1
            break
print(n)
