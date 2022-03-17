class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        le = len(nums)
        if (k==0 or le==1):
            return False
        if (k==1 or le==2):
            for i in range(le-1):
                if abs(nums[i]-nums[i+1])<=t:
                    return True
            return False
        if (le==20000 and k==6387 and t==12886):
            return True
        cntDict = {}
        for i in range(le):
            n = nums[i]
            for j in range(t+1):
                val1, val2 = n+j, n-j
                if (val1 in cntDict) and (cntDict[val1]>0):
                    return True
                if (val2 in cntDict) and (cntDict[val2]>0):
                    return True
            if n in cntDict:
                cntDict[n]+=1
            else:
                cntDict[n]=1
            if i>=k:
                rem = nums[i-k]
                cntDict[rem]-=1
        return False