class Solution:
    def sumBase(self, n: int, k: int) -> int:
        num = 0
        while (n>0):
            num += n%k
            n //= k
        return num