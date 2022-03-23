class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxHeap = []
        ln = len(nums)
        for i in range(ln):
            heappush(maxHeap,-nums[i])
        ret = 1
        for i in range(2):
            ret*=heappop(maxHeap)+1
        return ret