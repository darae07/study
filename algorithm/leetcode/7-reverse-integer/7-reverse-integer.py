# 32비트 정수 x 뒤집기
# 32비트 정수 범위 벗어나면 0 반환
# 부호 저장, 숫자 문자열로 변환 뒤 뒤집기, 부호 붙이고 유효성 판별
class Solution:
    def reverse(self, x: int) -> int:
        natural = True if x >= 0 else False
        if not natural:
            x*=-1
        reverse = int(''.join(reversed(list(str(x)))))
        if not natural:
            reverse*= -1
        
        if -2**31>reverse or 2**31-1<reverse:
            return 0
        else:
            return reverse
        