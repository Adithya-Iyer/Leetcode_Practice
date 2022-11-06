class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hn = zip(heights,names)
        hn = reversed(sorted(hn))
        return [n for h,n in hn]