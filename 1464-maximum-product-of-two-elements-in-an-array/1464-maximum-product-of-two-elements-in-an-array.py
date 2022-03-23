class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        ln = len(nums)
        ret = (nums[ln-1]-1)*(nums[ln-2]-1)
        return ret