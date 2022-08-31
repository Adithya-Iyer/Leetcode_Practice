class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        nums = []
        l = m + n
        i = j = 0
        while (i<m) and (j<n):
            if nums1[i]<nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        if i==m:
            nums.extend(nums2[j:])
        else:
            nums.extend(nums1[i:])
        if l%2==0:
            return (nums[l//2]+nums[(l//2)-1])/2
        return nums[l//2]