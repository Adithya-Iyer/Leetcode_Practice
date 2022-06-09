class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        n = len(nums)
        for i in range(n):
            ni = nums[i]
            freq[ni] = freq.get(ni, 0) + 1
        for key in freq:
            if freq[key]>n//2:
                return key
        return 0