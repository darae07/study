# 1. 오답
n = int(input())

che = [False, False]+[True]*(n-1)
for i in range(2, n+1):
    if che[i]:
        for j in range(2*i, n+1, i):
            che[i] = False
primes = list(filter(lambda x: che[x], range(2, n+1)))
while n > 1:
    for prime in primes:
        if n % prime == 0:
            print(prime)
            n = n//prime
            break


# 2. 느린 정답 - 2부터 n 까지 다 구하기
# 소요시간 O(n) - 1612ms
n = int(input())

prime = 2
while n > 1:
    if n % prime == 0:
        print(prime)
        n = n//prime
    else:
        prime += 1

# 3. 최적화한 정답 - 2부터 루트n까지만 구하기
# 소요시간 O(log n) - 68ms
n = int(input())
r = int(n**0.5)
prime = 2
while r >= prime:
    while n % prime == 0:
        print(prime)
        n = n//prime
    prime += 1
if n > 1:
    print(n)
