# 배열 정렬
# 인덱스와 투포인터 - 인덱스를 기준으로 우측 데이터에 l, r 포인터 이동하며 합을 구함 - 0이면 추가
# 인덱스 기준 좌측 데이터는 이미 검색이 완료됨
# l<r동안 반복, 정렬된 값이므로 합이 0보다 작으면 l+=1, 크면 r-=1
# 합이 0이면 정답 추가후 같은값 스킵 - l,r 다음,직전값 비교하여 같으면 증감으로 스킵
from itertools import combinations
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l,r= i+1, len(nums)-1
            while(l<r):
                s = nums[i]+nums[l]+nums[r]
                if s < 0:
                    l+=1
                elif s>0:
                    r-=1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return result