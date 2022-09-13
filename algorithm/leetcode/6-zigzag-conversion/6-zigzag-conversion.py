# 지그재그 패턴으로 쓰인 문자열 s
# 행 개수 numRows
# 줄별로 읽은 문자열 반환
# 열 - numRows 만큼 한글자씩
# 대각선 - numRows -2
# {0: 'pin', 1: 'alsig', ...}
# 문자열 반복, 인덱스 % numRows*2-2 = m
# m<numRows -> dic에 바로 추가
# 아니면 i = (numRows - (m - numRows +1))%numRows = (2*numRows-m-1)%numRows
# dic[i]에 추가
# 반복 종료후 객체 값 합치기

from collections import defaultdict
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        dic = defaultdict(str)
        for i in range(len(s)):
            zig_i = i%(1 if numRows == 1 else numRows*2-2)
            if zig_i>=numRows:
                zig_i = (2*numRows-zig_i-1)%numRows-1
            dic[zig_i] += s[i]
        result = ''
        for key in dic:
            result += dic[key]
        return result