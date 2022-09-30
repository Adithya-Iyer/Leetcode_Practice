class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startValue = 1
        negSum = 1
        for n in nums:
            negSum += n
            if negSum < 1:
                diff = 1-negSum
                startValue += diff
                negSum += diff
        return startValue