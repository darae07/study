# A 고정 비용, B 제품당 생산 비용, C 노드북 가격
# A+B*D<D*C => a/(c-b)<d => d=ceil(a/(c-b))
# 출력 손익분기점 = 흑자 전환 판매량 = D

import math
a, b, c = map(int, input().split())
if c-b > 0:  # 판매가가 생산비용보다 높아야 이득이 발생할 수 있다.
    point = a/(c-b)
    sales_count = int(point)+1 if point % 1 == 0 else math.ceil(point)
    print(-1 if sales_count < 0 else sales_count)
else:
    print(-1)
