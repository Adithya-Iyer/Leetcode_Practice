class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = 0
        for n in nums:
            unique ^= n
        return unique