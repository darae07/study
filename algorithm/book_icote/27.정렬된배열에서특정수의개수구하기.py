# -*- coding:utf-8 -*-
# x 특정 값
# data: 오름차순 정렬된 수열
# x의 등장 갯수
from bisect import bisect_left, bisect_right
from turtle import right


def solution(x, data):
    left = bisect_left(data, x)
    right = bisect_right(data, x)
    if right > left:
        return right-left
    return -1


def count_by_value(data, x):
    n = len(data)
    a = get_bisect_left(data, x, 0, n-1)
    if a == None:
        return 0
    b = get_bisect_right(data, x, 0, n-1)
    return b-a+1

# 값이 x인 최소 인덱스 -> 값 비교시 인덱스-1도 비교


def get_bisect_left(data, x, start,  end):
    if start > end:
        return None
    mid = (start+end)//2
    if (mid == 0 or x > data[mid-1]) and data[mid] == x:
        return mid
    elif data[mid] >= x:
        return get_bisect_left(data, x, start, mid-1)
    else:
        return get_bisect_left(data, x, mid+1, end)

# 값이 x인 최대 인덱스 -> 값 비교시 인덱스 +1도 비교


def get_bisect_right(data, x, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if (mid == len(data)-1 or x < data[mid+1]) and data[mid] == x:
        return mid
    elif data[mid] > x:
        return get_bisect_right(data, x, start, mid-1)
    else:
        return get_bisect_right(data, x, mid+1, end)


def solution2(x, data):
    count = count_by_value(data, x)
    if count == 0:
        return -1
    return count


print(solution2(2, [1, 1, 2, 2, 2, 2, 3]))
