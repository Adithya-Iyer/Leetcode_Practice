class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        n = len(differences)
        maxP = maxN = 0
        endP = endN = 0
        for d in differences:
            endP = max(endP, 0) + d
            endN = max(endN, 0) - d
            maxP = max(maxP, endP)
            maxN = max(maxN, endN)
        return max(0,upper-lower+1-max(maxP,maxN))