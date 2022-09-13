# l,r
# area = (r-l-1)*(max(h[r], h[l]))
# i 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l,r = 0, n-1
        area = 0
        while l<r:
            area = max(area, min(height[l], height[r])*(r-l))
            if height[l] <= height[r]:
                l+=1
            else:
                r-=1
        return area