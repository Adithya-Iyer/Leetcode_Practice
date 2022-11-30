class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<1:
            return False
        l = log(n,4)
        return (l==int(l))