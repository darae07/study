# 2,3,5만을 소인수(약수)로 가지는 수
def solution(n):
    numbers = [False]*(1001)
    numbers[1] = True
    for i in range(2, 1001):
        c = i
        while c > 1:
            if c % 2 == 0:
                c /= 2
            elif c % 3 == 0:
                c /= 3
            elif c % 5 == 0:
                c /= 5
            else:
                break
        if c == 1:
            numbers[i] = True
    dp = [i for i in range(1001) if numbers[i]]
    return dp[n-1]


# i번째 못생긴수를 갱신해 나가기
# 1번째 못생긴수 = 1
# 2,3,5의 1번째 배수는 2,3,5
# 2번째 배수는 4,6,10
# 2,3,5의 다음 배수 값과 현재 몇번째 배수인지를 저장

def solution2(n):
    ugly = [0]*(n+1)
    ugly[1] = 1
    i2 = i3 = i5 = 1
    next2, next3, next5 = 2, 3, 5

    for i in range(2, n+1):
        ugly[i] = min(next2, next3, next5)
        # 배수를 사용했으면 업데이트
        if ugly[i] == next2:
            i2 += 1
            next2 = ugly[i2]*2
        if ugly[i] == next3:
            i3 += 1
            next3 = ugly[i3]*3
        if ugly[i] == next5:
            i5 += 1
            next5 = ugly[i5]*5
    return ugly[n]


print(solution2(10))
