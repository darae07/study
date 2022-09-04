# 1. 오답
# 정문에서 가장 가까운 방
# T 테스트 케이스 갯수
# H, W, N = 층수, 각층 방수, 몇번째 손님
# room_number = n번째 손님에게 배정된 방 번호
# 방번호 형태 YXX | YYXX => Y 층수, XX 엘리베이터부터 세었을때 번호
# 1순위 XX 작게
# 2순위 YY 작게
# 101, 201, 301, ..., H01, ... , HW
# x = n//h
# y = n%h
# 입력 값이 작기 때문에 divmod보다 //,%가 빠를 듯

t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    x = n//h+1
    y = n % h
    y = h if y == 0 else y
    room_number = f'{y}{x if x>9 else "0"+str(x)}'
    print(room_number)


# 2. 정답
# n%h == 0인 경우 - 꼭대기 층. 이미 몫으로 1 올라갔기 때문에 이 경우를 제외하고 x+=1을 해줌(서수 맞춤)

t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    x = n//h
    y = n % h
    if y == 0:
        y = h
    else:
        x += 1
    room_number = f'{y}{x if x>9 else "0"+str(x)}'
    print(room_number)
