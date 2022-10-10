class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l, p, r = [], [], []
        for n in nums:
            if n<pivot:
                l.append(n)
            elif n>pivot:
                r.append(n)
            else:
                p.append(n)
        return l+p+r