class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for n in nums:
            hm[n] = hm.get(n,0) + 1
        hm = sorted(hm, key=hm.get, reverse=True)
        return hm[:k]