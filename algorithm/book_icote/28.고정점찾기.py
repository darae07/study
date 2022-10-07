# mid == data[mid] > 고정점
# mid < data -> 좌측
# mid > data -> 우측

def solution(array):
    length = len(array)
    mid = (length-1)//2
    s, e = 0, length-1
    while s <= e:
        if mid == array[mid]:
            return array[mid]
        if mid < array[mid]:
            e = mid-1
            mid = (s+e)//2
        else:
            s = mid+1
            mid = (s+e)//2
    return -1


print(solution([-15, -6, 1, 3, 7]))
