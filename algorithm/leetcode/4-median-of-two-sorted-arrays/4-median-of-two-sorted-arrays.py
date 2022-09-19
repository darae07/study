# 정렬된 배열 2개가 주어졌을때, log m+n에 중간값을 찾아라
# 중간값 = 정렬된 합쳐진 배열의 중간 인덱스(짝수인 경우 가운데 2값 더하고 //2)
# 중앙 인덱스는 배열 길이의 총 합(total)의 중앙 1개 혹은 2개
# 중앙 인덱스 좌, 우측 원소의 개수는 같음.
# 중앙 인덱스를 바르게 결정한다면, 좌측으로 분할된 배열의 오른쪽 끝값은 다른 배열의 중간값(오른쪽 끝+1인덱스)보다 작거나 같다.(조건1) 
# 조건을 만족할때까지 올바른 분할을 찾아간다.
# 기준이 되는 배열은 둘 중 짧은 배열로 하고, 기준 배열의 분할을 배열 절반 길이로 나누고 다른 배열은 total//2- 기준 배열 분할 길이로 한다.
# 기준이 되는 배열의 분할 우극값이 다른 배열 중간값보다 크면, 기준 배열 분할을 축소하고, 반대의 경우 기준 배열 분할을 확대한다.
# 조건1을 만족한다면, total이 홀수이면 중간값의 최소값을, 짝수이면 (분할값의 최대값 + 중간값의 최소값)/2를 반환한다.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        total = len(nums1)+ len(nums2)
        half = total //2 # 중앙 기준 좌측으로 분할된 원소의 개수
        
        l,r = 0, len(nums1)-1
        while True:
            p1 = (l+r)//2 # nums1을 위한 파티션 = 우측 끝 인덱스
            p2 = half - p1 -2 # nums2를 위한 파티션 = 인덱스는 0부터 시작하므로 -2
            end1 = nums1[p1] if p1>= 0 else float('-inf')
            mid1 = nums1[p1+1] if (p1+1)<len(nums1) else float('inf')
            end2 = nums2[p2] if p2>=0 else float('-inf')
            mid2 = nums2[p2+1] if (p2+1)<len(nums2) else float('inf')
            
            if end1 <= mid2 and end2 <= mid1: # 조건1 만족
                if total %2: # 홀수
                    return min(mid1, mid2)
                else:
                    return (max(end1, end2) + min(mid1, mid2))/2
            elif end1 > mid2:
                r = p1-1
            else:
                l = p1+1
        