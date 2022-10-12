class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        """
        [1,1,2,3,-3-,4,4,8,8] L
        [1,1,2,2,-3-,4,4,5,5] C
        [1,1,2,2,-3-,3,4,5,5] R
        [3,3,7,-7-,10,11,11] R
        [3,3,7,-10-,10,11,11] L
        [3,3,7,-7-,10,10,11] R 
        """
        if n==1:
            return nums[0]
        i, j = 0, n-1
        while(j>i+2):
            mid = (i+j)//2
            if mid%2==0:
                if nums[mid]==nums[mid-1]:
                    j = mid-2
                elif nums[mid]==nums[mid+1]:
                    i = mid+2
                else:
                    return nums[mid]
            else:
                if nums[mid]==nums[mid-1]:
                    i = mid+1
                else:
                    j = mid-1
        if j==i:
            return nums[i]
        if nums[i]==nums[i+1]:
            return nums[j]
        else:
            return nums[i]
        