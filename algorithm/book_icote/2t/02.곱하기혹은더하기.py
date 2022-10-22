# 각자리가 숫자로 이루어진 문자열 s
# 왼쪽부터 하나씩 확인하며 x 또는 + 연산
# 가장 큰 수 구하기
# 모든 연산은 왼쪽에서 오른쪽으로 이루어짐
# 한쪽이 1보다 작거나 같으면 +연산
# 나머지 모두 곱하기 연산

s = input()
result = 0
for char in s:
    char = int(char)
    if result <= 1 or char <= 1:
        result += char
    else:
        result *= char
print(result)
