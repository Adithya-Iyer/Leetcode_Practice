class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n<3:
            return True
        toggle = -1
        while(n>0):
            if n%2==toggle:
                return False
            toggle = n%2
            n >>= 1
        return True