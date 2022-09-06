# 1. 오답
def factorial(n):
    if n < 2:
        return n
    return n*factorial(n-1)


n = int(input())
print(factorial(n))

# 2. 수정된 정답
# 0 팩토리얼이 1인 이유 - 1! = 1 = 1*0!. 따라서 0!이 1이어야 식이 성립할 수 있다.


def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)


n = int(input())
print(factorial(n))
