class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(min(strs, key=len))
        prefix = ''
        for i in range(n):
            c = strs[0][i]
            if all([s[i] == c for s in strs]):
                prefix += c
            else:
                break
        return prefix