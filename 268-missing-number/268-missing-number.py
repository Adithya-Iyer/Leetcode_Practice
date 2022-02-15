class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        #Time=O(nlogn) and Space=O(1) approach
        """nums.sort()
        for i in range(n):
            if(i!=nums[i]):
                return i
        return n"""
        #Time=O(n) and Space=O(n) approach
        arr = [None for i in range(n+1)]
        for x in nums:
            arr[x] = 1
        for i in range(n+1):
            if (arr[i]==None):
                return i
        return n