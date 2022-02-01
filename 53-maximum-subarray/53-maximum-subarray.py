class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        le = len(nums)
        mss = nums[0]
        ss = [mss]
        for i in range(1, le):
            ss.append(max(ss[i-1]+nums[i], nums[i]))
            mss = max(ss[i], mss)
        return mss