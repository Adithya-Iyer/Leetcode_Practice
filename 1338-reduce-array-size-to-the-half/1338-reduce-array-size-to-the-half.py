class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        hm = {}
        for el in arr:
            hm[el] = hm.get(el,0) + 1
        vals = sorted(hm.values(), reverse=True)
        rem = n
        target = n//2
        i = 0
        while rem>target:
            rem -= vals[i]
            i += 1
        return i