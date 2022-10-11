class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        exists = {}
        n = len(nums)
        if (max(nums)-min(nums))<2:
            return False
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    if i in exists:
                        exists[i].append(j)
                    else:
                        exists[i] = [j]
        for k in exists:
            for v in exists[k]:
                if v in exists:
                    return True
        return False