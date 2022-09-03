# 문자열 순회하면서 다음 문자열과 같으면 넘어감
# 다를때 이후 문자열에 등장한다면 그룹 단어가 아니다

n = int(input())
answer = n
for _ in range(n):
    word = input()
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            pass
        elif word[i] in word[i+1:]:
            answer -= 1
            break
print(answer)
