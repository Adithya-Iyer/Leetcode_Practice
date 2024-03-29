class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start+(2*i) for i in range(n)]
        ret = nums[0]
        for i in range(1,n):
            ret ^= nums[i]
        return ret