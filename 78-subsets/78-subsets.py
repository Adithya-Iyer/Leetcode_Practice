class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powers = []
        n = len(nums)
        curr = []
        def gen(ind: int):
            powers.append(curr.copy())
            for i in range(ind, n):
                curr.append(nums[i])
                gen(i+1)
                curr.pop()
        gen(0)
        return powers
        