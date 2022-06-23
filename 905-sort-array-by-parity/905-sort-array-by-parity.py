class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ret = []
        for n in nums:
            if n%2==0:
                ret.append(n)
        for n in nums:
            if n%2!=0:
                ret.append(n)
        return ret