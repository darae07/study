# 뒤집기
# 크기 비교 후 큰 값 출력

a, b = map(lambda x: int(x[::-1]), input().split())
print(max(a, b))
