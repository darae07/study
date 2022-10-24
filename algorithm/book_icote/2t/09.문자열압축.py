# 문자열 모든 압축 단위에 대해 길이 검사
# 최소값 갱신
# 길이별 반복할 때마다 시작 문자열=문자열[0:길이], count = 0
# 시작 문자열 = 현재문자열 -> count+=1
# 아니면 시작문자열, 횟수로 문자열에 더하고, 시작문자열 = 현재문자열 갱신
# 문자열 길이 갱신
def solution(s):
    answer = 1e9
    for i in range(1, len(s)+1):
        prev = s[0:i]
        count = 1
        curr_s = ''
        for j in range(i, len(s), i):
            cs = s[j:j+i]
            if prev == cs:
                count += 1
            else:
                if count > 1:
                    curr_s += str(count)+prev
                else:
                    curr_s += prev
                prev = cs
                count = 1
        if count > 1:
            curr_s += str(count)+prev
        else:
            curr_s += prev
        print(prev, curr_s)
        answer = min(len(curr_s), answer)
    return answer


print(solution("aabbaccc"))
