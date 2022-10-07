class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = j = 0
        while(j<n):
            if nums[j]==val:
                j += 1
            else:
                nums[i] = nums[j]
                i, j = i+1, j+1
        return i