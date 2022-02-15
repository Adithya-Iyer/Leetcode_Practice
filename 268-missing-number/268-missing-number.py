class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #O(nlogn) approach
        nums.sort()
        n = len(nums)
        for i in range(n):
            if(i!=nums[i]):
                return i
        return n