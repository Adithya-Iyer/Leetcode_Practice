class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cntDict = {}
        for i in range(len(nums)):
            n = nums[i]
            if n in cntDict:
                cntDict[n]+=1
            else:
                cntDict[n]=1
            if cntDict[n]>1:
                return True
            if i>=k:
                rem = nums[i-k]
                cntDict[rem]-=1
        return False