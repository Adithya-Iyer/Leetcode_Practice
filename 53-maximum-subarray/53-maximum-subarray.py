class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        le = len(nums)
        mss = prev = nums[0]
        for i in range(1, le):
            prev = max(prev+nums[i], nums[i])
            mss = max(prev, mss)
        return mss