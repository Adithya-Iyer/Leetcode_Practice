class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sumDict = {}
        for i in range(len(nums)):
            n = nums[i]
            if n in sumDict:
                yield ([nums[sumDict[n]],n])
            sumDict[(target-n)] = i
        return 
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out = []
        n = len(nums)
        nums.sort()

        #Brute Force = O(n^3)
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if ((nums[i] + nums[j] + nums[k])==0):
                        insert = [nums[i] , nums[j] , nums[k]]
                        insert.sort()
                        if (insert not in out):
                            out.append(insert)

        #Using TwoSum logic = O(n^2)
        for i in range(n-2):
            x = nums[i]
            two_sums = self.twoSum(nums[i+1:], (-x))
            print(x, ' ', two_sums)
            if (two_sums == None):
                continue
            for ts in two_sums:
                triplet = [x]
                triplet.extend(ts)
                if (triplet not in out):
                    out.append(triplet)
        
        return (out)
      
