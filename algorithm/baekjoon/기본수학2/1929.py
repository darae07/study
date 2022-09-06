m, n = map(int, input().split())

che = [False, False]+[True]*(n-1)
for i in range(2, n+1):
    if che[i]:
        if i >= m:
            print(i)
        for j in range(2*i, n+1, i):
            che[j] = False
