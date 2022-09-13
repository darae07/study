class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = min([len(s) for s in strs])
        prefix = ''
        for i in range(n):
            ith_elements = set([s[i] for s in strs])
            if len(ith_elements)>1:
                break
            else:
                prefix += list(ith_elements)[0]
        return prefix