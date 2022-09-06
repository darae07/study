# 피보나치
# 조건 0, 1일때 값 반환, 아니면 fn = f(n-1)+f(n-2) 반환
# 중복 함수 호출이 많기 때문에 캐시로 이미 구한 값에 대해서는 다시 연산하지 않도록 함
dic = {}


def fibonachi(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in dic:
        fib = dic[n]
    else:
        fib = fibonachi(n-1)+fibonachi(n-2)
    dic[n] = fib
    return fib


n = int(input())
print(fibonachi(n))
