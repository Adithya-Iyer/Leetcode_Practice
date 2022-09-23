class Solution:
    def concatenatedBinary(self, n: int) -> int:
        num = 0
        digits = 0
        for i in range(1,n+1):
            if i&(i-1)==0:
                digits += 1
            num *= 2**digits
            num += i
            num %= 10**9+7
        return num