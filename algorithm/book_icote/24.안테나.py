# n채의 집
# 집의 위치 배열
# 한 곳에 안테나 설치
# 안테나로부터 모든 집까지 거리 합이 최소 되도록
# 안테나는 집이 있는 위치에만 설치 가능, 동일한 위치에 여러 집 존재 가능
# 집의 위치 정렬해서 중간값. -> 여러개일 경우 작은 값이기 때문에 바닥함수 취함
# len//2, 짝수일 경우 -1
n = int(input())
house = list(map(int, input().split()))
house.sort()
len_house = len(house)
index = len_house//2 if len_house % 2 == 1 else len_house//2-1
print(house[index])
print(house[(n-1)//2])  # 중간 인덱스 구할때 (n-1)//2
