# l -> 0 부터 nums 끝까지 순회
# r -> val로 치환된 최소 인덱스를 저장

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:     
        l,r = 0, len(nums)-1
        c = 0
        m = len(nums)
        while l<m:
            if nums[l] == val:
                while r>l and nums[r] == val:
                    r-=1
                if r <= l: 
                    c+=1
                    nums[l] = -1
                else:
                    nums[l], nums[r] = nums[r], nums[l]
                    m = r
            l+=1
         
        return l-c
