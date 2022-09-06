# 1. 시간복잡도 72
m = 64
n = 65

visited = [False, False]+[True]*(n-1)
primes = []

for i in range(2, n+1):
    if visited[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            visited[j] = False

primes = list(filter(lambda i: visited[i], range(m, n+1)))

if len(primes) > 0:
    print(sum(primes))
    print(min(primes))
else:
    print(-1)


# 2. 시간복잡도 약간 개선 72->68
m = int(input())
n = int(input())

visited = [False, False]+[True]*(n-1)

for i in range(2, n+1):
    if visited[i]:
        for j in range(2*i, n+1, i):
            visited[j] = False

primes = list(filter(lambda i: visited[i], range(m, n+1)))

if len(primes) > 0:
    print(sum(primes))
    print(min(primes))
else:
    print(-1)
