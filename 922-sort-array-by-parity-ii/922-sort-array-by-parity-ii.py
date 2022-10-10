class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if nums[0]%2 == 1:
            x = 1
            while(nums[x]%2 != 0):
                x += 1
            nums[0], nums[x] = nums[x], nums[0]
        for i in range(0, n-1):
            t = j = i + 1
            f = nums[i]%2
            while(nums[j]%2 == f):
                j += 1
            if t!=j:
                nums[t], nums[j] = nums[j], nums[t]
        return nums