class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n,0) + 1
        vals = list(hashmap.values())
        gp = 0
        # Approach 1
        # for v in vals:
        #     gp += v*(v-1)//2
        # Approach 2
        highest = max(vals)
        pairs = [0,0]
        for i in range(1,highest):
            pairs.append(pairs[i]+i)
        for v in vals:
            gp += pairs[v]
        return gp