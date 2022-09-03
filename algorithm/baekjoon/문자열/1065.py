# 1부터 입력값까지 루프
# 반복중 숫자가 각 자리별로 등차수열인지 검사
# 등차수열이라면 정답 +=1
# 정답 출력

# 이런 문제에서 조건 파악하는 방법?

n = int(input())
hansu = 0
for x in range(1, n+1):
    num_list = list(map(int, str(x)))
    if x < 100:
        hansu += 1
    elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
        hansu += 1
print(hansu)
