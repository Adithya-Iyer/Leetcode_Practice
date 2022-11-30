class Solution:
    def integerBreak(self, n: int) -> int:
        if n<=3:
            return n-1
        r = n%3
        t = n//3
        ret = int(3**(t-1))
        if r==1:
            return ret*4
        return ret*max(r,1)*3