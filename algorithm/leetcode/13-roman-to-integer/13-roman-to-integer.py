class Solution:
    symbol = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    def romanToInt(self, s: str) -> int:
        number = 0
        for i in range(len(s)):
            char = s[i]
            val = self.symbol[char]
            if i < len(s)-1 and val < self.symbol[s[i+1]]:
                number -= val
            else:
                number+=val
        return number        
        