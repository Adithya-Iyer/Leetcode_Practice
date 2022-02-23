class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k, n = 0, len(nums)
        for i in range(1, n):
            if (nums[i]!=nums[k]):
                k+=1
                nums[k]=nums[i]
        return (k+1)
                