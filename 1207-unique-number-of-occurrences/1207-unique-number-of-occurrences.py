class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
        for n in arr:
            hashmap[n] = hashmap.get(n,0)+1
        v = hashmap.values()
        return (len(v)==len(set(v)))