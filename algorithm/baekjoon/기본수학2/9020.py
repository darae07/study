# T = 테스트 케이스 갯수
# n = 4<=n<=10000, n%2=0
# 골드바흐 파티션 : 짝수를 두개의 소수의 합으로 나타내야함.
# 파티션 여러개 존재할땐 두 소수의 차이가 가장 작은것을 출력 -> n의 절반부터 2까지 역순으로 반복
# 소수 체를 구해주는 함수
# n에 따라 체를 구하고, n의 절반부터 2까지 역순으로 반복하며 체의 인덱스가 참인지 검사
# 참이면 che[n-i]가 참인지 검사하여 참이면 i, n-i 출력

def get_che(n):
    che = [False, False]+[True]*(n-1)
    for num in range(2, n+1):
        if che[num]:
            for multiple in range(2*num, n+1, num):
                che[multiple] = False
    return che


t = int(input())
for _ in range(t):
    n = int(input())
    che = get_che(n)
    for num in range(n//2, 1, -1):  # 처음 오답 사유, 까지를 2로 줘서 2가 미포함됨
        if che[num]:
            if che[n-num]:
                print(f'{num} {n-num}')
                break


# 범위내 체를 미리 구해놓으면 좀더 빠름

che = [False, False]+[True]*(10000-1)
for num in range(2, 10000+1):
    if che[num]:
        for multiple in range(2*num, 10000+1, num):
            che[multiple] = False

t = int(input())
for _ in range(t):
    n = int(input())
    for num in range(n//2, 1, -1):
        if che[num]:
            if che[n-num]:
                print(f'{num} {n-num}')
                break
