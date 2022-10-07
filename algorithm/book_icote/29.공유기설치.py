# 최대 거리의 범위를 최대부터 줄여나가기
# 인접 최대 거리 = mid
# 이진 탐색으로 최대 거리를 찾기
# mid 만족시키도록 공유기 설치
# 공유기개수 >= c -> 범위 우측 탐색
# 개수 < c -> 범위 좌측 탐색

n, c = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))

array.sort()
start, end = 1, array[-1]-array[0]
result = 0

while start <= end:
    count = 1
    mid = (start+end)//2
    v = array[0]
    for i in range(1, n):
        if array[i]-v >= mid:
            count += 1
            v = array[i]
    if count >= c:
        start = mid+1
        result = mid
    else:
        end = mid-1
print(result)
