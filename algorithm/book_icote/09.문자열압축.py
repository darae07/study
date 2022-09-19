# -*- coding:utf-8 -*-

def get_len(s, k):
    l = 0
    prev = ''
    for i in range(0, len(s)-k, k):
        if s[i:i+k+1] not in prev:
            l += k
        print(i, k, s[i:i+k], s[i+k:i+2*k])
        if s[i:i+k+1] != s[i+k:i+2*k+1]:
            l += 1
    return l+len(s) % k


def solution(s):
    answer = len(s)
    for i in range(1, len(s)):
        a = get_len(s, i)
        print(a)
        answer = min(answer, a)

    return answer

# 2.
# 압축 절반 이하여야 짧아짐
# 압축할 스텝마다 첫 스텝과 카운트 초기화, 문자열 스텝만큼 반복하며 현재 문자열과 이전 문자열을 비교
# 이전 문자열과 같으면 카운트 증가
# 다르면 이전 문자열을 압축 문자열에 결과 형태로 추가하고, 이전 문자열과 카운트 초기화
# 이전 문자열은 현재 문자열로, 첫 등장이므로 카운트 1로 초기화


def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2+1):
        compressed = ''
        prev = s[0:step]
        count = 1
        for j in range(step, len(s), step):
            curr = s[j:j+step]
            if prev == curr:
                count += 1
            else:
                compressed += str(count)+prev if count >= 2 else prev
                prev = curr
                count = 1
        compressed += str(count)+prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer
