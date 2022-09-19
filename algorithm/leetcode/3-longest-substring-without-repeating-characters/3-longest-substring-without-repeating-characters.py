# count 변수를 두고 result 갱신
# 문자열 순회하면서 방문했던 문자열 나오면 count 초기화, result max 갱신
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        substring = ""
        for i in range(len(s)):
            if s[i] in substring:
                longest = max(longest, len(substring))
                j = substring.find(s[i])
                substring = substring[j+1:]+s[i]
            else:
                substring += s[i]
        
        longest = max(longest, len(substring))    
        return longest