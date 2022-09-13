class Solution:
    def longestPalindrome(self, s: str) -> str:
        def get_palindrome(s, l, r):
            while l>=0 and r<len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        palindrome = ''
        for i in range(len(s)):
            odd = get_palindrome(s, i,i)
            even = get_palindrome(s, i, i+1)
            if len(odd) > len(even):
                if len(odd) > len(palindrome):
                    palindrome = odd
            else:
                if len(even) > len(palindrome):
                    palindrome = even
        return palindrome