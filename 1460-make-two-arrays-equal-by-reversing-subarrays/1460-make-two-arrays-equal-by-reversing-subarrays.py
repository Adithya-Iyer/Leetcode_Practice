class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # h1, h2 = {}, {}
        # for a in arr:
        #     h1[a] = h1.get(a,0) + 1
        # for t in target:
        #     h2[t] = h2.get(t,0) + 1
        # return h1==h2
        target.sort()
        arr.sort()
        return arr==target