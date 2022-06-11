import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap = []
        for i in range(k):
            heapq.heappush(heap, nums[i])
        for i in range(k, n):
            heapq.heappush(heap, nums[i])
            heapq.heappop(heap)
        return heapq.heappop(heap)