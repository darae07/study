n = int(input())
for _ in range(n):
    num, chars = input().split()
    num = int(num)
    added_chars = ''.join(map(lambda x: x*num, list(chars)))
    print(added_chars)
