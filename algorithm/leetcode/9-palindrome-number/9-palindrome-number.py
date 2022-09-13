# 숫자가 주어졌을때 팰린드롬인지 검사하라
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]