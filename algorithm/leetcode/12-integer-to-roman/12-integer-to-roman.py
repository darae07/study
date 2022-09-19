class Solution:
    symbol = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    def intToRoman(self, num: int) -> str:
        if num == 0:
            return ''
        expon = len(str(num))-1
        position = 10**expon
        m = num//position
        coef = ''
        if m >= 9:
            coef += (self.symbol[position] + self.symbol[position*10])
        elif m >= 4:
            coef += self.symbol[position*5]
            extra = self.symbol[position]*(1 if m == 4 else m-5)
            if m>5:
                coef+= extra
            elif m<5:
                coef = extra+coef
        else:
            coef += self.symbol[position]*m
        return coef + self.intToRoman(num%position)        