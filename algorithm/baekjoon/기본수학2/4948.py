# 범위의 소수를 모두 구해놓고 시작
length = 123456*2
che = [False, False]+[True]*(length)
for i in range(2, length+1):
    if che[i]:
        for j in range(2*i, length+1, i):
            che[j] = False
while True:
    m = int(input())
    if m == 0:
        break
    n = m*2
    primes_count = len(list(filter(lambda x: che[x], range(m+1, n+1))))
    print(primes_count)
