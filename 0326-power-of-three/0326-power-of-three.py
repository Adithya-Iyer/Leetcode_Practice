class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<1:
            return False
        l = log(n,3)
        x = log(n/3,3)
        return (l==int(l) or x==int(x))