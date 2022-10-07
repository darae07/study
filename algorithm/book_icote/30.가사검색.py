# 단어를 길이에 따라 나누고 정렬
# 각 쿼리에 대해 bisect_left, right 탐색으로 개수 구함
# ?->a로 치환한 문자열보다 크거나 같은 index, z로 치환한 문자열보다 작거나 같은 index
# 접두사에 와일드카드 나온 경우를 위한 뒤집은 단어를 담고있는 리스트

from bisect import bisect_left, bisect_right


def count_range(array, left_value, right_value):
    left = bisect_left(array, left_value)
    right = bisect_right(array, right_value)
    return right - left


def solution(words, queries):
    array = [[] for _ in range(10001)]
    reversed_array = [[] for _ in range(10001)]
    answer = []

    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    for q in queries:
        if q[0] != '?':
            res = count_range(array[len(q)], q.replace(
                '?', 'a'), q.replace('?', 'z'))
        else:
            res = count_range(
                reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(res)
    return answer
