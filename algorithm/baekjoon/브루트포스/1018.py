# n, m 크기의 보드(8<=n,m<=50)
# 체스판 칠하기 규칙 - 검-흰 번갈아서. 경우 두가지- 맨 위칸이 W or B
# 체스판 다시 칠할때, 칠해야 하는 최소 갯수 구하기
# w_first, b_first로 칠해야하는 수 각각 구해서 최소값을 반환하기
# 완전탐색. 모든 체스판을 살펴봐야 함.
# 반복 r = row, c = column
# w_first r,c가 짝수면 w, 홀수면 b가 되어야 함. 그렇지 않을때 카운트+1
# b_first r,c가 짝수면 b, 홀수면 w가 되어야 함. 그렇지 않을때 카운트+1
# r,c가 홀수 &&  -> w -> b_first += 1
#                 b -> w_first += 1
# 8*8 크기의 체스판으로 만들어야한다.

n, m = map(int, input().split())
cell_list = []
for _ in range(n):
    cell_list.append(input())

board_count = []
for area_left in range(n-7):
    for area_height in range(m-7):
        w_first = 0
        b_first = 0
        for i in range(area_left, area_left+8):
            for j in range(area_height, area_height+8):
                cell = cell_list[i][j]
                if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                    if cell == 'W':
                        b_first += 1
                    else:
                        w_first += 1
                else:
                    if cell == 'W':
                        w_first += 1
                    else:
                        b_first += 1
        board_count.append(min(w_first, b_first))
print(min(board_count))
