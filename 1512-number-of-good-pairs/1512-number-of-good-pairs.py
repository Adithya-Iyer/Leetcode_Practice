class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n,0) + 1
        vals = list(hashmap.values())
        gp = 0
        for v in vals:
            gp += v*(v-1)//2
        return gp