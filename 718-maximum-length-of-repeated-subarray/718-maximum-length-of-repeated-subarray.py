class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        cnt = [[0 for i in range(n+1)] for j in range(m+1)]
        ret = 0
        for j in range(1, m+1):
            for i in range(1, n+1):
                if nums1[j-1]==nums2[i-1]:
                    cnt[j][i] = 1 + cnt[j-1][i-1]
                    ret = max(ret, cnt[j][i])
                else:
                    cnt[j][i] = 0
        return ret