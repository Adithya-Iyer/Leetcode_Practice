class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        money = [nums[0], max(nums[0], nums[1])]
        if n==2:
            return money.pop()
        for i in range(2, n):
            money.append(max(nums[i]+money[i-2], money[i-1]))
        return money.pop()