class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n,0) + 1
        ret = 0
        for k in hashmap:
            if (k-1) in hashmap:
                ret = max(ret, (hashmap[k]+hashmap[k-1]))
            if (k+1) in hashmap:
                ret = max(ret, (hashmap[k]+hashmap[k+1]))
        return ret