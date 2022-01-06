class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sumDict = {}
        for i in range(len(nums)):
            n = nums[i]
            if n in sumDict:
                return ([sumDict[n],i])
            sumDict[(target-n)] = i
        return ([0,0])
